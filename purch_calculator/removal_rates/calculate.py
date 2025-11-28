from decimal import Decimal

from purch_calculator.removal_rates.models import (RemovalForSunflower,RemovalForRapeseed,
                    RawMaterialBatch, Tariffs)
from datetime import datetime, timedelta
import holidays

ru_holidays = holidays.Russia()

def add_business_days(start_date, days, holidays_calendar=None):
    if start_date is None:
        return None
    
    if holidays_calendar is None:
        holidays_calendar = {}

    if hasattr(start_date, "date"):
        start_date = start_date.date()

    current = start_date
    if days > 0:
        remaining = days
        while remaining > 0:
            current += timedelta(days=1)
            is_weekday = current.weekday() < 5
            is_holiday = current in holidays_calendar
            if is_weekday and not is_holiday:
                remaining -= 1

    elif days < 0:
        remaining = abs(days)
        while remaining > 0:
            current -= timedelta(days=1)
            is_weekday = current.weekday() < 5
            is_holiday = current in holidays_calendar
            if is_weekday and not is_holiday:
                remaining -= 1

    return current


class PurchCalculator:
    def __init__(self, sunflower: RemovalForSunflower,
                 rapeseed: RemovalForRapeseed,
                 batch:RawMaterialBatch, tariffs:Tariffs ):
        self.sunflower = sunflower
        self.rapeseed = rapeseed
        self.batch = batch
        self.tariffs = tariffs


    def financial_block(self):
        result = {}
        days = self.batch.delay_days

        if self.batch.receipt_start_date is None:
            result['plane'] = None
        else:
            if self.batch.agreement_type == 'Postpayment':
                days_to_use = days
            else:
                days_to_use = -days

            result['plane'] = add_business_days( # Плановая дата оплаты
                self.batch.receipt_start_date,
                days_to_use,
                ru_holidays
            )
        result['purchase_price'] = self.batch.purchase_price # Цена закупки, руб/кг бНДС
        result['purchase_price_NDS'] = float(self.batch.purchase_price) * 1.1  # Цена закупки, руб/кг cНДС
        if self.batch.purchase_type == 'DirectSupply':
            result['value_of_money'] = 0
        else:
            result['value_of_money'] = round(Decimal(result['purchase_price_NDS'])  *
                                         self.batch.key_rate / Decimal('100') *
                                         self.tariffs.storage_days / Decimal('365'),4)
        return result
    def calculate_all(self):
        return {
            'result': self.financial_block()
        }


