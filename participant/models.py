from django.db import models

# Create your models here.
class participant(models.Model):
    nickname = models.CharField(max_length=32,unique=True)
    reg_date = models.DateTimeField('Date of registration')
    def  __str__(self):
        return self.nickname