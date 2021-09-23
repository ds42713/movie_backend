from django.db import models
from django.db.models.base import Model
from django.utils.html import format_html

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name



class Film_company(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Film Company'

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Director'

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Actor'

    def __str__(self):
        return self.name

class MovieImage(models.Model):
    name = models.CharField(max_length=100)
    image_preview = models.ImageField(upload_to='preview')

    def __str__(self):
        return self.name

class Movie(models.Model):
    slug = models.SlugField(max_length=200,unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True,help_text='เรื่องย่อ')
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='upload', null=True , blank=True)
    image_preview = models.ManyToManyField(MovieImage,blank=True)
    actor = models.ManyToManyField(Actor, blank=True,help_text='นักแสดง')
    director = models.ManyToManyField(Director, blank=True,help_text='ผู้กำกับ')
    category = models.ManyToManyField(Category, blank=True)

    film_company = models.ForeignKey(Film_company, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Movie'

    def __str__(self):
        return self.name

    def show_image(self):
        if self.image:
            return format_html('<img src="' + self.image.url + '" height="200px">')
        return ''
    show_image.allow_tags = True

    def get_comment_count(self):
        return self.moviecomment_set.count()


class MovieComment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Movie Comment'

    def __str__(self):
        return self.comment

