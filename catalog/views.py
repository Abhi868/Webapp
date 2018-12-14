

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


#For users to browse through list of movies
class movies(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly)
    renderer_classes = (JSONRenderer,)
    def get(self,request,fomart=None):
        queryset=Movies.objects.all()
        movie=MovieSerializer(queryset,many=True)
        context={'movie_list':movie.data}
        return Response(context)


# List of all  movies
class MovieList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly)
    queryset=Movies.objects.all()
    serializer_class=MovieSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'catalog/movie_list.html'


    def list(self,request):
        queryset=self.get_queryset()
        serializer=MovieSerializer(queryset ,many=True)
        context={"data":serializer.data}
        return render(request,"catalog/movie_list.html" ,context)
        
    

# Detailed view of a movie
class CatalogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movies.objects.all()
    serializer_class=MovieSerializer


class MoviesListCreateView(generics.ListCreateAPIView):
    queryset=Movies.objects.all()
    serializer_class=MovieSerializer

    def perform_create(self, serializer):
        genre_type = serializer.validated_data.pop('genre_type')
        genre_list = [Genre.objects.get(genre_id=id) for id in list(genre_type)]
        movie = serializer.save()
        movie.genre.add(*genre_list)
        movie.save()

    