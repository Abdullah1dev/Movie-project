from django.urls  import path
from . import views
 
#now create the urls for wathlist app

urlpatterns = [
    path('',views.movie_list,name='movie_list'),
    path('add_movie/',views.add_movie,name='add_movie'),
    path('watched/<int:movie_id>/',views.mark_watched,name='mark_watched'),
    path('rate/<int:movie_id>/',views.rate_movie,name="rate_movie"),
    path('delete/<int:movie_id>/',views.delete_movie,name='delete_movie')
]
