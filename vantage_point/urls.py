from django.conf.urls import *
import vantage_point.views
# from vantage_point import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'vantage_point.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


	url(r'^$', vantage_point.views.home),
	url(r'^verifyaccount/(.*)/$', vantage_point.views.verify_account),
]
