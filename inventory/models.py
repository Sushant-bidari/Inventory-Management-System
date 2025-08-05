from django.db import models

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# 🔽 Supplier model with rating calculation(Weighted Suppiler Rating Algorithm)
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    delivery_time = models.FloatField(help_text="Average delivery time in days")
    defect_rate = models.FloatField(help_text="Defective product rate in %")
    price = models.FloatField(help_text="Average price per unit (Rs.)")
    rating = models.FloatField(null=True, blank=True, help_text="Auto-calculated supplier rating (0–10)")

    def calculate_rating(self):
        # Define weights (adjustable)
        weight_delivery = 0.4
        weight_defect = 0.3
        weight_price = 0.3

        delivery_score = max(0, 1 - (self.delivery_time / 10))
        defect_score = max(0, 1 - (self.defect_rate / 100))
        price_score = max(0, 1 - (self.price / 1000))

        rating = (
            delivery_score * weight_delivery +
            defect_score * weight_defect +
            price_score * weight_price
        )

        return round(rating * 10, 2)  # scale 0–10

    def save(self, *args, **kwargs):
        self.rating = self.calculate_rating()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} (Rating: {self.rating})"
