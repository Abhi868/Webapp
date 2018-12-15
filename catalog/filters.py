

from catalog.models import Movies
import django_filters

class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movies
        fields = ['name'] 