from django.db import models
from basedata.models import SoftDeletionModel


class Bicycle(SoftDeletionModel):
    owner   = models.OneToOneField(
                        "users.Student",
                        null=True,
                        blank=True,
                        on_delete=models.SET_NULL,
                        related_name='bicycle'
                    )
    manufacturer  = models.ForeignKey(
                        "BicycleManufacturer",
                        null=True,
                        blank=True,
                        on_delete=models.SET_NULL,
                        related_name='bicycles'
                    )
    color =  models.CharField(max_length=255)
    serial_number =  models.CharField(max_length=255, unique=True)
    school_tag =  models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.slug



class BicycleManufacturer(SoftDeletionModel):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name
