from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField( max_length=50)

    class Meta:
        verbose_name='Categories'

    def __str__(self):
        return self.name



class Article(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)

    title = models.CharField(max_length=100)
    content= models.TextField(max_length=2000)

    img=models.ImageField(upload_to='article_image/',default='default_image.jpg')

    #add a date field
    pub_date=models.DateField(auto_now=True)



    def __str__(self) -> str:
        return self.title