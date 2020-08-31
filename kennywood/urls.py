from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from kennywoodapi.models import *
from kennywoodapi.views import register_user, login_user
from kennywoodapi.views import ParkAreas, Attractions, ItineraryItems

# pylint: disable=invalid-name
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'parkareas', ParkAreas, 'parkarea')
router.register(r'attractions', Attractions, 'attraction')
router.register(r'itineraryitems', ItineraryItems, 'itinerary')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user),
    path('login/', login_user),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
