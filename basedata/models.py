import uuid
from django.db import models


def get_slug():

    return uuid.uuid1()




class SoftDeletionModel(models.Model):
    class Meta:
        abstract = True


    STATUS_CHOICES = [
        ('YES', 'YES'),
        ('NO', 'NO')
    ]

    slug = models.CharField(
        	       max_length=255,
                   primary_key=True,
                   default = get_slug
                  )
    active = models.CharField(
                    max_length=20,
                    default='YES'
                )
    created_at = models.DateTimeField(auto_now_add=True)


    def delete(self):
        self.active = 'NO'
        self.save()

    def hard_delete(self):
        super().delete()
