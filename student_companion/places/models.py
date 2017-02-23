from django.conf import settings
from django.core import files
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey

from google_places import GooglePlacesService


class PlaceCategoryQuerySet(models.QuerySet):
    pass


class PlaceCategory(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='category_children',
                            db_index=True,
                            verbose_name=_('parent category'))
    name = models.CharField(_('name'), max_length=40)
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    objects = PlaceCategoryQuerySet.as_manager()

    class Meta:
        verbose_name = _('place category')
        verbose_name_plural = _('place categories')

    def __str__(self):
        return self.name


class PlaceQuerySet(models.QuerySet):
    def visible(self):
        return self.filter(is_visible=True)

    def search(self, search_string):
        return self.filter(
            models.Q(name__icontains=search_string) |
            models.Q(tags__name__icontains=search_string)
        ).distinct()


class Place(models.Model):
    FREE = 0
    INEXPENSIVE = 1
    MODERATE = 2
    EXPENSIVE = 3
    VERY_EXPENSIVE = 4

    PRICE_LEVEL_CHOICES = (
        (FREE, _('free')),
        (INEXPENSIVE, _('inexpensive')),
        (MODERATE, _('moderate')),
        (EXPENSIVE, _('expensive')),
        (VERY_EXPENSIVE, _('very expensive')),
    )

    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     verbose_name=_('submitted by'),
                                     blank=True, null=True,
                                     related_name='submitted_places',
                                     related_query_name='submitted_place')
    is_visible = models.BooleanField(_('is visible'), default=False)
    google_places_id = models.CharField(_('Google API Place ID'),
                                        max_length=100,
                                        unique=True)
    categories = models.ManyToManyField('PlaceCategory', related_name='places',
                                        related_query_name='place',
                                        verbose_name=_('categories'),
                                        blank=True)
    description = models.TextField(_('description'), blank=True)
    website = models.URLField(_('website'), blank=True)
    google_maps_url = models.URLField(_('Google Maps URL'), blank=True)
    address = models.CharField(_('formatted address'), max_length=255,
                               blank=True)
    telephone_number = models.CharField(_('formatted telephone number'),
                                        max_length=15, blank=True)
    facebook_handle = models.CharField(_('Facebook username'), max_length=255,
                                       blank=True)
    twitter_handle = models.CharField(_('Twitter username'), max_length=255,
                                      blank=True)
    student_discount = models.CharField(_('student discount'), max_length=50,
                                        blank=True)
    opening_times = models.TextField(_('opening hours'), blank=True)
    price_level = models.PositiveSmallIntegerField(_('price level'),
                                                   choices=PRICE_LEVEL_CHOICES,
                                                   blank=True, null=True)
    tags = models.ManyToManyField('PlaceTag', blank=True,
                                  related_name='places',
                                  related_query_name='place')
    location_latitude = models.FloatField(_('latitude'), blank=True, null=True)
    location_longitude = models.FloatField(_('longitude'), blank=True,
                                           null=True)
    objects = PlaceQuerySet.as_manager()

    class Meta:
        verbose_name = _('place')
        verbose_name_plural = _('places')

    def __init__(self, *args, **kwargs):
        super(Place, self).__init__(*args, **kwargs)
        self.google_service = GooglePlacesService()

    def __str__(self):
        return self.name

    def get_place_from_google_api(self):
        if not self.google_places_id:
            raise Exception("Such place does not have Google Places API.")

        try:
            return self.google_service.get_place(self.google_places_id)
        except Exception:
            raise ValidationError("Google place ID is not valid.")


    def update_data_from_google_api(self, commit=True):
        place_json = self.get_place_from_google_api()

        if not self.name:
            self.name = place_json.get('name', '')

        if not self.slug:
            self.slug = '{}-{}'.format(
                slugify(self.name),
                self.google_places_id
            )

        if not self.description:
            self.description = place_json.get('review_summary', '')

        self.address = place_json.get('formatted_address', '')
        self.website = place_json.get('website', '')
        self.opening_times = ', '.join(place_json.get('opening_hours', {})
                                                 .get('weekday_text', []))
        self.telephone_number = place_json.get('formatted_phone_number', '')
        location = place_json.get('geometry').get('location')
        self.location_latitude = location.get('lat')
        self.location_longitude = location.get('lng')
        self.google_maps_url = place_json.get('url')
        self.price_level = place_json.get('price_level')

        if commit:
            self.save()

        return self

    def update_images_from_google_api(self):
        self.place_images.all().delete()

        place_photos_json = self.get_place_from_google_api().get('photos', [])

        for place_photo in place_photos_json:
            new_image = PlaceImage()
            new_image.place = self
            new_image.image_width = place_photo.get('width')
            new_image.image_height = place_photo.get('height')
            new_image.google_place_photo_id = place_photo.get(
                'photo_reference')
            new_image.update_image_from_google_api()

class PlaceImage(models.Model):
    place = models.ForeignKey('Place', related_name='place_images',
                              related_query_name='place_image',
                              verbose_name=_('Place'))
    google_place_photo_id = models.CharField(_('Google API Place Photo ID'),
                                             max_length=255,
                                             unique=True)
    image = models.ImageField(upload_to='places', height_field='image_height',
                              width_field='image_width',
                              verbose_name=_('Image'))
    image_height = models.PositiveSmallIntegerField(_('image height'),
                                                    blank=True,
                                                    null=True)
    image_width = models.PositiveSmallIntegerField(_('image width'),
                                                   blank=True,
                                                   null=True)

    class Meta:
        verbose_name = _('place image')
        verbose_name_plural = _('place images')

    def __init__(self, *args, **kwargs):
        super(PlaceImage, self).__init__(*args, **kwargs)
        self.google_service = GooglePlacesService()

    def __str__(self):
        return '{}\'s image'.format(self.place)

    def update_image_from_google_api(self):
        if not self.google_place_photo_id:
            raise Exception("No Google Place Photo ID")

        lf = self.google_service.get_place_photo(self.google_place_photo_id)

        self.image.save(self.google_place_photo_id + '.jpg', files.File(lf))

class PlaceTag(models.Model):
    name = models.SlugField(_('tag'), max_length=10)

    class Meta:
        verbose_name = _('place tag')
        verbose_name_plural = _('place tags')

    def __str__(self):
        return self.name
