from django.db import models

class Imersion(models.Model):
	cami = models.CharField(max_length=100, null=True)
	pfi = models.CharField(max_length=100, null=True)
	metier = models.CharField(max_length=100, null=True)
	gains_time = models.FloatField(null=True)
	gains_money = models.FloatField(null=True)
	duration = models.FloatField(null=True)
	title = models.CharField(max_length=100, null=True)
	description = models.CharField(max_length=500, null=True)
	date = models.CharField(max_length=30, null=True)
	time_initial = models.CharField(max_length=30, null=True)
	status = models.CharField(max_length=30, null=True)
	def __str__(self):
		return '{}'.format(self.id)