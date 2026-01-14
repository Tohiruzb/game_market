from django.utils import timezone


from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Category of Game')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
class Article(models.Model):

    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='photos/', null=True, blank=True)
    created_time = models.DateTimeField(
        default=timezone.now
    )
    image_1 = models.ImageField(upload_to='media/carousel/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='media/carousel/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='media/carousel/', null=True, blank=True)
    image_4 = models.ImageField(upload_to='media/carousel/', null=True, blank=True)
    image_5 = models.ImageField(upload_to='media/carousel/', null=True, blank=True)
    updated_time = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=True, null=True)
    views = models.IntegerField(default=0)
    rating = models.FloatField()
    link = models.URLField(max_length=500, blank=True, null=True)
    published_time = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_id': self.pk})

    def get_photo(self):
        if self.image:
            return self.image.url
        else:
            return None


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'





