from django.urls import path
from .views import KigaliViewset

urlpatterns = [
    path('kigali/', KigaliViewset.as_view()),
    path('kigali/<int:id>', KigaliViewset.as_view())
]



