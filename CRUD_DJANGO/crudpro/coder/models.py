from django.db import models

# Create your models here.

class CoderModel(models.Model):
         name=models.CharField(max_length=255)
         designation=models.CharField(max_length=122)
         email=models.EmailField(max_length=122)
         yoe=models.IntegerField()


         def __str__(self):
             return self.name
         class Meta:
                ordering=['-yoe']
