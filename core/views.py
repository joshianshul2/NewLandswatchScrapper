from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import Journal, Category, StatusMaster
from .serializers import JournalSerializer
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views.generic import ListView,TemplateView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models import Sum,Avg
import bcrypt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from .models import User,UserManager,PropertyMaster,Property_TypeMaster,TypeMaster,AvgMaster
import schedule
import time
from apscheduler.schedulers.background import BackgroundScheduler
# Scrapper
import requests
import csv
import time
import pdb
import operator
import  csv
from django.db.models import F
import random
import re
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework import generics
from rest_framework.response import Response
from django.urls import reverse
from .serializers import JournalSerializer
from django.contrib.auth.decorators import login_required

status_dict = {1: "Active", 2: "Under Contract", 3: "Off Market", 4: "Sold"}
def index(request):
    return render(request, 'index2.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    # hashed_password = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
    # password= User.objects.create()
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=request.POST['password'], email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/success')



def Alert(request):
    qs = AvgMaster.objects.all()
    # qs = filter2(request)

    # if request.method == 'POST':
    #     view_percentage = request.GET.get('view_percentage')
    #     view_state = request.GET.get('view_state')
    #     print(view_state, view_percentage)
    #     print("Rishu")
    # return render(request,'bootstrap_form.html')
    if request.method == 'GET':
        print("Anjali Dubey")
        view_percentage = request.GET.get('view_percentage')
        view_state = request.GET.get('view_state')
        print(view_state, view_percentage)
        # # qws = PropertyMaster.objects.get(state='view_state')
        # # print(qws)
        # qr = PropertyMaster.objects.values('state','county').annotate(Aj=Sum('price')/Sum('acres')).distinct()
        #     # .annotate(Aj=Sum('price')/Sum('acres')).distinct()
        # # query = PropertyMaster.objects.filter('student__state' = request.user)
        # # print(qr)
        # # # ab = AvgMaste.objects.create()
        # # # print(qr[Aj])
        # for course in qr:
        #     # qw = AvgMaster.objects.create(state=course['state'],NetPrAr=course['Aj'])
        #     print(course["state"],course["county"],course["Aj"])
        # # qw.save()
        # # # a=view_state
        # # for i in qr:
        # #     a.append(i)
        # #     print(i.values())
        # print(a)
        if PropertyMaster.objects.filter(state=request.GET.get('view_state')).exists():
            qw = PropertyMaster.objects.filter(state=request.GET.get('view_state'))[0]
            # if (bcrypt.checkpw(request.POST['login_password'].encode('utf-8'), user.password.encode('utf-8'))):
            if (request.GET.get('view_state') == qw.state):
                # print(qw.state)
                print("Rishu")
                print(view_state)
                qr = PropertyMaster.objects.filter(state=view_state).annotate(
                    Aj=Sum('price') / Sum('acres')).distinct().values()
                ar = list(PropertyMaster.objects.filter(state=view_state).values('state', 'county').distinct())
                print(ar)
                rishu = 1 - float(view_percentage) / 100
                for course in qr:
                    qw = AvgMaster.objects.create(state=course['state'], county=course['county'], NetPrAr=course['Aj'],
                                                  Rate=course['price'] / course['acres'], UserPercentage=rishu,
                                                  FinaleValue=rishu * course['Aj'],
                                                  accountId=course['accountId'], acres=course['acres'],
                                                  adTargetingCountyId=course['adTargetingCountyId'],
                                                  address=course['address'], baths=course['baths'],
                                                  beds=course['beds'], brokerCompany=course['brokerCompany'],
                                                  brokerName=course['brokerName'],
                                                  Url=course['Url'],
                                                  city=course['city'],
                                                  cityID=course['cityID'],
                                                  companyLogoDocumentId=course['companyLogoDocumentId'],
                                                   countyId=course['countyId'],
                                                  description=course['description'], hasHouse=course['hasHouse'],
                                                  hasVideo=course['hasVideo'],
                                                  hasVirtualTour=course['hasVirtualTour'],
                                                  imageCount=course['imageCount'], latitude=course['latitude'],
                                                  longitude=course['longitude'],
                                                  imageAltTextDisplay=course['imageAltTextDisplay'],
                                                  isHeadlineAd=course['isHeadlineAd'], types=''.join(course['types']),
                                                  lwPropertyId=course['lwPropertyId'], isALC=course['isALC'],
                                                     price=course['price'],
                                                  status=course["status"],
                                                   zip=course['zip']
                                                  )
                    print(course["state"], course["county"], course["Aj"], course["Rate"])
                    akp = AvgMaster.objects.filter(Rate__gte=F('FinaleValue'),UserPercentage__lte=abs(rishu)).values()

                # akp = AvgMaster.objects.filter(Rate__gte=F('FinaleValue')).values()
                print(akp)
                print("Zakir Khan")
                qs = filter2(request)
                for i in akp:
                    print("ANshul",i["state"], i["county"], i["Rate"], i["FinaleValue"])
                # qw.save()
                # # a=view_state
                # for i in qr:
                #     a.append(i)
                #     print(i.values())
                # print(a)

            else:
                print("Anshul")
    anji = AvgMaster.objects.all()
    akp = filter(request)
    context = {
                 'aj': akp,
        # 'status': StatusMaster.objects.all()
                }
    return render(request, "rishu.html", context)

# class ProtectedView(TemplateView):
#     template_name = '/'
#
#     @method_decorator(login_required(login_url='/show'))
#     def dispatch(self, *args, **kwargs):
#         return super(ProtectedView, self).dispatch(*args, **kwargs)



# class ProtectedView(TemplateView):
#     template_name = 'secret.html'
# @method_decorator(login_required)
# @login_required(login_url='/login')
def show(request):

    a=[]
    qs = PropertyMaster.objects.all()
    qs = filter(request)
    auths = PropertyMaster.objects.order_by('acres')
    ordered = sorted(auths, key=operator.attrgetter('acres'))
    if request.method == 'GET':
        for row in PropertyMaster.objects.all().reverse():
            print("AJ")
            if PropertyMaster.objects.filter(lwPropertyId=row.lwPropertyId).count() > 1:
                row.delete()
        view_percentage = request.GET.get('view_percentage')
        view_state = request.GET.get('view_state')
        print(view_state,view_percentage)
        # # qws = PropertyMaster.objects.get(state='view_state')
        # # print(qws)
        # qr = PropertyMaster.objects.values('state','county').annotate(Aj=Sum('price')/Sum('acres')).distinct()
        #     # .annotate(Aj=Sum('price')/Sum('acres')).distinct()
        # # query = PropertyMaster.objects.filter('student__state' = request.user)
        # # print(qr)
        # # # ab = AvgMaste.objects.create()
        # # # print(qr[Aj])
        # for course in qr:
        #     # qw = AvgMaster.objects.create(state=course['state'],NetPrAr=course['Aj'])
        #     print(course["state"],course["county"],course["Aj"])
        # # qw.save()
        # # # a=view_state
        # # for i in qr:
        # #     a.append(i)
        # #     print(i.values())
        print(a)
        if PropertyMaster.objects.filter(state=request.GET.get('view_state')).exists():
            qw = PropertyMaster.objects.filter(state=request.GET.get('view_state'))[0]
            # if (bcrypt.checkpw(request.POST['login_password'].encode('utf-8'), user.password.encode('utf-8'))):
            if (request.GET.get('view_state') == qw.state):
                # print(qw.state)
                print("Rishu")
                print(view_state)
                qr = PropertyMaster.objects.filter(state=view_state).annotate(Aj=Sum('price') / Sum('acres')).distinct().values()
                ar =list(PropertyMaster.objects.filter(state=view_state).values('state','county',).distinct())
                print(ar)
                rishu = 1- float(view_percentage)/100
                for course in qr:
                    qw = AvgMaster.objects.create(state=course['state'],county=course['county'],NetPrAr=course['Aj'],Rate=course['price'] / course['acres'],UserPercentage=rishu,FinaleValue=rishu*course['Aj'])
                    print(course["state"], course["county"], course["Aj"],course["Rate"])
                akp = AvgMaster.objects.filter(Rate__lt=F('FinaleValue')).values()
                print("Zakir Khan")
                qs = filter(request)
                for i in akp:
                    print(i["state"], i["county"], i["Rate"],i["FinaleValue"])
                # qw.save()
                # # a=view_state
                # for i in qr:
                #     a.append(i)
                #     print(i.values())
                print(a)

            else:
                print("Anshul")
    anji = AvgMaster.objects.all()
    context = {
        'queryset': qs,
        'aj' : anji,
        # 'status': StatusMaster.objects.all()
        }
    return render(request,"bootstrap_form.html",context)


def loader(request):
    for row in PropertyMaster.objects.all().reverse():
        if PropertyMaster.objects.filter(lwPropertyId=row.lwPropertyId).count() > 1:
            row.delete()
    # schedule.every(5).seconds.do(job)
    # schedule.every(15).seconds.do(job2)
    schedule.every(5).seconds.do(job3)
    # return redirect('bootstrap_form.html')
    while True:
        schedule.run_pending()
        time.sleep(1)
    return render(request,"bootstrap_form.html")


def job():
        # a=0
        print("I'm Ronaldo...")
        # zipcode_list = [75009]

        zipcode_list = [75002, 75006, 75007, 75009, 75010, 75013, 75019, 75020, 75021, 75022, 75024, 75028, 75032,
                                75034, 75035, 75038, 75040, 75041, 75043, 75044, 75048, 75050, 75051, 75056, 75057, 75058,
                                75061, 75063, 75065, 75067, 75068, 75069, 75070, 75071, 75074,75076, 75077, 75078, 75080, 75081, 75083, 75087, 75088, 75089, 75090, 75092, 75093, 75097, 75098, 75102, 75103, 75104, 75105, 75109, 75110, 75114, 75115, 75116, 75117, 75119, 75124, 75126, 75135, 75142, 75143, 75144, 75147, 75148, 75154, 75156, 75159, 75160]

        # with open("datafile") as myfile:
        #     head = [next(myfile) for x in range(N)]
        # with open('zip_code_database.csv', 'r') as file:
        #     # head = [next(myfile) for x in range(N)]
        #     reader = csv.reader(file)
        #     for row in range(30):
        #         print(row)
                # zipcode_list = [75002, 75006, 75007, 75009, 75010, 75013, 75019, 75020, 75021, 75022, 75024, 75028, 75032,
                #                 75034, 75035, 75038, 75040, 75041, 75043, 75044, 75048, 75050, 75051, 75056, 75057, 75058,
                #                 75061, 75063, 75065, 75067, 75068, 75069, 75070, 75071, 75074,75076, 75077, 75078, 75080, 75081, 75083, 75087, 75088, 75089, 75090, 75092, 75093, 75097, 75098, 75102, 75103, 75104, 75105, 75109, 75110, 75114, 75115, 75116, 75117, 75119, 75124, 75126, 75135, 75142, 75143, 75144, 75147, 75148, 75154, 75156, 75159, 75160]

        headers = {
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
              "Accept-Encoding": "*",
              "Connection": "keep-alive"
                }
        try:

            for zip in zipcode_list:
                        if len(str(zip)) == 4:
                            zip = "0" + str(zip)
                        n = 0
                        url = "https://www.landwatch.com/api/property/search/1113/zip-" + \
                              str(zip) + "/land/listed-1-day"
                        page = 0
                        # print(url)
                        page = requests.get(url, headers=headers)
                        # time.sleep(random.randrange(1, 2))
                        while (page == 0):
                            page = requests.get(url, headers=headers)
                            time.sleep(random.randrange(1, 5))
                        data = page.json()
                        print(data['searchResults']['locationSeo']['pageHeaderCount'])
                        countListing = data['searchResults']['locationSeo']['pageHeaderCount']
                        countListing = re.findall(r'\d+', countListing)
                        print(countListing)
                        if len(countListing) == 3:
                            page_count = int(int(countListing[2]) / 25 + 2)
                        else:
                            page_count = 2
                        # print(countListing)

                        for i in range(1, page_count):
                            url = "https://www.landwatch.com/api/property/search/1113/zip-" + \
                                  str(zip) + "/land/listed-1-day/page-" + str(i)
                            # print(url)
                            page = 0
                            page = requests.get(url, headers=headers)
                            # time.sleep(random.randrange(1, 2))
                            while (page == 0):
                                page = requests.get(url, headers=headers)
                                time.sleep(random.randrange(1, 5))
                            data = page.json()
                            print("Length of data : ",data)

                            print(data['searchResults']['propertyResults'])
                            # print(lwPropertyId)


                            for item in data['searchResults']['propertyResults']:
                        #         # a=a+1

                                # temp = {
                                #     "accountId" : item['accountId'],
                                #     "acres" : item['acres'],
                                #     "adTargetingCountyId" : item['adTargetingCountyId'],
                                #     "address": item['address'],
                                #     "baths" :item['baths'],
                                #     "beds" : item['beds'],
                                #     "brokerCompany" : item['brokerCompany'],
                                #     "brokerName":item['brokerName'],
                                #     "Url" : "https://www.landwatch.com" + item['canonicalUrl'],
                                #     "city" : item['city'],
                                #     "cityID" : item['cityID'],
                                #     "companyLogoDocumentId" : item['companyLogoDocumentId'],
                                #     "county" : item['county'], "countyId" :item['countyId'],
                                #     "description" : item['description'], "hasHouse" : item['hasHouse'],
                                #     "hasVideo" : item['hasVideo'],
                                #     "hasVirtualTour" : item['hasVirtualTour'],
                                #     "imageCount" : item['imageCount'],
                                #     "imageAltTextDisplay" : item['imageAltTextDisplay'],
                                #     "isHeadlineAd" : item['isHeadlineAd'], "types" : item['types'],
                                #     "lwPropertyId" : item['lwPropertyId'], "isALC" : item['isALC'],
                                #     "latitude" : item['latitude'], "state" : item['state'],
                                #     "longitude" : item['longitude'], "price" : item['price'],
                                #     "Rate" : item['price'] /item['acres'], "status"  : item['status'], "zip" : item['zip']
                                # }

                                prop = PropertyMaster.objects.create(accountId=item['accountId'], acres=item['acres'],
                                                                 adTargetingCountyId=item['adTargetingCountyId'],
                                                                 address=item['address'], baths=item['baths'],
                                                                 beds=item['beds'], brokerCompany=item['brokerCompany'],
                                                                 brokerName=item['brokerName'],
                                                                 Url="https://www.landwatch.com" + item['canonicalUrl'],
                                                                 city=item['city'],
                                                                 cityID=item['cityID'],
                                                                 companyLogoDocumentId=item['companyLogoDocumentId'],
                                                                 county=item['county'], countyId=item['countyId'],
                                                                 description=item['description'], hasHouse=item['hasHouse'],
                                                                 hasVideo=item['hasVideo'],
                                                                 hasVirtualTour=item['hasVirtualTour'],
                                                                 imageCount=item['imageCount'],
                                                                 imageAltTextDisplay=item['imageAltTextDisplay'],
                                                                 isHeadlineAd=item['isHeadlineAd'],types=' '.join(item['types']),
                                                                 lwPropertyId=item['lwPropertyId'], isALC=item['isALC'],
                                                                 latitude=item['latitude'],state=item['state'],
                                                                 longitude=item['longitude'], price=item['price'],status=status_dict[item["status"]],
                                                                Rate=item['price'] / item['acres'], zip=item['zip']
                                                           )

                                        # status_dict[item["status"]]
                                        # prop = PropertyMaster.objects.create(accountId=item['accountId'], acres=item['acres'],
                                        #                                  adTargetingCountyId=item['adTargetingCountyId'],
                                        #                                  address=item['address'], baths=item['baths'],
                                        #                                  beds=item['beds'], brokerCompany=item['brokerCompany'],
                                        #                                  brokerName=item['brokerName'],
                                        #                                  Url="https://www.landwatch.com" + item['canonicalUrl'],
                                        #                                  city=item['city'],
                                        #                                  cityID=item['cityID'],
                                        #                                  companyLogoDocumentId=item['companyLogoDocumentId'],
                                        #                                  county=item['county'], countyId=item['countyId'],
                                        #                                  description=item['description'], hasHouse=item['hasHouse'],
                                        #                                  hasVideo=item['hasVideo'],
                                        #                                  hasVirtualTour=item['hasVirtualTour'],
                                        #                                  imageCount=item['imageCount'],
                                        #                                  imageAltTextDisplay=item['imageAltTextDisplay'],
                                        #                                  isHeadlineAd=item['isHeadlineAd'],types=item['types'],
                                        #                                  lwPropertyId=item['lwPropertyId'], isALC=item['isALC'],
                                        #                                  latitude=item['latitude'],state=item['state'],
                                        #                                  longitude=item['longitude'], price=item['price'],
                                        #                                 Rate=item['price'] / item['acres'],status= item['status'] , zip=item['zip']
                                        #                            )
                                        # print(prop)

                        print(n, " records found in zipcode : ", zip)

        finally:
            print("Completed")
            # loader(request)

            # qs = filter(request)
                # auths = PropertyMaster.objects.order_by('acres')
                # ordered = sorted(auths, key=operator.attrgetter('acres'))
            # context = {
            #     'queryset': qs,
            #         # 'acres': ordered,
            #     }
            # return render(request, "bootstrap_form.html")


def job2():
    # a=0
    print("I'm Ram...")
    zipcode_list = [75090]

    # zipcode_list = [75002, 75006, 75007, 75009, 75010, 75013, 75019, 75020, 75021, 75022, 75024, 75028, 75032,
    #                         75034, 75035, 75038, 75040, 75041, 75043, 75044, 75048, 75050, 75051, 75056, 75057, 75058,
    #                         75061, 75063, 75065, 75067, 75068, 75069, 75070, 75071, 75074,75076, 75077, 75078, 75080, 75081, 75083, 75087, 75088, 75089, 75090, 75092, 75093, 75097, 75098, 75102, 75103, 75104, 75105, 75109, 75110, 75114, 75115, 75116, 75117, 75119, 75124, 75126, 75135, 75142, 75143, 75144, 75147, 75148, 75154, 75156, 75159, 75160]
    #
    # with open("datafile") as myfile:
    #     head = [next(myfile) for x in range(N)]
    # with open('zip_code_database.csv', 'r') as file:
    #     # head = [next(myfile) for x in range(N)]
    #     reader = csv.reader(file)
    #     for row in range(30):
    #         print(row)
    # zipcode_list = [75002, 75006, 75007, 75009, 75010, 75013, 75019, 75020, 75021, 75022, 75024, 75028, 75032,
    #                 75034, 75035, 75038, 75040, 75041, 75043, 75044, 75048, 75050, 75051, 75056, 75057, 75058,
    #                 75061, 75063, 75065, 75067, 75068, 75069, 75070, 75071, 75074,75076, 75077, 75078, 75080, 75081, 75083, 75087, 75088, 75089, 75090, 75092, 75093, 75097, 75098, 75102, 75103, 75104, 75105, 75109, 75110, 75114, 75115, 75116, 75117, 75119, 75124, 75126, 75135, 75142, 75143, 75144, 75147, 75148, 75154, 75156, 75159, 75160]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"
    }
    try:

        for zip in zipcode_list:
            if len(str(zip)) == 4:
                zip = "0" + str(zip)
            n = 0
            url = "https://www.landwatch.com/api/property/search/1113/zip-" + \
                  str(zip) + "/land/listed-1-day"
            page = 0
            # print(url)
            page = requests.get(url, headers=headers)
            # time.sleep(random.randrange(1, 2))
            while (page == 0):
                page = requests.get(url, headers=headers)
                time.sleep(random.randrange(1, 5))
            data = page.json()
            print(data['searchResults']['locationSeo']['pageHeaderCount'])
            countListing = data['searchResults']['locationSeo']['pageHeaderCount']
            countListing = re.findall(r'\d+', countListing)
            print(countListing)
            if len(countListing) == 3:
                page_count = int(int(countListing[2]) / 25 + 2)
            else:
                page_count = 2
            # print(countListing)

            for i in range(1, page_count):
                url = "https://www.landwatch.com/api/property/search/1113/zip-" + \
                      str(zip) + "/land/listed-1-day/page-" + str(i)
                # print(url)
                page = 0
                page = requests.get(url, headers=headers)
                # time.sleep(random.randrange(1, 2))
                while (page == 0):
                    page = requests.get(url, headers=headers)
                    time.sleep(random.randrange(1, 5))
                data = page.json()
                # print("Length of data : ",len(data))

                for item in data['searchResults']['propertyResults']:
                    # a=a+1
                    prop = PropertyMaster.objects.create(accountId=item['accountId'], acres=item['acres'],
                                                         adTargetingCountyId=item['adTargetingCountyId'],
                                                         address=item['address'], baths=item['baths'],
                                                         beds=item['beds'], brokerCompany=item['brokerCompany'],
                                                         brokerName=item['brokerName'],
                                                         Url="https://www.landwatch.com" + item['canonicalUrl'],
                                                         city=item['city'],
                                                         cityID=item['cityID'],types=item['types'],
                                                         companyLogoDocumentId=item['companyLogoDocumentId'],
                                                         county=item['county'], countyId=item['countyId'],
                                                         description=item['description'], hasHouse=item['hasHouse'],
                                                         hasVideo=item['hasVideo'],
                                                         hasVirtualTour=item['hasVirtualTour'],
                                                         imageCount=item['imageCount'],
                                                         imageAltTextDisplay=item['imageAltTextDisplay'],
                                                         isHeadlineAd=item['isHeadlineAd'],
                                                         lwPropertyId=item['lwPropertyId'], isALC=item['isALC'],
                                                         latitude=item['latitude'], state=item['state'],
                                                         longitude=item['longitude'], price=item['price'],
                                                         Rate=item['price'] / item['acres'], status=status_dict[item["status"]],
                                                         zip=item['zip'],

                                                         )

                    ###do something###

                    n = n + 1
                print("n=",n)

                # for item in data['searchResults']['propertyResults']:
                #     if PropertyMaster.objects.filter(lwPropertyId=item['lwPropertyId']).exists():
                #
                #         if PropertyMaster.objects.all().values().filter(lwPropertyId=item[lwPropertyId],
                #                                                         user=request.user):
                #             PropertyMaster.objects.all().values().filter(lwPropertyId=item[lwPropertyId],
                #                                                          user=request.user).update(
                #                 accountId=item['accountId'], acres=item['acres'],
                #                 adTargetingCountyId=item['adTargetingCountyId'],
                #                 address=item['address'], baths=item['baths'],
                #                 beds=item['beds'], brokerCompany=item['brokerCompany'],
                #                 brokerName=item['brokerName'],
                #                 Url="https://www.landwatch.com" + item['canonicalUrl'],
                #                 city=item['city'],
                #                 cityID=item['cityID'],
                #                 companyLogoDocumentId=item['companyLogoDocumentId'],
                #                 county=item['county'], countyId=item['countyId'],
                #                 description=item['description'], hasHouse=item['hasHouse'],
                #                 hasVideo=item['hasVideo'],
                #                 hasVirtualTour=item['hasVirtualTour'],
                #                 imageCount=item['imageCount'],
                #                 imageAltTextDisplay=item['imageAltTextDisplay'],
                #                 isHeadlineAd=item['isHeadlineAd'],
                #                 lwPropertyId=item['lwPropertyId'], isALC=item['isALC'],
                #                 latitude=item['latitude'], state=item['state'],
                #                 longitude=item['longitude'], price=item['price'],
                #                 Rate=item['price'] / item['acres'], status=item['status'], zip=item['zip'],
                #
                #             )
                #             print("1")
                #         else:
                #             mylist_obj = PropertyMaster.objects.all().values().filter(lwPropertyId=item[lwPropertyId],
                #                                                                       user=request.user).update(
                #                 accountId=item['accountId'], acres=item['acres'],
                #                 adTargetingCountyId=item['adTargetingCountyId'],
                #                 address=item['address'], baths=item['baths'],
                #                 beds=item['beds'], brokerCompany=item['brokerCompany'],
                #                 brokerName=item['brokerName'],
                #                 Url="https://www.landwatch.com" + item['canonicalUrl'],
                #                 city=item['city'],
                #                 cityID=item['cityID'],
                #                 companyLogoDocumentId=item['companyLogoDocumentId'],
                #                 county=item['county'], countyId=item['countyId'],
                #                 description=item['description'], hasHouse=item['hasHouse'],
                #                 hasVideo=item['hasVideo'],
                #                 hasVirtualTour=item['hasVirtualTour'],
                #                 imageCount=item['imageCount'],
                #                 imageAltTextDisplay=item['imageAltTextDisplay'],
                #                 isHeadlineAd=item['isHeadlineAd'],
                #                 lwPropertyId=item['lwPropertyId'], isALC=item['isALC'],
                #                 latitude=item['latitude'], state=item['state'],
                #                 longitude=item['longitude'], price=item['price'],
                #                 Rate=item['price'] / item['acres'],status=status_dict[item["status"]], zip=item['zip'],
                #
                #             )
                #             print("2")
                #             mylist_obj.save()
                #     else:
                #         print("Aj")
                #         # PropertyMaster.objects.filter(id=item[lwPropertyId]).delete()
                #         PropertyMaster.save()
                #     # entry = TypeMaster.objects.all()
            print(n, " records found in zipcode : ", zip)

    finally:
        print("Completed")

        # qs = filter(request)
        # auths = PropertyMaster.objects.order_by('acres')
        # ordered = sorted(auths, key=operator.attrgetter('acres'))
        # context = {
        #     'queryset': qs,
        #     # 'acres': ordered,
        # }
        # return render(request, "bootstrap_form.html")


def job3():
    # a=0
    print("I'm Anshul...")
    zipcode_list = [758708]

    # zipcode_list = [75002, 75006, 75007, 75009, 75010, 75013, 75019, 75020, 75021, 75022, 75024, 75028, 75032,
    #                         75034, 75035, 75038, 75040, 75041, 75043, 75044, 75048, 75050, 75051, 75056, 75057, 75058,
    #                         75061, 75063, 75065, 75067, 75068, 75069, 75070, 75071, 75074,75076, 75077, 75078, 75080, 75081, 75083, 75087, 75088, 75089, 75090, 75092, 75093, 75097, 75098, 75102, 75103, 75104, 75105, 75109, 75110, 75114, 75115, 75116, 75117, 75119, 75124, 75126, 75135, 75142, 75143, 75144, 75147, 75148, 75154, 75156, 75159, 75160]
    #
    # with open("datafile") as myfile:
    #     head = [next(myfile) for x in range(N)]
    # with open('zip_code_database.csv', 'r') as file:
    #     # head = [next(myfile) for x in range(N)]
    #     reader = csv.reader(file)
    #     for row in range(30):
    #         print(row)
    # zipcode_list = [75002, 75006, 75007, 75009, 75010, 75013, 75019, 75020, 75021, 75022, 75024, 75028, 75032,
    #                 75034, 75035, 75038, 75040, 75041, 75043, 75044, 75048, 75050, 75051, 75056, 75057, 75058,
    #                 75061, 75063, 75065, 75067, 75068, 75069, 75070, 75071, 75074,75076, 75077, 75078, 75080, 75081, 75083, 75087, 75088, 75089, 75090, 75092, 75093, 75097, 75098, 75102, 75103, 75104, 75105, 75109, 75110, 75114, 75115, 75116, 75117, 75119, 75124, 75126, 75135, 75142, 75143, 75144, 75147, 75148, 75154, 75156, 75159, 75160]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"
    }
    try:

        for zip in zipcode_list:
            if len(str(zip)) == 4:
                zip = "0" + str(zip)
            n = 0
            url = "https://www.landwatch.com/api/property/search/1113/zip-" + \
                  str(zip) + "/land/listed-1-day"
            page = 0
            # print(url)
            page = requests.get(url, headers=headers)
            # time.sleep(random.randrange(1, 2))
            while (page == 0):
                page = requests.get(url, headers=headers)
                time.sleep(random.randrange(1, 5))
            data = page.json()
            print(data['searchResults']['locationSeo']['pageHeaderCount'])
            countListing = data['searchResults']['locationSeo']['pageHeaderCount']
            countListing = re.findall(r'\d+', countListing)
            print(countListing)
            if len(countListing) == 3:
                page_count = int(int(countListing[2]) / 25 + 2)
            else:
                page_count = 2
            # print(countListing)

            for i in range(1, page_count):
                url = "https://www.landwatch.com/api/property/search/1113/zip-" + \
                      str(zip) + "/land/listed-1-day/page-" + str(i)
                # print(url)
                page = 0
                page = requests.get(url, headers=headers)
                # time.sleep(random.randrange(1, 2))
                while (page == 0):
                    page = requests.get(url, headers=headers)
                    time.sleep(random.randrange(1, 5))
                data = page.json()
                # print("Length of data : ",len(data))

                for item in data['searchResults']['propertyResults']:
                    # a=a+1
                    prop = PropertyMaster.objects.create(accountId=item['accountId'], acres=item['acres'],
                                                         adTargetingCountyId=item['adTargetingCountyId'],
                                                         address=item['address'], baths=item['baths'],
                                                         beds=item['beds'], brokerCompany=item['brokerCompany'],
                                                         brokerName=item['brokerName'],
                                                         Url="https://www.landwatch.com" + item['canonicalUrl'],
                                                         city=item['city'],
                                                         cityID=item['cityID'],
                                                         companyLogoDocumentId=item['companyLogoDocumentId'],
                                                         county=item['county'], countyId=item['countyId'],
                                                         description=item['description'], hasHouse=item['hasHouse'],
                                                         hasVideo=item['hasVideo'],
                                                         hasVirtualTour=item['hasVirtualTour'],
                                                         imageCount=item['imageCount'],
                                                         imageAltTextDisplay=item['imageAltTextDisplay'],
                                                         isHeadlineAd=item['isHeadlineAd'],
                                                         types=' '.join(item['types']),Rate=item['price']/item['acres'],
                                                         lwPropertyId=item['lwPropertyId'], isALC=item['isALC'],
                                                         latitude=item['latitude'], state=item['state'],
                                                         longitude=item['longitude'], price=item['price'],
                                                         status=status_dict[item["status"]], zip=zip,
                                                         )

                    ###do something###

                    n = n + 1
                # print("n=",n)

                # for item in data['searchResults']['propertyResults']:
                #     if PropertyMaster.objects.filter(lwPropertyId=item['lwPropertyId']).exists():
                #
                #         if PropertyMaster.objects.all().values().filter(lwPropertyId=item[lwPropertyId],
                #                                                         user=request.user):
                #             PropertyMaster.objects.all().values().filter(lwPropertyId=item[lwPropertyId],
                #                                                          user=request.user).update(
                #                 accountId=item['accountId'], acres=item['acres'],
                #                 adTargetingCountyId=item['adTargetingCountyId'],
                #                 address=item['address'], baths=item['baths'],
                #                 beds=item['beds'], brokerCompany=item['brokerCompany'],
                #                 brokerName=item['brokerName'],
                #                 Url="https://www.landwatch.com" + item['canonicalUrl'],
                #                 city=item['city'],
                #                 cityID=item['cityID'],
                #                 companyLogoDocumentId=item['companyLogoDocumentId'],
                #                 county=item['county'], countyId=item['countyId'],
                #                 description=item['description'], hasHouse=item['hasHouse'],
                #                 hasVideo=item['hasVideo'],
                #                 hasVirtualTour=item['hasVirtualTour'],
                #                 imageCount=item['imageCount'],
                #                 imageAltTextDisplay=item['imageAltTextDisplay'],
                #                 isHeadlineAd=item['isHeadlineAd'],
                #                 lwPropertyId=item['lwPropertyId'], isALC=item['isALC'],
                #                 latitude=item['latitude'], state=item['state'],
                #                 longitude=item['longitude'], price=item['price'],
                #                 Rate=item['price'] / item['acres'], status=item['status'], zip=item['zip'],
                #
                #             )
                #             print("1")
                #         else:
                #             mylist_obj = PropertyMaster.objects.all().values().filter(lwPropertyId=item[lwPropertyId],
                #                                                                       user=request.user).update(
                #                 accountId=item['accountId'], acres=item['acres'],
                #                 adTargetingCountyId=item['adTargetingCountyId'],
                #                 address=item['address'], baths=item['baths'],
                #                 beds=item['beds'], brokerCompany=item['brokerCompany'],
                #                 brokerName=item['brokerName'],
                #                 Url="https://www.landwatch.com" + item['canonicalUrl'],
                #                 city=item['city'],
                #                 cityID=item['cityID'],
                #                 companyLogoDocumentId=item['companyLogoDocumentId'],
                #                 county=item['county'], countyId=item['countyId'],
                #                 description=item['description'], hasHouse=item['hasHouse'],
                #                 hasVideo=item['hasVideo'],
                #                 hasVirtualTour=item['hasVirtualTour'],
                #                 imageCount=item['imageCount'],
                #                 imageAltTextDisplay=item['imageAltTextDisplay'],
                #                 isHeadlineAd=item['isHeadlineAd'],
                #                 lwPropertyId=item['lwPropertyId'], isALC=item['isALC'],
                #                 latitude=item['latitude'], state=item['state'],
                #                 longitude=item['longitude'], price=item['price'],
                #                 Rate=item['price'] / item['acres'], status=item['status'], zip=item['zip'],
                #
                #             )
                #             print("2")
                #             mylist_obj.save()
                #     else:
                #         print("Aj")
                #         # PropertyMaster.objects.filter(id=item[lwPropertyId]).delete()
                #         PropertyMaster.save()
                #     # entry = TypeMaster.objects.all()
            print(n, " records found in zipcode : ", zip)

    finally:
        print("Completed")

        # qs = filter(request)
        # auths = PropertyMaster.objects.order_by('acres')
        # ordered = sorted(auths, key=operator.attrgetter('acres'))
        # context = {
            # 'queryset': qs,
            # 'acres': ordered,
        # }
        # return render(request, "bootstrap_form.html")


def login(request):
    if User.objects.filter(email=request.POST.get('login_email')).exists():
        user = User.objects.filter(email=request.POST.get('login_email'))[0]
        # if (bcrypt.checkpw(request.POST['login_password'].encode('utf-8'), user.password.encode('utf-8'))):
        if (request.POST.get('login_password') == user.password):
            request.session['id'] = user.id
            if request.POST.get('next',None) :
                print("Dipu")
                return  HttpResponseRedirect(request.GET['next'])
            return redirect('/show')
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


def is_valid_queryparam(param):
    return param != '' and param is not None

def export_users_csv2(request,qs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="AJ.csv"'

        writer = csv.writer(response)
        # writer.writerow(
        #     ['lwPropertyId', 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', 'Rate', 'Url', 'types',
        #      'status', 'created_at', 'updated_at'])

        # users = qs.object.filter.values_list('lwPropertyId', 'address', 'city', 'state', 'county', 'zip',
        #                                    'price', 'acres', 'Rate', 'Url', 'types', 'status',
        #                                    'created_at', 'updated_at')
        users = qs.filter(address="address", city="city", state="state", county="county",
                          Url="Url", types="types", status="status")
        # for user in users:
        writer.writerow(qs)

        return response


def filter(request):
    qs = PropertyMaster.objects.all()
    wq = AvgMaster.objects.all()
    category = PropertyMaster.objects.all()
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    view_acres = request.GET.get('view_acres')
    status = request.GET.get('status')
    title2_contains_query = request.GET.get('title2_contains')
    view_state = request.GET.get('view_state')
    types = request.GET.get('types')
    view_percentage = request.GET.get('view_percentage')


    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(city__icontains=title_contains_query)

    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)

    elif is_valid_queryparam(title_or_author_query):
        qs = qs.filter(Q(city__icontains=title_or_author_query)).distinct()
                       # | Q(author__name__icontains=title_or_author_query



    if is_valid_queryparam(view_count_min):
        qs = qs.filter(price__gte=view_count_min)

    if is_valid_queryparam(view_count_max):
        qs = qs.filter(price__lt=view_count_max+"1")

    if is_valid_queryparam(date_min):
        qs = qs.filter(publish_date__gte=date_min)

    if is_valid_queryparam(status) and status != 'Choose...':
        qs = qs.filter(status=status)

    if is_valid_queryparam(date_max):
        qs = qs.filter(publish_date__lt=date_max)

    if is_valid_queryparam(view_acres):
        qs = qs.filter(acres__gte=view_acres)

    if is_valid_queryparam(types):
        qs = qs.filter(types__icontains=types)

    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)

    elif is_valid_queryparam(types):
        qs = qs.filter(Q(types__icontains=types)).distinct()



    # if is_valid_queryparam(view_state):
    #     qs = qs.filter(state__icontains=view_state)
    #
    # elif is_valid_queryparam(id_exact_query):
    #     qs = qs.filter(id=id_exact_query)

    # elif is_valid_queryparam(types):
    #     qs = qs.filter(Q(state__icontains=view_state)).distinct()
    #
    # if is_valid_queryparam(view_percentage):
    #     wq = wq.filter(__gte=view_percentage)
    #

    # if is_valid_queryparam(acres) :
    #     qs = qs.filter(acres__values=acres)
    # export_users_csv2(request,qs)
    return qs

def filter2(request):
    qs = AvgMaster.objects.all()
    category = PropertyMaster.objects.all()
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    view_acres = request.GET.get('view_acres')
    status = request.GET.get('status')
    title2_contains_query = request.GET.get('title2_contains')
    view_state = request.GET.get('view_state')
    types = request.GET.get('types')
    view_percentage = request.GET.get('view_percentage')


    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(city__icontains=title_contains_query)

    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)

    elif is_valid_queryparam(title_or_author_query):
        qs = qs.filter(Q(city__icontains=title_or_author_query)).distinct()
                       # | Q(author__name__icontains=title_or_author_query



    if is_valid_queryparam(view_count_min):
        qs = qs.filter(price__gte=view_count_min)

    if is_valid_queryparam(view_count_max):
        qs = qs.filter(price__lt=view_count_max+"1")

    if is_valid_queryparam(date_min):
        qs = qs.filter(publish_date__gte=date_min)

    if is_valid_queryparam(status) and status != 'Choose...':
        qs = qs.filter(status=status)

    if is_valid_queryparam(date_max):
        qs = qs.filter(publish_date__lt=date_max)

    if is_valid_queryparam(view_acres):
        qs = qs.filter(acres__gte=view_acres)

    if is_valid_queryparam(types):
        qs = qs.filter(types__icontains=types)

    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)

    elif is_valid_queryparam(types):
        qs = qs.filter(Q(types__icontains=types)).distinct()



    # if is_valid_queryparam(view_state):
    #     qs = qs.filter(state__icontains=view_state)
    #
    # elif is_valid_queryparam(id_exact_query):
    #     qs = qs.filter(id=id_exact_query)

    # elif is_valid_queryparam(types):
    #     qs = qs.filter(Q(state__icontains=view_state)).distinct()
    #
    # if is_valid_queryparam(view_percentage):
    #     wq = wq.filter(__gte=view_percentage)
    #

    # if is_valid_queryparam(acres) :
    #     qs = qs.filter(acres__values=acres)
    export_users_csv2(request,qs)
    return qs



def infinite_filter(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    return PropertyMaster.objects.all()[int(offset): int(offset) + int(limit)]


def is_there_more_data(request):
    offset = request.GET.get('offset')
    if int(offset) > PropertyMaster.objects.all().count():
        return False
    return True

class ReactFilterView(generics.ListAPIView):
    serializer_class = JournalSerializer

    def get_queryset(self):
        qs = filter(self.request)
        return qs


class ReactInfiniteView(generics.ListAPIView):
    serializer_class = JournalSerializer

    def get_queryset(self):
        qs = infinite_filter(self.request)
        return qs

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response({
            "journals": serializer.data,
            "has_more": is_there_more_data(request)
        })
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('/')
# def export_users_csv2(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="AJ.csv"'
#
#     writer = csv.writer(response)
#         # writer.writerow(
#         #     ['lwPropertyId', 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', 'Rate', 'Url', 'types',
#         #      'status', 'created_at', 'updated_at'])
#
#     # users = qs.object.filter.values_list('lwPropertyId', 'address', 'city', 'state', 'county', 'zip',
#     #                                    'price', 'acres', 'Rate', 'Url', 'types', 'status',
#     #                                    'created_at', 'updated_at')
#     users = qs.filter(address="address", city="city", state="state", county="county",
#                                         Url="Url", types="types", status="status")
#         # for user in users:
#     writer.writerow(qs)
#
#     return response


@cache_control(no_cache=True, must_revalidate=True)
def logout_view(request):
    # logout(request)
    return render(request,'index2.html')


