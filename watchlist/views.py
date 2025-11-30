from django.shortcuts import render , redirect , get_object_or_404
#now we import the models class here
from .models import Movie

def movie_list(request):
    search_query=request.GET.get('search')
    
    if search_query:
        movies=Movie.objects.filter(title__icontains=search_query)
    else:
        movies=Movie.objects.all()
    return render(request, 'watchlist/movie_list.html' ,{'movies' : movies} )


def add_movie(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        year=request.POST.get('year')
        genre=request.POST.get('genre')
        
        Movie.objects.create(
            title = title,
            year = year if year else None,
            genre = genre
        )
        
        return redirect('movie_list')
    return render(request,'watchlist/add_movie.html')

def mark_watched(request , movie_id):
    movie=get_object_or_404(Movie , id=movie_id)
    movie.watched=True
    movie.save()
    return redirect('movie_list')

def rate_movie(request , movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie , id=movie_id)
        rating=request.POST.get('rating')
        movie.rating=rating
        movie.save()
        return redirect('movie_list')
    

#now for delete movie

def delete_movie(request,movie_id):
    movie=get_object_or_404(Movie , id=movie_id)
    movie.delete()
    return redirect('movie_list')


