from django.shortcuts import render,get_object_or_404 , redirect
from django.urls import reverse_lazy
from django.views.generic import  (TemplateView , ListView , DetailView ,
                                    CreateView, DetailView , UpdateView,
                                    )
from .models import Post, Comment
from .forms import PostForm, CommentForm

from django.utils import timezone
#for class based views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.



class AboutView(TemplateView):
    template_name = 'blog/about.html'



class PostListView(ListView):
    model = Post

    def get_queryset(self):
        ## note __ after the field name is a condiotion or expression or it can be a function call
        return Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')


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




@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################



### comment views
# @login_required
def add_comment_to_post(request , pk):
    post = get_object_or_404(Post, pk =pk )

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', context = {'form':form})



@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)



@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)











    c
