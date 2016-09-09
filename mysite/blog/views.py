from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'blog/home.html')

def blog(request):
	return render(request, 'blog/blog.html')

def contact(request):
	return render(request, 'blog/contact.html')

def about(request):
	return render(request, 'blog/about.html')
