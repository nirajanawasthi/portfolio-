from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, BlogPost
from .forms import ContactForm


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.filter(featured=True)[:6]
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent! I'll get back to you soon.")
            return redirect("core:home")

    return render(
        request,
        "core/index.html",
        {
            "profile": profile,
            "skills": skills,
            "projects": projects,
            "form": form,
        },
    )


def project_list(request):
    projects = Project.objects.all()
    return render(request, "core/project_list.html", {"projects": projects})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "core/project_detail.html", {"project": project})


def blog_list(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, "core/blog_list.html", {"posts": posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, "core/blog_detail.html", {"post": post})
