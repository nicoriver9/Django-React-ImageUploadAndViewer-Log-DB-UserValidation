from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validate_image_size(value):
    # Esta función validará el tamaño de la imagen
    if value.size > 10 * 1024 * 1024:  # Aquí estamos limitando el tamaño a 10MB
        raise ValidationError("El tamaño de la imagen no debe ser mayor a 10MB.")


def validate_image_format(value):
    allowed_formats = ["image/png", "image/jpeg"]
    if value.content_type not in allowed_formats:
        raise ValidationError("Solo se permiten imágenes PNG o JPG.")

class Image(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    service = models.CharField(max_length=10)
    image_base64 = models.TextField()  # Campo para almacenar la imagen en formato base64
    # image = models.ImageField(upload_to='images/', validators=[validate_image_size, validate_image_format])


    def __str__(self):
        return self.name