from django.shortcuts import get_object_or_404, render

from .models import TravelPost


def posts_list(request):
    posts = TravelPost.objects.filter(status=TravelPost.Status.ACTIVE)
    return render(request, 'post/posts_list.html', {'posts': posts})


def post_detail(request, travel_slug):
    post = get_object_or_404(TravelPost, slug=travel_slug)
    return render(request, 'post/post_detail.html', {'post': post})
