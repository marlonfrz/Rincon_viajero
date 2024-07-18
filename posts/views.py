from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import TravelPost


def posts_list(request):
    posts = TravelPost.objects.filter(status=TravelPost.Status.ACTIVE)
    paginator = Paginator(posts, 9)

    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'post/offer_list.html', {'posts': page_posts})

    return render(request, 'post/posts_list.html', {'posts': page_posts})


def post_detail(request, travel_slug):
    post = get_object_or_404(TravelPost, slug=travel_slug)
    return render(request, 'post/post_detail.html', {'post': post})
