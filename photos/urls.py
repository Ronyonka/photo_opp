from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.all_photos,name='all_photos'),
    url(r'^search/', views.search_results, name='search_results'),
]