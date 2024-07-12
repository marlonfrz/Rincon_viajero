from django.shortcuts import render

from .models import TravelPost


def posts_list(request):
    posts = TravelPost.objects.filter(status=TravelPost.Status.ACTIVE)
    return render(request, 'post/posts_list.html', {'posts': posts})


def post_detail(request, travel_slug):
    post = TravelPost.objects.get(slug=travel_slug)
    return render(request, 'post/posts_detail.html', {'post': post})
