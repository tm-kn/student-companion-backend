from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

MIN_RATING_VALUE = 1
MAX_RATING_VALUE = 5


class PlaceRating(models.Model):
    place = models.ForeignKey('places.Place', related_name='place_ratings',
                              related_query_name='place_rating',
                              verbose_name=_('place'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='place_rating',
                             verbose_name=_('user'))
    rating = models.PositiveSmallIntegerField(
        _('rating'),
        validators=[MinValueValidator(MIN_RATING_VALUE),
                    MaxValueValidator(MAX_RATING_VALUE)]
    )
    rated_at = models.DateTimeField(_('rated at'), default=timezone.now)

    class Meta:
        verbose_name = _('place rating')
        verbose_name_plural = _('place rating')
        unique_together = ('place', 'user')

    def __str__(self):
        return _('Rating on %s by %s.') % (place, user)
