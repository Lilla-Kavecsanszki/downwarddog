from .models import Classes, Timetable, Booking
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post, Classes, Timetable, Booking
from .forms import CommentForm
from django.db import IntegrityError


def home(request):
    """ Homepage """
    return render(request, 'index.html')


def yoga_page(request):
    """ Yoga page """
    return render(request, 'yoga.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "articles.html"
    paginate_by = 4


class YogaList(generic.ListView):
    model = Classes
    queryset = Classes.objects.filter(status=1).order_by('status')
    template_name = 'yoga.html'
    context_object_name = 'classes_list'
    paginate_by = 4


class YogaDetail(View):
    def get(self, request, slug, *args, **kwargs):
        class_instance = get_object_or_404(Classes, slug=slug, status=1)
        timetables = Timetable.objects.filter(
            classes=class_instance).order_by('available_date')

        return render(request, 'yoga_detail.html', {
            'class_instance': class_instance,
            'timetables': timetables
        })


class BookNow(View):
    def get(self, request, timetable_id):
        timetable = get_object_or_404(Timetable, id=timetable_id)
        context = {
            'timetables': timetable
        }

        return render(request, 'book_now.html', context)

    def post(self, request, timetable_id):
        timetable = get_object_or_404(Timetable, id=timetable_id)
        try:
            # Check if the user is authenticated
            if request.user.is_authenticated:
                # Create a new booking/enquiry, set the default number of dogs to 1
                num_dogs = int(request.POST.get('num_dogs', 1))
                booking = Booking.objects.create(
                    user=request.user, classes=timetable, approved=False, number_of_dogs=num_dogs)
                # Redirect to the 'my_bookings' page, otherwise to the login page
                return render(request, 'my_bookings.html', {
                    'pending': True
                })
            else:
                return redirect('account_login')
        except IntegrityError:
            return render(request, 'my_bookings.html', {
                'already_booked': True,
            })


class MyBookings(View):
    def get(self, request):
        """ My Bookings page """
        approved_bookings = Booking.objects.filter(
            user=request.user, approved=True)
        if approved_bookings:
            return render(request, 'my_bookings.html', {
                'approved_bookings': approved_bookings,
                'approved': True,
            })
        else:
            return render(request, 'my_bookings.html', {
                'approved': False,
            })

    def post(self, request, booking_id):
        """ Delete the booking """
        booking = get_object_or_404(
            Booking, id=booking_id, user=request.user, approved=True)
        booking.delete()
        return redirect('my_bookings')


class UpdateBooking(View):
    def post(self, request, booking_id):
        """ Update the number of dogs """
        booking = get_object_or_404(
            Booking, id=booking_id, user=request.user, approved=True)
        num_dogs = int(request.POST.get('num_dogs', 1))
        booking.number_of_dogs = num_dogs
        booking.save()
        return redirect('my_bookings')


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
