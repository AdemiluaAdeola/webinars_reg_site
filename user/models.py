from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from datetime import date

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(verbose_name='Date of Birth')
    phone = models.CharField(
        max_length=15,
        verbose_name='Phone Number',
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]
    )
    instagram = models.URLField(blank=True, null=True, default="https://instagram.com")
    facebook = models.URLField(blank=True, null=True, default="https://facebook.com")
    twitter = models.URLField(blank=True, null=True, default="https://twitter.com")
    linkedin = models.URLField(blank=True, null=True, default="https://linkedin.com")

    def __str__(self):
        return f"{self.user.username} - Profile"

    @property
    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
