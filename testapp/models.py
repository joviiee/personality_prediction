from django.db import models

class test(models.Model):
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.a}"

class Questions(models.Model):
    question = models.CharField(max_length=250)
    index = models.CharField(max_length=2)
    def __str__(self):
	    return f"{self.question}"