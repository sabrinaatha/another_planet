from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return super().__str__()


# Create your models here.
