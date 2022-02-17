from django.urls import path
#from .views import Index
from .views import article_list


urlpatterns = [
    #path('', Index),
    path('articles/', article_list)
]