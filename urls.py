Lower level urls file
=====================
#from . import views
#from django.shortcuts                                import render_to_response
#from django.shortcuts                                 import get_object_or_404, redirect
#from django.utils                                     import timezone
# from django.template                                  import RequestContext
#from .models                                          import Itmanual
#from .forms                                           import PostForm
#from . import views
from django.conf.urls                                 import patterns, url, include
from django.shortcuts                                 import render
from django.contrib                                   import admin

def all_items(request):
    return render(request, 'ogsocial/og-events.html', {})

urlpatterns = [
    #url(r'^og/post/(?P<pk>[0-9]+)/$', views.post_detail),
    #url(r'^og/post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    #url(r'^og/post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^$', all_items),
    url(r'^admin/', include(admin.site.urls)),
]

