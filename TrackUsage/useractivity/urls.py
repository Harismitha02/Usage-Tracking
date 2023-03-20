from django.urls import path
from .views import track_activity

urlpatterns = [
    # other urls
    path('track_activity/', track_activity, name='track_activity'),
]
