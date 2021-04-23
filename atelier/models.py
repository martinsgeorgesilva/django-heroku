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


class Dojo_imersion(models.Model):
	usuario = models.CharField(max_length=100, null=True)
	UET = models.CharField(max_length=100, null=True)
	module = models.CharField(max_length=50, null=True)
	date = models.CharField(max_length=30, null=True)
	time_initial = models.CharField(max_length=30, null=True)
	status = models.CharField(max_length=30, null=True)
	nota = models.FloatField(null=True)
	description = models.CharField(max_length=1000, null=True)
	gabarito1 = models.CharField(max_length=1000, null=True)
	gabarito2 = models.CharField(max_length=1000, null=True)
	gabarito3 = models.CharField(max_length=1000, null=True)
	gabarito4 = models.CharField(max_length=1000, null=True)
	gabarito5 = models.CharField(max_length=1000, null=True)
	gabarito6 = models.CharField(max_length=1000, null=True)
	gabarito7 = models.CharField(max_length=1000, null=True)
	gabarito8 = models.CharField(max_length=1000, null=True)
	gabarito9 = models.CharField(max_length=1000, null=True)
	gabarito0 = models.CharField(max_length=1000, null=True)
	def __str__(self):
		return '{}'.format(self.id)