from django.contrib import admin
from .models import Post, Comment, Classes, Timetable, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Classes)
class ClassesAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_filter = ('status', 'updated_on')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'status', 'updated_on')
    search_fields = ['title', 'content']


@admin.register(Timetable)
class TimetableAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('classes', 'available_date')
    search_fields = ['title', 'content']


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'classes', 'number_of_dogs', 'approved')
    list_filter = ('approved',)
    search_fields = ('user__username', 'classes__title', 'approved')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)
