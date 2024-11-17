from django.urls import path
from . import views

from .views import BlogDetailView, HomeView, CelebrityListView, CelebritySingleView, MovieListView, MovieDetailView


urlpatterns = [
    path('',HomeView, name='HomeView'),

    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_single'),  # pk — это ключ для DetailView

    path('celebrities/', CelebrityListView.as_view(), name='celebrity_list'),
    path('celebrities/<int:id>/', CelebritySingleView.as_view(), name='celebrity_single'),

    path('blog_detail/',BlogDetailView, name='blog_detail'),
    path('blog/', views.blog_grid, name='blog_grid'), 
    # path('', views.BlogPostListView.as_view(), name='blog_grid'),  # Список постов в виде grid
    path('search/', views.search, name='blog_search'),             # Поиск постов (опционально)
    path('profile/', views.user_profile, name='user_profile'),
    path('404-/', views.nonexistent_page, name='404.html'),
    path('userfavoritegrid/', views.user_favorite_grid, name='user_favorite_grid'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),


    # path('login/', views.login_view, name='login'),
    # path('signup/', views.signup_view, name='signup'),
]
