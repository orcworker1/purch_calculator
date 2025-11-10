from django.db import models



class Removal(models.Model):
    Moisture = models.DecimalField(max_digits=10, decimal_places=2)
    Weed_impurity = models.DecimalField(max_digits=10, decimal_places=2)
    Oil_impurity = models.DecimalField(max_digits=10, decimal_places=2)
    Oil_content = models.DecimalField(max_digits=10, decimal_places=2)
    KCHM = models.DecimalField(max_digits=10, decimal_places=2)
    Protein = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Removal #{self.id}"


# Create your models here.
