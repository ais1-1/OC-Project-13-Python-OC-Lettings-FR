""" Define lettings models """
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Address model.
    Attributes:
    number (int): street number
    street (str): street name
    city (str): city name
    state (str): state abbreviation
    zip_code (int): postal code
    country_iso_code (str): Alpha-3 code as described in the ISO 3166 international standard
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    class Meta:
        """db_table (str): the name of the database table to use for the model
        verbose_name_plural (str): plural form of the model"""

        db_table = "oc_lettings_site_address"
        verbose_name_plural = "addresses"

    def __str__(self):
        """Used in print"""
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """Letting model
    attributes:
    title (str): title of the letting
    address (Addres): Address model instance"""

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        """db_table (str): the name of the database table to use for the model"""

        db_table = "oc_lettings_site_letting"

    def __str__(self):
        """Used in print"""
        return self.title
