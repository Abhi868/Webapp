

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from catalog.models import Movies, Genre
from catalog.serializers import MovieSerializer,  GenreSerializer
from rest_framework import generics
# from rest_framework import status,viewsets
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import filters
from rest_framework import request



# List of all  movies. Admin can update or destroy a specific object and users 



class MovieList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset=Movies.objects.all()
    serializer_class=MovieSerializer
    # def get_queryset(self):
    #     movie_name=self.request.query_params('query',None)
    #     queryset=Movies.objects.get(name=movie_name)
    #     return queryset
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'catalog/movie_list.html'

# class MovieByName(generics.ListAPIView):
#     queryset = Movies.objects.all()
#     serializer_class = MovieSerializer
#     def query_set(self):
#         movie_name= self.kwargs['name']
#         return Movies.objects.filter(name=movie_name)


    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('username')

#For admin to create a movie object else will only have read access

class MoviesListCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset=Movies.objects.all()
    serializer_class=MovieSerializer


    def perform_create(self, serializer):
        genre_type = serializer.validated_data.pop('genre_type')
        genre_list = [Genre.objects.get(genre_id=id) for id in list(genre_type)]
        movie = serializer.save()
        movie.genre.add(*genre_list)
        movie.save()

    def get_queryset(self):
        queryset = Movies.objects.all()
        moviename = self.request.query_params.get('q', None)
        if moviename is not None:
            queryset = queryset.filter(name=moviename)
        return queryset
    

def HomeView(request):
    return render(request,"catalog/base.html")


# class MovieList(generics.ListAPIView):
#     serializer_class = MovieSerializer

#     def get_queryset(self):
#         """
#         Optionally restricts the returned purchases to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         queryset = Movies.objects.all()
#         moviename = self.request.query_params.get('q', None)
#         if moviename is not None:
#             queryset = queryset.filter(name=moviename)
#         return queryset


class MovieDetailCustom(generics.RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "name"
    

