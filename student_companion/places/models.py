from django.db import models
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey


class PlaceCategory(MPTTModel):
    parent_category = TreeForeignKey('self', null=True, blank=True,
                                     related_name='category_children',
                                     db_index=True,
                                     verbose_name=_('parent category'))
    name = models.CharField(_('name'), max_length=40)
    slug = models.SlugField(_('slug'), max_length=20, unique=True)

    class Meta:
        verbose_name = _('place category')
        verbose_name_plural = _('place categories')

    def __str__(self):
        return self.name


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

    name = models.CharField(_('place'), max_length=30)
    is_visible = models.BooleanField(_('is visible'), default=False)
    google_places_id = models.CharField(_('Google API Place ID'),
                                        max_length=100, blank=True,
                                        unique=True)
    description = models.TextField(_('description'))
    website = models.URLField(_('website'), blank=True)
    address = models.CharField(_('formatted address'), max_length=255)
    telephone_number = models.CharField(_('formatted telephone number'),
                                        max_length=15, blank=True)
    facebook_handle = models.CharField(_('Facebook username'), max_length=255,
                                       blank=True)
    twitter_handle = models.CharField(_('Twitter username'), max_length=255,
                                      blank=True)
    student_discount = models.CharField(_('student discount'), max_length=50)
    opening_times = models.TextField(_('opening hours'), blank=True)
    price_level = models.PositiveSmallIntegerField(_('price level'),
                                                   choices=PRICE_LEVEL_CHOICES)
    tags = models.ManyToManyField('PlaceTag')

    class Meta:
        verbose_name = _('place')
        verbose_name_plural = _('places')

    def __str__(self):
        return self.name


class PlaceTag(models.Model):
    name = models.SlugField(_('tag'), max_length=10)

    class Meta:
        verbose_name = _('place tag')
        verbose_name_plural = _('place tags')

    def __str__(self):
        return self.name
