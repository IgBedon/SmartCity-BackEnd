from django.db import models

class Sensor(models.Model):
    
    TIPO_SENSOR_CHOICE = [
        ('Temperatura', 'Temperatura'),
        ('Umidade', 'Umidade'),
        ('Contador', 'Contador'),
        ('Luminosidade', 'Luminosidade')
    ]
    
    tipo = models.CharField(max_length=50, choices=TIPO_SENSOR_CHOICE)
    mac_address = models.CharField(max_length=20, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    localizacao = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    unidade_medida = models.CharField(max_length=20, blank=True, null=True)
    observacao = models.TextField(blank=True)
    status_operacional = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.tipo} - {self.localizacao}"
    
class TemperaturaData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    valor = models.FloatField()
    #timestamp = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f"Temperatura: {self.valor} °C - {self.timestamp}"
    
class UmidadeData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    valor = models.FloatField()
    timestamp = models.DateTimeField()
    
class ContadorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f"Contagem: {self.timestamp}"
    
class LuminosidadeData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    valor = models.FloatField()
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f"Luminosidade: {self.valor} Lux - {self.timestamp}"