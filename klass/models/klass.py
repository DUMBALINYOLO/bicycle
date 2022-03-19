from django.db import models
from basedata.models import SoftDeletionModel



class Klass(SoftDeletionModel):

    GRADE_CHOICES = [
        ('FORM 1', 'FORM 1'),
        ('FORM 2', 'FORM 2'),
        ('FORM 3', 'FORM 3'),
        ('FORM 4', 'FORM 4'),
        ('FORM 5', 'FORM 5'),
        ('FORM 6', 'FORM 6'),
    ]

    grade = models.CharField(
                        max_length=100,
                        choices=GRADE_CHOICES
                    )
    name = models.CharField(
                        max_length=100,
                    )


    def __str__(self):
        return self.name


    @property
    def students(self):
        return self.students.all()


    @property
    def students_number(self):
        return self.students.count()


    @property
    def boys(self):
        return self.students.filter(
                gender='MALE'
        )


    @property
    def girls(self):
        return self.students.filter(
                gender='FEMALE'
        )


    @property
    def girls_number(self):
        return self.students.filter(
                        gender='FEMALE'
                ).count()


    @property
    def boys_number(self):
        return self.students.filter(
                        gender='MALE'
                ).count()
