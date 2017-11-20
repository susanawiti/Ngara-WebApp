from django.conf.urls import url


from .views import SnippetServiceAPIView


urlpatterns = [
    url(r'^$',SnippetServiceAPIView.as_view())
    ]