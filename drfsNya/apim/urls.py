from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/series', SerieViewSet, 'series')
router.register('api/peliculas', PeliculaViewSet, 'peliculas')
router.register('api/animes', AnimeViewSet, 'animes')

urlpatterns = router.urls