from django.db import models

# Create your models here.

class CursoManager(models.Manager):
    def validador_basico(self, postData):

        errors = {}

        if len(postData['name']) < 5:
            errors['name_len'] = "El nombre tiene que tener mas de 4 caracteres"

        return errors

class Curso(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CursoManager()

    def __str__(self):
        return f" El nombre es {self.name}"

    def __repr__(self):
        return f" El nombre es {self.name}"



class DescripcionManager(models.Manager):
    def validador_basico(self,postData):
        errors={}

        if len(postData['description']) < 15 :
            errors['description_len'] = " La descripcion debe tener la menos 15 caracteres"

        return errors


class Descripcion(models.Model):
    description = models.CharField(max_length=250)
    curso = models.OneToOneField(Curso, related_name="description", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = DescripcionManager()

    def __str__(self):
        return f" La descripcion es {self.description}"

    def __repr__(self):
        return f" La descripcion es {self.description}"

