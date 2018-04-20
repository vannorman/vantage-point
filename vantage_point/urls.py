from django.conf.urls import *
import vantage_point.views
# from vantage_point import views


urlpatterns = [
    # Examples:
    url(r'^$', vantage_point.views.start, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^verifyaccount/(.*)/$', vantage_point.views.verify_account),
    url(r'^verifycode/$', vantage_point.views.verify_code),
    url(r'^start/$', vantage_point.views.start),
    url(r'^survey/pre/$', vantage_point.views.survey_pre),

]
