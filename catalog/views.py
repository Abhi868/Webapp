

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from catalog.models import Movies, Genre
from catalog.serializers import MovieSerializer,  GenreSerializer
from rest_framework import generics
from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .filters import MovieFilter
from rest_framework import request



# List of all  movies. Admin can update or destroy a specific object and users 



class MovieList(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticatedOrReadOnly)
    queryset=Movies.objects.all()
    serializer_class=MovieSerializer
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'catalog/movie_list.html'


#For admin to create a movie object else will only have read access

class MoviesListCreateView(generics.ListCreateAPIView):

    # permission_classes = (IsAuthenticatedOrReadOnly)
    queryset=Movies.objects.all()
    serializer_class=MovieSerializer

    def perform_create(self, serializer):
        genre_type = serializer.validated_data.pop('genre_type')
        genre_list = [Genre.objects.get(genre_id=id) for id in list(genre_type)]
        movie = serializer.save()
        movie.genre.add(*genre_list)
        movie.save()

def HomeView(request):
    return render(request,"catalog/base.html")
# class BaseView(request):
#     # if request.method=="GET":
#     #     queryset=Movies.objects.all()   
#     #     query=request.query_params.get('q')
#     #     if query:
#     #         t=queryset.objects.all(name=query)
#     #         print(t)

class MovieDetailCustom(generics.RetrieveAPIView):
   
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "name"

