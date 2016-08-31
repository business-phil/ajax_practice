from django.conf.urls import url
from views import Welcome, Posts

urlpatterns = [
    url(r'^$', Welcome.as_view(), name='welcome'),
    url(r'^posts$', Posts.as_view(), name='posts'),
]
