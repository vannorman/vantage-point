from django.conf.urls import *
import vantage_point.views


urlpatterns = [
    url(r'^$', vantage_point.views.start, name='home'),
    # app.tryvantagepoint.com/
    # Presents an "Enter code" page. Code is submitted via JS POST command to /verifycode/ in templates/start.html.
    # Checks if user entered the correct code. 
    # Shows "Mount headset now" if correct code entered. 
    # No further functionality (does not hand-off any info to headset.)

    url(r'^verifyaccount/(.*)/$', vantage_point.views.verify_account), 
    # LEGACY - used by Oculus builds to check if the user entered the correct code on the Oculus machine.

    url(r'^verifycode/$', vantage_point.views.verify_code), 
    # Used to verify codes from templates/start.html
    
    url(r'^start/$', vantage_point.views.start),
    # both / and /start/ point to templates/start.html
    
    url(r'^survey/pre/$', vantage_point.views.survey_pre),
    url(r'^survey/post/$', vantage_point.views.survey_post),
    # Survey pages. Pressing "submit" on these pages will post directly to a google form. 
    # If that form is changed, you will need to ensure the form on this page matches the new form data.
    # Note that No session id passed (e.g. user navigated direct to this url beacuse we told them to.)

    url(r'^survey/pre/(.*)/$', vantage_point.views.survey_pre_session),
    url(r'^survey/post/(.*)/$', vantage_point.views.survey_post_session),
    # Same survey pages, but with a session id passed in the URL. The Legacy Oculus build used an in-game browser which passed a unique session id. This session ID is filled in a hidden form field and populated into the google form along with responses.

    # Google forms: 
    # PRototype form response sheet (first film footage), No longer used: 
    # https://docs.google.com/spreadsheets/d/1PfiUTiR5HuhBDl0pc-JaiE-WQrFxOlezbE3ihO01kdw/edit#gid=1124649957
    
    # New form response spreadsheet (Second film footage), Used with Oculus build:
    # https://docs.google.com/spreadsheets/d/1sOgDwbfzIacpUYPyxNKUs8v2VMLmVo13PPZ3F4apPa4/edit#gid=1124649957
    # NOTE: This response sheet appears to be empty. I haven't looked at this in over a month -- when I was
    # setting it up, it was working and app.tryvantagepoint.com/survey/pre and survey/post WERE correctly posting
    # to the google form. Not sure why the response sheets are empty now.

    # Survey itself and all form response sheets live in this folder
    # https://drive.google.com/open?id=1ui0MmQPOPnZ6MjXVnREgDoCTv-ekZQZC


]
