from django.shortcuts import render
from .models import Post
from django.views import generic
# Create your views here.

class Postlist(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    context_object_name = 'post_list'
    template_name = 'index.html'


class DetailView(generic.DeleteView):
    model = Post
    template_name = 'post_detail.html'
    
