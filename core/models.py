from django.db import models
from django.db import models
from django.utils.text import slugify


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, help_text="e.g. Django Backend Developer")
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    resume = models.FileField(upload_to="resume/", blank=True, null=True)
    profile_image = models.ImageField(upload_to="profile/", blank=True, null=True)
    hero_background = models.ImageField(upload_to="hero/", blank=True, null=True)
    about_image = models.ImageField(upload_to="about/", blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("backend", "Backend"),
        ("frontend", "Frontend"),
        ("database", "Database"),
        ("tools", "Tools"),
    ]
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.PositiveIntegerField(default=80, help_text="0-100")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category", "order"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text="Comma-separated")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    thumbnail = models.ImageField(upload_to="projects/", blank=True, null=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(",")]

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=300, blank=True)
    cover_image = models.ImageField(upload_to="blog/", blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"



