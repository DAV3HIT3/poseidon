
from django.core.serializers.python import Serializer

from .models import *

class RegionSerializer(Serializer):
    def end_object( self, obj ):
        self._current['id'] = obj._get_pk_val()
        self.objects.append( self._current )
