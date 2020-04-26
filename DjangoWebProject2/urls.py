from django.conf.urls import include, url
import testDjango.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', testDjango.views.index, name='index'),
    url(r'^home$', testDjango.views.index, name='home'),
]