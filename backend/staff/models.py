from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
	staff_first_name = models.CharField(max_length=250)
	staff_last_name = models.CharField(max_length=250)

	staff_title = models.CharField(max_length=250)

	staff_phone = models.CharField(max_length=250)
	staff_email = models.CharField(max_length=250)

	class Meta:
        #ordering = ['created_on']
		verbose_name = "Staff"
		verbose_name_plural = "Staffs"


	def __str__(self):
		return self.staff_first_name