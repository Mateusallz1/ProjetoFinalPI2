from django.db import models
# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=500)
    

class Pokemon(models.Model):
    number = models.CharField(max_length=3)
    name = models.CharField(max_length=128)
    type = models.ForeignKey(Type, related_name='tipos', on_delete=models.CASCADE)
    description = models.CharField(max_length=500)


class Trainer(models.Model):
    name = models.CharField(max_length=128)
    age = models.CharField(max_length=3)
    region = models.CharField(max_length=58)
    pokemon = models.ManyToManyField(Pokemon, related_name='pokemon')

    def total_pokes(self):
        total = Pokemon.objects.filter(trainer=self).count()
        return total


class Researcher(models.Model):
    name = models.CharField(max_length=128)
    trainers = models.ManyToManyField(Trainer, related_name='trainers')


