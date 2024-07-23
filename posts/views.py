from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .forms import SearchForm
from .models import TravelPost


def posts_list(request):
    search_form = SearchForm(request.GET or None)
    query = request.GET.get('query', '')

    if query:
        posts = TravelPost.objects.filter(
            status=TravelPost.Status.ACTIVE, travel_name__icontains=query
        )
    else:
        posts = TravelPost.objects.filter(status=TravelPost.Status.ACTIVE)

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
