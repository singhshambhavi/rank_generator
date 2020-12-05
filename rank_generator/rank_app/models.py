from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.


class Details(models.Model):

    name = models.CharField(max_length=100)
    uuid = models.PositiveIntegerField(blank=False, unique=True)
    topic = models.CharField(max_length=1250)
    score = models.PositiveIntegerField(blank=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
    rank = models.PositiveIntegerField(default=1)
    
    #def get_url(self):
        #return reverse ('display', args=(self.id))
    
    class Meta:
        db_table = 'details'
        ordering = ['-rank']

    def update(self, *args, **kwargs):
        obj = Details.objects.all().order_by('score')
        rank = Details.objects.filter(score__gt=obj.score).count()
        ranks = Details.objects.all().update(rank=rank)
        super().update(**kwargs)

    def save(self, *args, **kwargs):
        self.rank = Details.objects.filter(score__gt=self.score).count()+1
        super(Details, self).save(*args, **kwargs)
        