from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Import a model we created into View
#Use Querysets to filter models and post the models to the view


# Create your views here.
#We created a function (def) called post_list that takes request and will return the value
# it gets from calling another function render that will render (put together) our template blog/post_list.html.
def post_list(request):
    posts=Post.objects.filter(published_date__lte= timezone.now()).order_by('published_date') #Creating a posts QuerySet
    return render(request, 'blog/post_list.html',{'posts':posts})
