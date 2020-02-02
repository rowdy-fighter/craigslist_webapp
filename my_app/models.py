from django.db import models
from django.utils import timezone

class Search(models.Model):
    search = models.CharField(max_length=1000)
    #date=models.DateTimeField('date_published')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search)
    
    class Meta:
        verbose_name_plural = 'Searches'













# class volume(models.Model):
#     search = models.CharField(max_length=1000)
#     date=models.DateTimeField('date_published')
#     created = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return '{}'.format(self.search)
    
#     class Meta:
#         verbose_name_plural = 'Volume'

# class Choice(models.Model):
#     question = models.CharField(max_length=200)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
    
#     def __str__(self):
#         return self.choice_text
