from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import  (TemplateView , ListView , DetailView ,
                                    CreateView, DetailView , UpdateView,
                                    )
from .models import Post, Comment
from .forms import PostForm, CommentForm
#for class based views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.



class AboutView(TemplateView):
    template_name = 'about.html'



class PostListView(ListView):
    model = Post

    def get_queryset(self):
        ## note __ after the field name is a condiotion or expression or it can be a function call
        return Post.objects.filter(published_date_lte = timezone.now()).order_by('-published_date'))


class PostDetailView(DetailView):
    model = Post



#ensure a auth user is the only person who can create post
class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name ='blog/post_detail.html'
    form_class = PostForm
    model = Post



class PostUpdateView(LoginRequiredMixin, UpdateView):
        login_url = '/login/'
        redirect_field_name ='blog/post_detail.html'
        form_class = PostForm
        model = Post


class PostDeleteView(LoginRequiredMixin, DetailView):
    model = Post
    ## the idea behind reverse_lazy function it waits until you successfully deletes the dedicated post
    success_url = reverse_lazy('blog:post_list')



## unpublished list of posts

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('created_date')
