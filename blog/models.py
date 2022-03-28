from django.db import models

class Blog(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    #新添加：
    image = models.ImageField(upload_to='portfolio/images/')
    date = models.DateField()
    
   
    def __str__(self):
        return self.tittle
