from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from .models import Author, Book

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class AuthorView:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio

class AuthorList(TemplateView):
    model = Author
    template_name = 'author_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["authors"] = Author.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["authors"] = Author.objects.all()
            context["header"] = "Trending Authors"
        return context

class AuthorCreate(CreateView):
    model = Author
    fields = ['name', 'img', 'bio']
    template_name = "author_create.html"
    def get_success_url(self):
        return reverse('author_detail', kwargs={'pk': self.object.pk})

class AuthorDetail(DetailView):
    model = Author
    template_name = "author_detail.html"

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name', 'img', 'bio']
    template_name = "author_update.html"
    def get_success_url(self):
        return reverse('author_detail', kwargs={'pk': self.object.pk})

class AuthorDelete(DeleteView):
    model = Author
    template_name = "author_delete_confirmation.html"
    success_url = "/authors/"

class BookCreate(View):
    def post(self, request, pk):
        title = request.POST.get("title")
        length = request.POST.get("length")
        cover = request.POST.get("cover")
        author = Author.objects.get(pk=pk)
        Book.objects.create(title=title, length=length, cover=cover, author=author)
        return redirect('author_detail', pk=pk)