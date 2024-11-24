from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')  # Название фильма
    year = models.PositiveIntegerField(verbose_name='Year')  # Год выпуска
    description = models.TextField(verbose_name='Description')  # Описание фильма
    director = models.CharField(max_length=255, verbose_name='Director')  # Режиссер
    writers = models.CharField(max_length=255, verbose_name='Writers')  # Сценаристы
    # stars = models.TextField(verbose_name='Stars')  # Актеры
    actors = models.ManyToManyField('Celebrity', related_name='movies', verbose_name='Actors')
    genres = models.CharField(max_length=255, verbose_name='Genres')  # Жанры
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Rating')  # Рейтинг (например, 8.1)
    num_reviews = models.PositiveIntegerField(verbose_name='Number of Reviews')  # Количество отзывов
    poster_image = models.ImageField(upload_to='posters/', blank=True, null=True, verbose_name='Poster Image')  # Изображение постера
    trailer_url = models.URLField(max_length=500, blank=True, null=True, verbose_name='Trailer URL')  # Ссылка на трейлер
    duration = models.PositiveIntegerField(verbose_name='Duration (in minutes)', blank=True, null=True)  # Продолжительность фильма
    release_date = models.DateField(verbose_name='Release Date', blank=True, null=True)  # Дата выхода
    movie_file = models.FileField(upload_to='movies/', blank=True, null=True, verbose_name='Movie File') # Файл фильма


    def __str__(self):
        return f"{self.title} ({self.year})"

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

class Celebrity(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='celebrity_photos/')
    biography = models.TextField()
    fullname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=100)
    height = models.IntegerField(help_text='Height in cm')
    keywords = models.TextField(help_text='Comma-separated keywords')
    social_facebook = models.URLField(blank=True, null=True)
    social_twitter = models.URLField(blank=True, null=True)
    social_google = models.URLField(blank=True, null=True)
    social_linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    @property
    def keywords_list(self):
        # Возвращает список ключевых слов
        return [keyword.strip() for keyword in self.keywords.split(',') if keyword]

    
    class Meta:
        verbose_name = 'Celebrity'
        verbose_name_plural = 'Celebrities'

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    published_date = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-published_date']


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username
