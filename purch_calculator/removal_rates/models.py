from django.db import models



class RemovalForSunflower(models.Model):
    Moisture = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Weed_impurity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Oil_impurity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Oil_content = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    KCHM = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Protein = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return f"Removal #{self.id}"

class RemovalForRapeseed(models.Model):
    Moisture = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Weed_impurity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Oil_impurity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Oil_content = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    KCHM = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Protein = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Removal #{self.id}"



# Create your models here.
