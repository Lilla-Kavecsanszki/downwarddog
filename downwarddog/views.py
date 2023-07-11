from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, ClassType
from .forms import CommentForm


def home(request):
    """ Homepage """
    return render(request, 'index.html')

def yoga_page(request):
    """ Yoga page """
    return render(request, 'yoga.html')

def yoga_classes(request):
    class_types = [
        {
            'name': 'Vinyasa Flow Yoga',
            'description': 'Vinyasa Flow is a dynamic practice and one of the most popular forms of yoga in the world. In this class, you will flow through a sequence of postures.',
            'available_dates_times': ['2023-09-10 09:00', '2023-09-12 17:30', '2023-09-15 11:00']
        },
        {
            'name': 'Ashtanga Yoga',
            'description': 'Linking breath and movement, students move through a set sequence of asanas that purify, strengthen and give flexibility to the body.',
            'available_dates_times': ['2023-09-11 16:00', '2023-09-13 08:30', '2023-09-16 10:30']
        },
        {
            'name': 'Scaravelli Yoga',
            'description': 'A gentle yet mentally-demanding class that focuses on developing core strength, releasing tension and creating length in the spine.',
            'available_dates_times': ['2023-09-10 14:30', '2023-09-12 11:00', '2023-09-15 15:00']
        },
        {
            'name': 'Iyengar Yoga',
            'description': 'The Iyengar yoga method is internationally respected for its rigorous style and its sophisticated understanding of asana.',
            'available_dates_times': ['2023-09-11 10:00', '2023-09-13 13:30', '2023-09-16 09:00']
        }
    ]

    context = {
        'yoga_classes': class_types
    }
    return render(request, 'yoga.html', context)


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "articles.html"
    paginate_by = 4


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "articles_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "articles_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('articles_detail', args=[slug]))
