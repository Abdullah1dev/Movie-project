from django.db import models

class Movie(models.Model):
    title=models.CharField(max_length=150)
    year=models.IntegerField(null=True , blank=True)
    genre=models.CharField(max_length=100 , blank=True)
    watched=models.BooleanField(default=False)
    rating=models.IntegerField(null=True , blank=True)
    notes=models.TextField(max_length=300 , blank=True)
    added_date=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['-added_date']
        
      