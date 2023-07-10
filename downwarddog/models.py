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


"""Like counting"""


def number_of_likes(self):
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


"""Yoga page - Classes"""


class ClassType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


"""Booking"""


class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    booking_date = models.DateField()
    start_time = models.TimeField()
    class_type = models.ForeignKey(ClassType, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f'Booking by {self.user.get_full_name()} on {self.booking_date} at {self.start_time} for {self.class_type}'

    class Meta:
        ordering = ['booking_date', 'start_time']
