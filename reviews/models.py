from django.db import models
import numpy as np


class Landlord(models.Model):
    name = models.CharField(max_length=200)

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __unicode__(self):
        return self.name


class Review(models.Model):
        RATING_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        )
        YES_NO = (
        ('Yes', 'Yes'),
        ('No', 'No'),)

        landlord = models.ForeignKey(Landlord)
        pub_date = models.DateField('date published')
        user_name = models.CharField(max_length=100)
        comment = models.CharField(max_length=200)
        rating = models.IntegerField(choices=RATING_CHOICES)
        communication = models.IntegerField(choices=RATING_CHOICES, null=True)
        rent_again = models.CharField(choices=YES_NO, max_length=5, null=True)
        address = models.CharField(max_length=200, null = True)
        apt_condition = models.IntegerField(choices=RATING_CHOICES, null=True)
        maintenance_eff = models.IntegerField(choices=RATING_CHOICES, null=True)
