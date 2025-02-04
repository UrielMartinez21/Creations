from django.db import models
from django.utils import timezone

# Create your models here.
class AccessLogValentine(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    device = models.CharField(max_length=100, null=True, blank=True)    # Por ejemplo: Móvil, PC, Tablet
    user_agent = models.TextField(null=True, blank=True)                # Cadena del navegador
    timestamp = models.DateTimeField(auto_now_add=True)                 # Se registra automáticamente la hora

    def __str__(self):
        # Convertir la fecha (en UTC) a la zona horaria local configurada (Ciudad de México)
        local_timestamp = timezone.localtime(self.timestamp)
        formatted_date = local_timestamp.strftime("%d/%m/%Y %H:%M:%S")
        return f"{self.ip_address} - {formatted_date}"