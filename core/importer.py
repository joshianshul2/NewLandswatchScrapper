from django.db.models import Q, Count
import io
from django.shortcuts import render, get_object_or_404
# from rest_framework import generics
# from rest_framework.response import Response
# from .models import Journal, Category, StatusMaster
# from .serializers import JournalSerializer
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from pandas.compat import StringIO
# from django.views.generic import ListView,TemplateView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models import Sum,Avg
import bcrypt
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from .models import User,UserManager,PropertyMaster,Property_TypeMaster,TypeMaster,AvgMaster
# import schedule
# import time
# from apscheduler.schedulers.background import BackgroundScheduler
# Scrapper
import requests
import csv
import time
import pdb
import operator
# import psycopg2test
# import  csv
from django.db.models import F
import random
import re
from django.db.models import Q, Count
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db import connections