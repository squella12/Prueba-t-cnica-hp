from django.db import models

# Creamos el modelo pokemon con sus respectivos campos
class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    type1 = models.CharField(max_length=50)
    type2 = models.CharField(max_length=50, blank=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    img_1 = models.CharField(max_length=100)

    # Nombre que se mostrara al guardar un pokemon
    def __str__(self):
        return self.name

    # Definimos el nombre de la tabla en la base de datos
    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemones"
        ordering = ['id']