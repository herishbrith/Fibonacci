from django.db import models

class Count(models.Model):

	countId = models.AutoField(primary_key=True)
	visitCount = models.IntegerField()
	searchCount = models.IntegerField()

class SiteUser(models.Model):

	ipId = models.AutoField(primary_key=True)
	ipAddress = models.CharField(max_length=40)
	visits = models.IntegerField(default=1)
	searchCount = models.IntegerField(default=0)
