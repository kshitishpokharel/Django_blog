from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author' : 'John Doe',
        'title' : 'First Post',
        'content' : 'First post content',
        'date' : '2019-11-27'
    },
    {
        'author': 'John Doe 1',
        'title': 'First Post 1',
        'content': 'First post content 2',
        'date': '2019-11-26'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
