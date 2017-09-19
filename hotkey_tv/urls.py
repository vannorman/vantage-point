from django.conf.urls import *

import hotkey_tv.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hotkey_tv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



	url(r'^$', hotkey_tv.views.home),

]
