from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views import View
from django.core.paginator import Paginator
from .models import Category, Movie, Celebrity, BlogPost, UserProfile
from .forms import UserProfileForm

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def HomeView(request):
    # Получаем первые 5 фильмов
    movies = Movie.objects.all()[:5]

    for movie in movies:
        # Разделяем строку жанров по запятым
        movie.genre_list = [genre.strip() for genre in movie.genres.split(',')]  # Превращаем строку жанров в список


    # Передаем фильмы в контекст для шаблона
    return render(request, 'pages/homev2.html', {'movies': movies})

def nonexistent_page(request):
    return render(request, 'pages/404.html')

def coming_soon(request):
    return render(request, 'pages/comingsoon.html')

# def movie_list(request):
#     movie = Movie.objects.all()
#     return render(request, 'pages/movielist.html')

# def movie_single(request, id):
#     movie = get_object_or_404(Movie, id=id)
#     return render(request, 'moviesingle.html', {'movie': movie})

class MovieListView(ListView):
    model = Movie
    template_name = 'pages/movielist.html'  # Шаблон для списка фильмов
    context_object_name = 'movies'          # Имя контекстной переменной для доступа к фильмам
    # paginate_by = 10                        # Количество фильмов на страницу (опционально)

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'pages/moviesingle.html'  # Шаблон для одного фильма
    context_object_name = 'movie'             # Имя контекстной переменной для доступа к фильму

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Разделяем сценаристов и жанры
        context['writers_list'] = self.object.writers.split(',') if self.object.writers else []
        context['genres_list'] = self.object.genres.split(',') if self.object.genres else []
        
        return context
    
class CelebrityListView(ListView):
    model = Celebrity
    template_name = 'pages/celebritylist.html'  # Путь к шаблону для списка знаменитостей
    context_object_name = 'celebrities'   # Имя переменной в шаблоне для списка объектов

class CelebritySingleView(DetailView):
    model = Celebrity
    template_name = 'pages/celebritysingle.html'  # Путь к шаблону для детальной страницы знаменитости
    context_object_name = 'celebrity'       # Имя переменной в шаблоне для объекта знаменитости
    pk_url_kwarg = 'id'                     # Указывает, что в URL используется параметр 'id' как первичный ключ



def BlogDetailView(request):
    return render(request, 'pages/blogdetail.html')

def blog_grid(request):
    posts = BlogPost.objects.all()  # Получаем все посты для отображения
    return render(request, 'pages/bloggrid.html', {'posts': posts})


def search(request):
    query = request.GET.get('q')
    results = BlogPost.objects.filter(title__icontains=query)
    return render(request, 'bloggrid.html', {'posts': results, 'query': query})


@login_required
def user_profile(request):
    user = request.user

    # Если у вас есть модель профиля, загружаем или создаем объект профиля
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=user)
        profile.save()

    # Проверка POST-запроса для обновления данных профиля
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=profile)

    # Передача данных в шаблон
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'pages/userprofile.html', context)

def user_favorite_grid(request):
    # Здесь можно получить избранные фильмы пользователя из базы данных
    # и передать их в контекст шаблона.
    
    # Пример: избранные фильмы пользователя
    favorite_movies = [
        # Здесь может быть queryset с фильмами, которые пользователь добавил в избранное
        # Например: UserFavorite.objects.filter(user=request.user)
    ]
    
    return render(request, 'pages/userfavoritegrid.html', {'favorite_movies': favorite_movies})




