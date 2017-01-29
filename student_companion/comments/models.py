from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class PlaceComment(models.Model):
    place = models.ForeignKey('places.Place', related_name='place_comments',
                              related_query_name='place_comment',
                              verbose_name=_('place'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='place_comment',
                             verbose_name=_('user'))
    comment = models.TextField(_('comment'))
    created_at = models.DateTimeField(_('created at'), default=timezone.now)

    class Meta:
        verbose_name = _('place comment')
        verbose_name_plural = _('place comments')

    def __str__(self):
        return _('Comment on %s by %s.') % (place, user)
