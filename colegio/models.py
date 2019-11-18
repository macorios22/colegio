from django.db import models

# Create your models here.
class Curso(models.Model):
    """Model definition for Curso."""
    nombre= models.CharField(max_length=50)
    class Meta:
        """Meta definition for Integrante."""

        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return u'/colegio/create'

class Pensum(models.Model):
    """Model definition for pensum."""
    nombre= models.CharField(max_length=50)
    seccion= models.TextField(blank=True)
    cursos=models.ManyToManyField(Curso)
    class Meta:
        """Meta definition for curso."""

        verbose_name = 'Pensum'
        verbose_name_plural = 'Pensums'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return u'/colegio/%d' % self.id
