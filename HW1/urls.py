from django.contrib import admin
from django.urls import path
from dog.views import home_view, time, workdir

urlpatterns = [
    path('', home_view, name='home'),
    path('current_time/', time, name='time'),
    path('workdir/', workdir, name='workdir'),
    path('admin/', admin.site.urls),
]