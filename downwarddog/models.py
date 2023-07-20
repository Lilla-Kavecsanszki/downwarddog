from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


"""Articles"""

STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='post_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """Like counting"""
        return self.likes.count()


"""Comments"""


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


"""Classes"""

STATUS = ((0, 'Draft'), (1, 'Published'))


class Classes(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    duration_minutes = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["status"]
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.title


class Timetable(models.Model):
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE,
                                related_name='approved_classes')
    available_date = models.DateTimeField()

    class Meta:
        ordering = ["available_date"]
        constraints = [
            models.UniqueConstraint(fields=['classes', 'available_date'],
                                    name='unique_class'),
        ]

    def __str__(self):
        return f'Yoga class {self.classes} is scheduled for {self.available_date}'


"""Booking"""


class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,
                             related_name="user_booking")
    classes = models.ForeignKey(Timetable, on_delete=models.CASCADE,
                                related_name='class_booking',)
    approved = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['classes', 'user'],
                                    name='unique_booking'),
        ]

    def __str__(self):
        return f'{self.classes} is booked by {self.user}'
