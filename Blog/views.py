from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'Blog/home_page.html', )

def contact(request):
    return render(request, 'Blog/contact-me.html', )

def footer(request):
    return render(request, 'Blog/footer.html', )

def web(request):
    return render(request, 'Blog/portfolio-web.html', )

def academic(request):
    return render(request, 'Blog/academic.html', )

def research(request):
    return render(request, 'Blog/research.html', )

def about(request):
    return render(request, 'Blog/about-me.html', )
