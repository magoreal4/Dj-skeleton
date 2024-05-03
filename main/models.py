from django.db import models
from .validators import validate_file_extension,validate_file_extension_svg
from django.utils.html import mark_safe
from solo.models import SingletonModel

class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='Site Name')
    site_description = models.TextField(max_length=255, blank=True, null=True)
    site_logo = models.FileField(upload_to='svg/', validators=[validate_file_extension_svg], default="", blank=True)
    

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"

class Alcance(models.Model): # Tabla con nombre Alcance
    title = models.CharField("titulo", default="", max_length=50)
    description = models.TextField("contenido", max_length=250, default="", blank=True)
    svg = models.FileField(upload_to='icon/', validators=[validate_file_extension], default="", blank=True)
    display = models.BooleanField(default=True)
    order = models.IntegerField("order", default=0)
    created_at = models.DateTimeField("Creado", auto_now_add=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Nuestros Servicios"
        ordering = ['order'] 
    
    def __str__(self):
        return self.title
