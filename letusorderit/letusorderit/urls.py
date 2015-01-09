from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'letusorderit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(
    #     regex=r'^$',
    #     view=RedirectView.as_view(url='/api/v1', permanent=False),
    #     name="redirect_to_api"
    # ),

    url(r'^v1/', include('ordermgmt.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
