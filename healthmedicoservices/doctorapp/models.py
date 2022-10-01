from dataclasses import fields
from stat import ST_UID
from django.db import models

# Create your models here.

class Doctor(models.Model):
    doc_name = models.CharField(max_length=20)
    doc_phon = models.IntegerField()
    doc_add = models.CharField(max_length=100)

    # class Meta:
    #     model = models
    #     fields = ['doc_name','doc_phon','doc_add']

    def __str__(self):
        return self.doc_name

class User(models.Model):
    use_name = models.CharField(max_length=20)
    use_phon = models.IntegerField()
    use_add = models.CharField(max_length=100)

    def __str__(self):
        return self.use_name
