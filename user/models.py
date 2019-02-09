from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	hostel_number = models.IntegerField(default = 1)
	hostel_name   = models.CharField(max_length = 30, default = "Old Hostel")
	phone_number = models.CharField(max_length = 30, default = '0')
	first_time = models.BooleanField(default = True)
	###
	teaching_assistant='TA'
	student='ST'
	professor='PR'

	EMPLOYMENT_CHOICES = (
        (teaching_assistant, 'Teaching Assistant'),
        (student, 'Student'),
        (professor, 'Professor'),
    )
	####
	employment = models.CharField(max_length = 2, choices = EMPLOYMENT_CHOICES, default= student)

	def __str__(self):
		return self.user.username + "'s Profile"

class Achievements(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	total_quantity = 0
	total_money = 0