from django.shortcuts import render, redirect

# Create your views here.
def root(request):
    return render(request, "root.html")

def newBlog(request):
    return render(request, "newBlog.html")

def createBlog(request):
    return redirect("/")

def showBlog(request, blog_id):
    context = {
            'number' : blog_id
    }
    return render(request, "showBlog.html", context)

def editBlog(request, blog_id):
    context = {
            'number' : blog_id
    }
    return render(request, "editBlog.html", context)

def deleteBlog(request, blog_id):
    return redirect("/")
