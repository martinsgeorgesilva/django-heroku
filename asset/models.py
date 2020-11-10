from django.db import models


class ProjectVehicle(models.Model):
	label_project = models.CharField(max_length=100, null=True)

	def __str__(self):
		return '{}'.format(self.id)

class SectionVehicle(models.Model):
	label_section = models.CharField(max_length=100, null=True)
	projectlabel = models.CharField(max_length=100, null=True)

	def __str__(self):
		return '{}'.format(self.id)

class Points(models.Model):
    label_point  = models.CharField(max_length=1000, null=True)
    number_point = models.FloatField(null=True)
    coment = models.CharField(max_length=100, null=True)
    imagem = models.FileField(upload_to='documents/', null=True)
    cell = models.CharField(max_length=100, null=True)
    value_measure = models.CharField(max_length=100, null=True)
    sectionlabel = models.CharField(max_length=100, null=True)
    projectlabel = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '{}'.format(self.id)

class csvfile(models.Model):
	file = models.FileField(upload_to='documents/csv/')

	def __str__(self):
		return '{}'.format(self.file)




class Measure(models.Model):
    Label = models.CharField(max_length=100, null=True)
    value_measure = models.FloatField(null=True)
    
    def __str__(self):
    	return '{}'.format(self.id)


