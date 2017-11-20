from django.conf.urls import url
from ngaraapp import views
# from snippets import views
from .views import (
UserView,
UserLoginView,



)
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
  url(r'^users/$', UserView.as_view()),
  url(r'^login/$', UserLoginView.as_view()),
   
#   url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
  
  
  # url(r'^users/$', UserView.as_view()),
  # url(r'^login/$', UserSignupView.as_view()),
]

urlpatterns = [
    # url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/$', views.snippet_detail),
]




