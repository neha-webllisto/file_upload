from django.db import models

# Create your models here.
class Save_model(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	file = models.FileField()

	class Meta:
		db_table = 'Save_model'