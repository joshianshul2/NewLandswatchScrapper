from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Sum,Avg
from .models import User,UserManager,PropertyMaster,Property_TypeMaster,TypeMaster,AvgMaster
import csv
import requests
import time

def job3():
     time.sleep(5)
     with open('texas_zip_code.csv', 'r') as file:
        reader = csv.reader(file)
        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                "Accept-Encoding": "*",
                "Connection": "keep-alive"
            }
        try:

                for zip in reader:
                    print("ZipCode : ",zip)
                    time.sleep(5)
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
                    countListing = data['searchResults']['locationSeo']['pageHeaderCount']
                    countListing = re.findall(r'\d+', countListing)
                    if len(countListing) == 3:
                        page_count = int(int(countListing[2]) / 25 + 2)
                    else:
                        page_count = 2
                    # print(countListing)

                    for i in range(1, page_count):
                        time.sleep(5)
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
                            time.sleep(5)
                            # a=a+1
                            print(item['zip'][0])
                            prop = PropertyMaster.objects.create(accountId=item['accountId'], acres=item['acres'],
                                                                 adTargetingCountyId=item['adTargetingCountyId'],
                                                                 address=item['address'], baths=item['baths'],
                                                                 beds=item['beds'], brokerCompany=item['brokerCompany'],
                                                                 brokerName=item['brokerName'],
                                                                 Url="https://www.landwatch.com" + item['canonicalUrl'],
                                                                 city=item['city'],
                                                                 cityID=item['cityID'],types=''.join(item['types']),
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

job3()