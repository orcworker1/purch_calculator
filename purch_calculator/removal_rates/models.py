from django.db import models



class RemovalForSunflower(models.Model):
    moisture_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    moisture_removal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weed_impurity_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weed_impurity_removal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    oil_impurity_removal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    oil_impurity_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    oil_content_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    oil_content_removal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    KCHM_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    KCHM_removal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    protein_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    protein_removal = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def __str__(self):
        return f"Removal #{self.id}"

class RemovalForRapeseed(models.Model):
    moisture_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    moisture_removal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weed_impurity_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weed_impurity_removal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    oil_impurity_removal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    oil_impurity_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    oil_content_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    oil_content_removal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    KCHM_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    KCHM_removal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    protein_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    protein_removal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Removal #{self.id}"



# Create your models here.
