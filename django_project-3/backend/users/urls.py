from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('users/',UserAPIView.as_view()),
    path('users/<int:pk>/',UserAPIView.as_view()),
    path('user/',TokenUserView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/holidays', HolidayListView.as_view(), name='fetch_holidays'),
    path('api/countries/', CountryListView.as_view(), name='fetch_countries')
]
# <str:country>/<int:year>/