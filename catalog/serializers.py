

from rest_framework import serializers
from catalog.models import Movies,Genre




class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields=('genre_type',)



class MovieSerializer(serializers.ModelSerializer):
    genre=GenreSerializer(many=True, read_only=True)
    genre_type=serializers.MultipleChoiceField(choices = [(o.genre_id, o.genre_type) for o in Genre.objects.all()], write_only=True)
    class Meta:
        model=Movies
        fields=('name','imdb_score','director','_99popularity','genre','genre_type',)   
