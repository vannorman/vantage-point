from django.conf.urls import *

import dragonboy.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'dragonboy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



	url(r'^$', dragonboy.views.home),

]
