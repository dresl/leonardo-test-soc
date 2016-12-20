# -#- coding: utf-8 -#-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Widget


class TestSocWidget(Widget):

    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255)
    number = models.IntegerField(
        verbose_name=_("Number "),
        help_text=_("Please, enter a number"),
        blank=True,
        null=True)

    class Meta:
        abstract = True
        verbose_name = _("Test soc widget")
        verbose_name_plural = _("Test soc widgets")
