from django.db import models

# Create your models here.


Status_choices = [
    ('IN PROGRESS', 'in Progress'),
    ('OUT FOR DELIVERY', 'Out for Delivery'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Cancelled'),
]

class items(models.Model):
    Name=models.CharField(max_length=20)
    Quantity=models.IntegerField()
    Price=models.IntegerField()
    Category=models.CharField(max_length=20)
    Supplier=models.CharField(max_length=20)
    Created_at=models.TimeField()
    Updated_at=models.TimeField(null=True)
    choices=models.CharField(choices=Status_choices,default='IN_PROGRESS',max_length=20)

    def __str__(self):
        return self.Name
