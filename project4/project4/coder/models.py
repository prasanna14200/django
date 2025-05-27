from django.db import models

# Create your models here.

class coder_model(models.Model):
    coder_id = models.IntegerField()
    coder_name = models.CharField(max_length=111)
    coder_email = models.EmailField()

    def __str__(self):
        return f"{self.coder_name} ({self.coder_id})"
  