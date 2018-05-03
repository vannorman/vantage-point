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
    
    # No session id passed (e.g. user navigated direct because they had a Daydream)
    url(r'^survey/pre/$', vantage_point.views.survey_pre),
    url(r'^survey/post/$', vantage_point.views.survey_post),

    # Session id passed from Unity in the URL
    url(r'^survey/pre/(.*)/$', vantage_point.views.survey_pre_session),
    url(r'^survey/post/(.*)/$', vantage_point.views.survey_post_session),

]
