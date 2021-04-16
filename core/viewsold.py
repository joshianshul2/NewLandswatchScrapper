from django.db.models import Q, Count
import io
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from pandas.compat import StringIO
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models import Sum,Avg
import bcrypt
from django.utils.decorators import method_decorator
from .models import User,UserManager,PropertyMaster,Property_TypeMaster,TypeMaster,AvgMaster
import requests
import csv
import time
import pdb
import operator
from django.db.models import F
import random
import re
from django.db.models import Q, Count
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd
from core import testdb
from core import propframe,qwerty
from io import StringIO

status_dict = {1: "Active", 2: "Under Contract", 3: "Off Market", 4: "Sold"}
def index(request):
    return render(request, 'index2.html')

def login(request):
    if User.objects.filter(email=request.POST.get('login_email')).exists():
        user = User.objects.filter(email=request.POST.get('login_email'))[0]
        # if (bcrypt.checkpw(request.POST['login_password'].encode('utf-8'), user.password.encode('utf-8'))):
        if (request.POST.get('login_password') == user.password):
            request.session['id'] = user.id
            if request.POST.get('next',None) :
                print("Dipu")
                return  HttpResponseRedirect(request.GET['next'])
            return redirect('/rishu')
    return redirect('/')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    # job(request)

    return render(request, 'test111.html', context)

def set_password(self, pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    self.password_hash = pwhash.decode('utf8') # decode the hash to prevent is encoded twice


@cache_control(no_cache=True, must_revalidate=True)
def logout_view(request):
    # logout(request)
    return render(request,'index2.html')

def index3(request):
    user_list = PropertyMaster.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 200)
   
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages(10))
    return render(request, 'user_list.html', { 'users': users })