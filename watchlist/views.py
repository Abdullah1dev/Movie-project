from django.shortcuts import render , redirect , get_object_or_404
#now we import the models class here
from .models import Movie


#for movie list
def movie_list(request):
    search_query=request.GET.get('search')
    
    if search_query:
        movies=Movie.objects.filter(title__icontains=search_query)
    else:
        movies=Movie.objects.all()
    return render(request, 'watchlist/movie_list.html' ,{'movies' : movies} )

#for add movie
def add_movie(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        year=request.POST.get('year')
        genre=request.POST.get('genre')
        poster=request.FILES.get('poster')
        
        
        Movie.objects.create(
            title = title,
            year = year if year else None,
            genre = genre,
            poster=poster,
            
        )
        
        return redirect('movie_list')
    return render(request,'watchlist/add_movie.html')

#for mark as watched 
def mark_watched(request , movie_id):
    movie=get_object_or_404(Movie , id=movie_id)
    movie.watched=True
    movie.save()
    return redirect('movie_list')

#for rate movie
def rate_movie(request , movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie , id=movie_id)
        rating=request.POST.get('rating')
        notes=request.POST.get('notes')
        movie.rating=rating
        movie.notes=notes
        movie.save()
        return redirect('movie_list')
    

#now for delete movie

def delete_movie(request,movie_id):
    movie=get_object_or_404(Movie , id=movie_id)
    movie.delete()
    return redirect('movie_list')


