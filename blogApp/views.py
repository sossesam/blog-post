from django.shortcuts import render,redirect

from blogApp.models import taskDb
from .forms import taskForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = taskForm(request.POST or None)
        if form.is_valid:
            form.save()
            messages.success(request, 'post added')
            posts = taskDb.objects.all()
            return render(request, 'index.html', {'posts': posts})

    else:
        posts = taskDb.objects.all()
        return render(request, 'index.html', {'posts': posts})


def delete(request, post_id):
    post = taskDb.objects.get(id=post_id)       
    post.delete()
    messages.success(request,'item has been deleted')
    return redirect('home')

def article(request, list_id):
    post_item = taskDb.objects.get(id = list_id)
    return render(request, 'post.html', {'post_item': post_item})


    
    