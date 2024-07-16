from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import (CreateView, DetailView, ListView,
                                  UpdateView, DeleteView)
from .models import Post


class PostListView(ListView):
    """Post listing class-based view
    """
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    """Post detail view
    """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """Post create view
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """Save the post's author before submitting
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Post update view
    """
    model = Post
    fields = ['title', 'content']

    def test_func(self):
        """Check that the post's author is the logged in user
        """
        post = self.get_object()
        return post.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Post delete view
    """
    model = Post
    success_url = "/"

    def test_func(self):
        """Check that the post's author is the logged in user
        """
        post = self.get_object()
        return post.author == self.request.user


def about(request):
    """About route
    """
    return render(request, 'blog/about.html', {'title': 'About'})
