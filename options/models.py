from django.db import models

class list(models.Model):
  book = models.CharField(max_length=255)
  writer = models.CharField(max_length=255)




class LM(models.Model):
  book = models.CharField(max_length=255)
  writer = models.CharField(max_length=255)







class WH(models.Model):
  book = models.CharField(max_length=255)
  writer = models.CharField(max_length=255)





  def __str__(self):
    return f"{self.book} {self.writer}"