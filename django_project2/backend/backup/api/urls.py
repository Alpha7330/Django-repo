from django.urls import path
from .views import *
urlpatterns = [
    path('showroom/',showroomview.as_view()),
    path('showroom/<int:id>',showroomview.as_view())
]
