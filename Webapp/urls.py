
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from catalog.views import MovieList
from catalog import views
from catalog.serializers import MovieSerializer
from catalog.models import Movies
# from catalog.views import ListCreateAPIView
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth import views as auth_views

urlpatterns =[

    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(),name="login"),
    path('logout/', auth_views.LogoutView.as_view(),{'template_name': 'catalog/login.html'},name="logout"),

    path('movies/', views.MoviesListCreateView.as_view(), name='movie-list'),
    #Search using movie id
    path('movies/<int:pk>/',views.MoviesListCreateView.as_view(), {'template_name':'catalog/base.html'}),
    
    path('' ,views.HomeView,name="home"),
    #Search using movie name
    url(r'^movies/(?P<name>.+)/$', views.MovieDetailCustom.as_view(), name='movie-detail'),

]
 
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])