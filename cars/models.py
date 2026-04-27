from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Marca")
    model = models.CharField(max_length=100, verbose_name="Modelo")
    year = models.IntegerField(verbose_name="Ano")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    description = models.TextField(verbose_name="Descrição")
    photo = models.ImageField(upload_to='cars/', verbose_name="Foto")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"
        ordering = ['-created_at']
