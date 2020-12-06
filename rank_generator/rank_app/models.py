from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.


class Details(models.Model):

    name = models.CharField(max_length=100)
    uuid = models.PositiveIntegerField(blank=False, unique=True)
    topic = models.CharField(max_length=1250)
    score = models.PositiveIntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    rank = models.PositiveIntegerField(default=1)
    
    class Meta:
        db_table = 'details'
        ordering = ['-rank']


    def save(self, *args, **kwargs):
        self.rank = Details.objects.filter(score__gt=self.score).distinct().count()+1
        super(Details, self).save(*args, **kwargs)
        
    