from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls import url
from core import views
from django.urls import path
# from socialcustom.views import SomeTableView


urlpatterns = [
    # url(r'^$', views.index),
    # url(r'^login$', views.login),
    # path('api-auth/', include('rest_framework.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('admin/', admin.site.urls),
    # path('', BootstrapFilterView, name='bootstrap'),
    # path('api/', ReactFilterView.as_view(), name='react'),
    # path('infinite-api/', ReactInfiniteView.as_view(), name='infinite-react'),
    # re_path(r'^react/', TemplateView.as_view(template_name='index.html')),
    # url(r'^register$', views.register),
    # url(r'^success$', views.success),
    #
    # url(r'^job$', views.job),
    # url(r'^simple_list$', views.simple_list),

    url(r'^$', views.index),
    # url(r'^loader$', views.loader, name='loader'),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^show$', views.show),
    url(r'^Alert$', views.Alert),
    url(r'^logout_view$', views.logout_view),
    path('loader', views.loader, name='loader'),
    url(r'^export_users_csv2$',views.export_users_csv2, name='export_users_csv2'),



    # url(r'^job$', views.job),

    # path('', views.BootstrapFilterView, name='bootstrap'),
    # url(r'^ActorsView$', ActorsView.as_view(), name="actors"),

    # url(r'^Loader$', views.Loader),
    # url(r'^Rishu$', views.Rishu),

    # path("a",SomeTableView.as_view())

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
