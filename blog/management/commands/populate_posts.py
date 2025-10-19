from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post
from random import choice
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the blog with sample posts'

    def handle(self, *args, **kwargs):
        # Create some sample users if none exist
        user = User.objects.filter(username='admin').first()

        titles = [
            "10 Tips for Writing Better Code",
            "My Journey into Django Development",
            "Understanding Python Decorators",
            "How to Stay Productive as a Developer",
            "What's New in Django 4.2",
            "The Importance of Testing Your Code",
            "How I Built My Personal Blog with Django",
            "Why You Should Learn Python in 2025",
            "Common Mistakes New Developers Make",
            "Getting Started with APIs in Django"
        ]

        contents = [
            "In this post, I'll share ten tips that have helped me write cleaner and more efficient code...",
            "When I started learning Django, I had no idea what I was doing. But with time, I began to understand the power of the framework...",
            "Decorators in Python can be tricky at first. Let's break down what they are and how you can use them in your projects...",
            "Staying productive can be hard. Here's what I do to keep my momentum going even when motivation dips...",
            "Django 4.2 brings a lot of improvements. One of my favorites is async views support...",
            "Testing your code is one of the best habits you can develop. Here’s why and how to get started...",
            "I recently built my own blog using Django, and I want to share how you can do the same in a weekend...",
            "Python continues to be one of the most popular languages, and for good reason. Here's why 2025 is a great time to start...",
            "Every developer makes mistakes. These are some common ones I see among beginners and how to avoid them...",
            "APIs are everywhere. In this guide, we’ll look at how to build simple APIs using Django and Django REST Framework..."
        ]

        for i in range(20):
            title = choice(titles)
            content = choice(contents)
            author = user
            date_posted = timezone.now() - timedelta(days=choice(range(1, 365)))

            post = Post.objects.create(
                title=title,
                content=content,
                author=author,
                date_posted=date_posted
            )

            self.stdout.write(self.style.SUCCESS(f'Post "{post.title}" created.'))

        self.stdout.write(self.style.SUCCESS('Successfully populated blog posts.'))
