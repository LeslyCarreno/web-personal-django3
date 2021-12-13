from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200,verbose_name = "Título")
    description = models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imagen", upload_to = "projects")
    link = models.URLField(null=True, blank=True, verbose_name="URL")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de Edición")

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ["-created"]
    def _str_(self):
        return self.Title