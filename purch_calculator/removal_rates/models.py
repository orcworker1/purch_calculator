from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

class RemovalForSunflower(models.Model):
    moisture_base = models.DecimalField(
        _("Влажность (базовое значение, %)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )
    moisture_removal = models.DecimalField(
        _("Влажность (коэффициент съема)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    weed_impurity_base = models.DecimalField(
        _("Сорность (базовое значение, %)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )
    weed_impurity_removal = models.DecimalField(
        _("Сорность (коэффициент съема)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    oil_impurity_base = models.DecimalField(
        _("Масличная примесь (базовое значение, %)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )
    oil_impurity_removal = models.DecimalField(
        _("Масличная примесь (коэффициент съема)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    oil_content_base = models.DecimalField(
        _("Масличность (базовое значение, %)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )
    oil_content_removal = models.DecimalField(
        _("Масличность (коэффициент съема)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    KCHM_base = models.DecimalField(
        _("КЧМ (базовое значение, %)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )
    KCHM_removal = models.DecimalField(
        _("КЧМ (коэффициент съема)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    protein_base = models.DecimalField(
        _("Протеин (базовое значение, %)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )
    protein_removal = models.DecimalField(
        _("Протеин (коэффициент съема)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    def __str__(self):
        return f"Removal #{self.id}"

class RemovalForRapeseed(models.Model):
    moisture_base = models.DecimalField(
        _("Влажность (базовое значение, %)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )
    moisture_removal = models.DecimalField(
        _("Влажность (коэффициент съема)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    weed_impurity_base = models.DecimalField(
        _("Сорность (базовое значение, %)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )
    weed_impurity_removal = models.DecimalField(
        _("Сорность (коэффициент съема)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    oil_impurity_base = models.DecimalField(
        _("Масличная примесь (базовое значение, %)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )
    oil_impurity_removal = models.DecimalField(
        _("Масличная примесь (коэффициент съема)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    oil_content_base = models.DecimalField(
        _("Масличность (базовое значение, %)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )
    oil_content_removal = models.DecimalField(
        _("Масличность (коэффициент съема)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    KCHM_base = models.DecimalField(
        _("КЧМ (базовое значение, %)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )
    KCHM_removal = models.DecimalField(
        _("КЧМ (коэффициент съема)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    protein_base = models.DecimalField(
        _("Протеин (базовое значение, %)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )
    protein_removal = models.DecimalField(
        _("Протеин (коэффициент съема)"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    def __str__(self):
        return f"Removal #{self.id}"


# Create your models here.
