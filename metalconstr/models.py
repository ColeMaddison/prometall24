from django.db import models

class Category(models.Model):
	class Meta():
		db_table = "category"

	cat_name = models.CharField(max_length=128, unique=True)
	cat_description = models.TextField()

	def __str__(self):
		return self.cat_name

class Construction(models.Model):
	class Meta():
		db_table = "construction"

	category = models.ForeignKey(Category)
	const_name = models.CharField(max_length=128)
	const_description = models.TextField()
	const_imagename = models.CharField(max_length=128)

	def __str__(self):
		return self.const_name