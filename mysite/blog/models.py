from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):  # Here we are define the table name by the class
	title = models.CharField(max_length=140) 	# Here we are define the column name by the variable
	body = models.TextField() 
	date =  models.DateTimeField()

	# Here is a link to the Django Models field documentation
	# https://docs.djangoproject.com/en/1.10/topics/db/models/


	# Now what this does is allows us to actually return data from the database
	def __uni__(self):
	# __str__ if you're using Python 3
	# __uni__ if you're using Python 2
		return self.title
