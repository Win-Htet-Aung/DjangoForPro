from django.urls import path
from .views import HomePageView, AboutPageView, new_home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('new_home/', new_home, name='new_home'),
]
x_urls = staticfiles_urlpatterns()
print('x', x_urls)

urlpatterns += staticfiles_urlpatterns()
