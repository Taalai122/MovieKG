from django.contrib import admin
from .models import Movie, Celebrity, BlogPost, Category, UserProfile

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'rating')
    search_fields = ('title', 'year')
    list_filter = ('year', 'genres')
    filter_horizontal = ('actors',)  # Удобный виджет для выбора актёров
    # Добавление полей в админке, если нужно
    fields =   ('title', 'year', 'description', 'director', 'writers', 'genres', 'rating', 
                'num_reviews', 'poster_image', 'trailer_url', 'duration', 'release_date', 
                'movie_file', 'actors')



@admin.register(Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    list_display = ('name', 'fullname', 'country', 'date_of_birth', 'height')
    search_fields = ('name', 'fullname', 'country')
    list_filter = ('country', 'date_of_birth')
    ordering = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'photo', 'biography')
        }),
        ('Personal Info', {
            'fields': ('fullname', 'date_of_birth', 'country', 'height')
        }),
        ('Social Media', {
            'fields': ('social_facebook', 'social_twitter', 'social_google', 'social_linkedin')
        }),
        ('Additional Info', {
            'fields': ('keywords',)
        }),
    )

# @admin.register(BlogPost)
# class BlogGridAdmin(admin.ModelAdmin):
#     list_display = ('title', 'content', 'created_at', 'image')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'views', 'category')
    search_fields = ('title', 'description')
    list_filter = ('category', 'published_date')
    date_hierarchy = 'published_date'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'country', 'state')
    search_fields = ('user__username', 'first_name', 'last_name', 'country', 'state')
    list_filter = ('country', 'state')