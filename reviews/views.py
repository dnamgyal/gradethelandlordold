from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Review, Landlord
from .forms import ReviewForm, AddLandlord
import datetime

from django.contrib.auth.decorators import login_required

def index(request):
    landlord_count = Landlord.objects.all().count()
    review_count = Review.objects.all().count()
    context = {'landlord_count':landlord_count, 'review_count':review_count}
    return render(request, 'reviews/index.html', context)

def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def landlord_list(request):
    landlord_list = Landlord.objects.order_by('-name')
    form = AddLandlord()
    context = {'landlord_list':landlord_list, 'form': form}

    return render(request, 'reviews/landlord_list.html', context)


def landlord_detail(request, landlord_id):
    landlord = get_object_or_404(Landlord, pk=landlord_id)
    form = ReviewForm()
    return render(request, 'reviews/landlord_detail.html', {'landlord': landlord, 'form': form})

@login_required
def add_review(request, landlord_id):
    landlord = get_object_or_404(Landlord, pk=landlord_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        communication = form.cleaned_data['communication']
        rent_again = form.cleaned_data['rent_again']
        address = form.cleaned_data['address']
        apt_condition = form.cleaned_data['apt_condition']
        maintenance_eff = form.cleaned_data['maintenance_eff']
        user_name = request.user.username
        review = Review()
        review.communication = communication
        review.address = address
        review.rent_again = rent_again
        review.apt_condition = apt_condition
        review.maintenance_eff = maintenance_eff
        review.landlord = landlord
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:landlord_detail', args=(landlord.id,)))

    return render(request, 'reviews/landlord_detail.html', {'landlord': landlord, 'form': form})

@login_required
def add_landlord(request):
    landlord_list = Landlord.objects.order_by('-name')
    count = Landlord.objects.all().count() + 1
    if request.method == "POST":
        form = AddLandlord(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            l = Landlord()
            l.name = name
            l.save()
            return HttpResponseRedirect(reverse('reviews:landlord_list'))
    landlord = get_object_or_404(Landlord, pk=count)
    return render(request, 'reviews/landlord_detail.html', {'landlord': landlord, 'form': form})

def user_review_list(request, username=None):
    if not username:
        username = request.user.username
    latest_review_list = Review.objects.filter(user_name=username).order_by('-pub_date')
    context = {'latest_review_list':latest_review_list, 'username':username}
    return render(request, 'reviews/user_review_list.html', context)
