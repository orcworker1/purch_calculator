from symtable import Class

from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
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


class RawMaterialBatch(models.Model):
    CULTURE_CHOICES = [ # Выбор культуры
        ('raps', 'Рапс'),
        ('sunflower', 'Подсолнечник')]

    PURCHASE_TYPE_CHOICES = [
        ('DirectSupply', 'Прямая поставка'),
        ('ElevatorSupply', 'Поставка на элеватор'),
        ('InventoryF13', 'Перепись  Ф - 13'),
    ]
    FACTORY_CHOICES = [
        ('AMPZ', 'АМПЗ'),
        ('DMEZ', 'ЭМЭЗ'),
        ('EMEZ', 'ДМЭЗ'),
        ('VHEMEZ', 'ВХМЭЗ'),
        ('BKMEZ', 'БКМЭЗ'),
        ('BLMEZ', 'БЛМЭЗ'),
        ('OMEZ', 'ОМЭЗ'),
    ]
    PARTNER_TYPE_CHOICES = [
        ('Trader', 'Трейдер'),
        ('Farm', 'СХТП'),
        ('Agroholding', 'Агрохолдинг'),
        ]
    CONTRACT_TYPE_CHOICES = [
        ('FZV', 'ФЗВ'),
        ('ZCHT', 'ЗЧТ'),
        ('ZCHC', 'ЗЧЦ'),
    ]
    TRANSPORT_CHOICES = [
        ('Auto', 'Авто'),
        ('Railway', 'ЖД'),
    ]

    AGREEMENT_CHOICES = [
        ('Prepayment', 'Предоплата'),
        ('Postpayment', 'Постоплата'),
    ]

    purchase_price = models.DecimalField( # Закупочная цена
        _("Закупочная ценаб руб/кг"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )
    weight_actual = models.DecimalField( #Вес
        _("Вес партии, тонн"),
        max_digits=10, decimal_places=2,default=0,
        validators=[MinValueValidator(0, message=_("Вес не может быть отрицательным."))]
    )
    moisture_actual = models.DecimalField( # Влажность
        _("Влажность факт, %"),
        max_digits=5, decimal_places=2,default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )
    weed_impurity_actual = models.DecimalField( # Сорность
        _("Сорность факт, %"),
        max_digits=5, decimal_places=2,default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    oil_impurity_actual = models.DecimalField( # Масличная примесь
        _("Масличная примесь факт, %"),
        max_digits=5, decimal_places=2,default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    oil_content_actual = models.DecimalField( # Масляничность
        _("Масличность факт, %"),
        max_digits=5, decimal_places=2,default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    KCHM_actual = models.DecimalField( # КМЧ
        _("КЧМ факт, %"),
        max_digits=5, decimal_places=2,default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )

    protein_actual = models.DecimalField( # Протеин
        _("Протеин факт, %"),
        max_digits=5, decimal_places=2,default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))]
    )
    culture = models.CharField( # культура( Подсолнечник или Рапс)
        max_length=20,
        choices=CULTURE_CHOICES,
        default='Рапс',
    )
    receipt_start_date = models.DateField( # Начало приемки сырья
        _('Начало приемки сырья'),
        null=True,
        blank=True
    ) #
    receipt_end_date = models.DateField( # Окончание приемки сырья
        _('Окончание приемки сырья'),
        null = True,
        blank = True
    )

    purchase_type = models.CharField( # вид закупки (выбор из списка)
        max_length=30,
        choices=PURCHASE_TYPE_CHOICES,
        default='Прямая поставка',
    )

    target_factory = models.CharField( # Завод (выбор из списка)
        max_length=30,
        choices=FACTORY_CHOICES,
        default='AMPZ',
    )


    partner_type = models.CharField(  # Партнер (выбор из списка)
        max_length=30,
        choices=PARTNER_TYPE_CHOICES,
        default='Trader',
    )
    contract_type = models.CharField(  # Контракт (выбор из списка)
        max_length=30,
        choices=CONTRACT_TYPE_CHOICES,
        default='FZV',
    )

    transport_type =  models.CharField(  # Транспорт (выбор из списка)
        max_length=30,
        choices=TRANSPORT_CHOICES,
        default='Auto',
    )

    agreement_type = models.CharField(  # Соглашение (выбор из списка)
        max_length=30,
        choices=AGREEMENT_CHOICES,
        default='Prepayment',
    )
    delay_days = models.IntegerField(
        _('Отсрочка'),  #Отсрочка
        validators=[MaxValueValidator(30, message='Значение не может быть больше 30 дней')],
        default=0,

    )
    def __str__(self):
        return f"Removal #{self.id}"


class Tariffs(models.Model):
    distance = models.DecimalField( #Расстояние, км
        _("Расстояние, КМ "),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))])


    tariff =  models.DecimalField( #Тариф
        _("Тариф, р/тн/км"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))])

    storage_days = models.IntegerField( # Срок хранения
        _('Срок хранения, дней'),
        validators=[MinValueValidator(0, message='начение не может быть отрицательным')],
        default=0,
    )
    acceptance_cost = models.DecimalField( # Стоимость приемки
        _("Стоимость приемки, р/тн"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))])

    storage_cost = models.DecimalField( # Стоимость хранения
        _("Стоимость хранения, р/тн/сут"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))])

    shipping_cost = models.DecimalField( # Стоимость отгрузки
        _("Стоимость отгрузки, р/тн"),
        max_digits=10, decimal_places=2, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))])

    natural_loss_pct = models.DecimalField( # Естественная убыль
        _("Естественная убыль, %"),
        max_digits=10, decimal_places=4, default=0,
        validators=[MinValueValidator(0, message=_("Значение не может быть отрицательным."))])



"""Расстояние, км  - число 2 знака после запятой, не может быть отрицательным
   Тариф, р/тн/км – число 2 знака после запятой, не может быть отрицательным
	Срок хранения, дней – целое число, не может быть отрицательным
	Стоимость приемки, р/тн – число 2 знака после запятой, не может быть отрицательным
	Стоимость хранения, р/тн/сут – число 2 знака после запятой, не может быть отрицательным
	Стоимость отгрузки, р/тн – число 2 знака после запятой, не может быть отрицательным
	Естественная убыль, % - десятичное число, 4 знака после запятой 
"""

"""Необходимо добавить поля в таблицу «Общая информация» :

Вид закупки – из выпадающего списка (Прямая поставка, Поставка на элеватор, Перепись Ф-13)

Целевой завод  - из выпадающего списка (АМПЗ, ДМЭЗ, ЭМЭЗ, ВХМЭЗ, БКМЭЗ, БЛМЭЗ, ОМЭЗ)

Тип партнера - из выпадающего списка (Трейдер, СХТП, Агрохолдинг)

Тип контракта -  из выпадающего списка (ФЗВ, ЗЧТ, ЗЧЦ)
Тип ТС - из выпадающего списка (Авто, ЖД)

Соглашение - из выпадающего списка (Предоплата, Постоплата)

Отсрочка – число (не больше 30 дней)"""


# Create your models here.
