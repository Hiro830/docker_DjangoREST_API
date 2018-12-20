#from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("Hello world!!")

########
# coding: utf-8

import django_filters
from examplepj import viewsets, filters

from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
