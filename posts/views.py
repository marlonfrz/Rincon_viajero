from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .forms import SearchForm
from .models import TravelPost


def posts_list(request, category=None):
    active_status = TravelPost.Status.ACTIVE

    with transaction.atomic():
        TravelPost.objects.filter(deadline__lt=timezone.now(), status=active_status).update(
            status=TravelPost.Status.CANCELLED
        )
        TravelPost.objects.filter(status=TravelPost.Status.CANCELLED).delete()

    search_form = SearchForm(request.GET or None)
    query = request.GET.get('query', '')

    posts = TravelPost.objects.filter(status=active_status)
    no_results = False

    if query:
        posts = posts.filter(travel_name__icontains=query)
        if not posts.exists():
            posts = TravelPost.objects.filter(status=active_status)
            no_results = True

    if category:
        category_slug = TravelPost.get_category_from_slug(category)
        posts = posts.filter(category=category_slug)
        if not posts.exists():
            return render(request, 'post/no_posts_apologies.html', {'active_category': category})

    if not posts.exists():
        return render(request, 'post/no_posts_apologies.html')

    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)

    context = {
        'posts': page_posts,
        'search_form': search_form,
        'active_category': category,
        'no_results': no_results,
    }

    return render(request, 'post/posts_list.html', context)


def post_detail(request, category, post_slug):
    category_choice = TravelPost.get_category_from_slug(category)
    post = get_object_or_404(TravelPost, slug=post_slug, category=category_choice)

    search_form = SearchForm(request.GET or None)
    return render(request, 'post/post_detail.html', {'post': post, 'search_form': search_form})


def cookies_policy(request):
    return render(request, 'warning/cookies_policy.html')


def about_us(request):
    return render(request, 'warning/about_us.html')


def legal_warning(request):
    return render(request, 'warning/legal_warning.html')


def custom_404(request, exception=None):
    return render(request, '404.html', status=404)


def custom_500(request, exception=None):
    return render(request, '500.html', status=500)


def test(request):
    return render(request, 'test.html')


def test2(request):
    return render(request, 'test2.html')
