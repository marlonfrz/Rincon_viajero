from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .forms import SearchForm
from .models import TravelPost


def posts_list(request):
    now = timezone.now()

    TravelPost.objects.filter(deadline__lt=now, status=TravelPost.Status.ACTIVE).update(
        status=TravelPost.Status.CANCELLED
    )

    TravelPost.objects.filter(status=TravelPost.Status.CANCELLED).delete()

    search_form = SearchForm(request.GET or None)
    query = request.GET.get('query', '')

    active_status = TravelPost.Status.ACTIVE

    posts = TravelPost.objects.filter(status=active_status)
    if query:
        posts = posts.filter(travel_name__icontains=query)

    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    context = {
        'posts': page_posts,
        'search_form': search_form,
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'post/offer_list.html', context)

    return render(request, 'post/posts_list.html', context)


def post_detail(request, travel_slug):
    post = get_object_or_404(TravelPost, slug=travel_slug)
    return render(request, 'post/post_detail.html', {'post': post})


def cookies_policy(request):
    return render(request, 'warning/cookies_policy.html')


def about_us(request):
    return render(request, 'warning/about_us.html')


def legal_warning(request):
    return render(request, 'warning/legal_warning.html')


def custom_404(request, exception=None):
    return render(request, '404.html', status=404)
