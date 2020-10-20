from django.db import models


class Measure(models.Model):
    Label = models.CharField(max_length=100, null=True)
    value_measure = models.FloatField(null=True)
    
    def __str__(self):
    	return '{}'.format(self.id)

class Points(models.Model):
    Point  = models.CharField(max_length=100, null=True)
    coment = models.CharField(max_length=1000, null=True)
    imagem = models.FileField(upload_to='documents/', null=True)
    Cell = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '{}'.format(self.id)


class csvfile(models.Model):
	file = models.FileField(upload_to='documents/csv/')
	def __str__(self):
		return '{}'.format(self.file)


#class VariableTypeLib(models.Model):
#	VariableTypeID = models.BigIntegerField(null=True)


#	def __str__(self):
#		return '{}'.format(self.id)


class Sensor(models.Model):
	SensorID = models.BigIntegerField(null=True)

	def __str__(self):
		return '{}'.format(self.id)


class Asset(models.Model):
	AssetID = models.BigIntegerField(null=True)

	def __str__(self):
		return '{}'.format(self.id)


class AssetMonitoredInfoTimeSeries_000001(models.Model):
    value = models.FloatField(null=True)
    datahora =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.value)

class novatabela(models.Model):
    valor = models.FloatField()
    datahora =  models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.valor)


class VariableTypeLib(models.Model):
    IoTDeviceID = models.BigIntegerField(null=True)

    def __str__(self):
    	return '{}'.format(self.id)



