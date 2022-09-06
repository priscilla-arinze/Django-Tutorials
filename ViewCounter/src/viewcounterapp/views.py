from django.shortcuts import render
from django.http import HttpResponse
from .models import PageViews
from django.db.models import F 


# Create your views here.
def incrementPageView(request):

    # attenpting to update database with update() & F() expression
    count = PageViews.objects.filter(id=1).update(pageViewCount = F('pageViewCount') + 1)

    # attempting to increment count variable
    count += 1


    # testing HTTP response
    return HttpResponse(count)


# def decrementPageView():
#     count = PageViews.objects.all()
