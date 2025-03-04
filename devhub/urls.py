"""
URL configuration for devhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import Profile, myProfile, home, index
from accounts import views as accounts_views
from meetup_point import views as meetup_views

urlpatterns = [
    # admin pages
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    #path('', include('accounts.urls')), #moved the home views in accounts to here

    # user pages
    path('my-profile/', myProfile, name='my-profile'),
    path('profile/<int:id>', Profile, name='profile'),
    path('', home, name='home'),

    # api pages
    path('api-auth/', include('rest_framework.urls')),
    path('api/profiles/', accounts_views.profile_list),
    path('api/get-profile/<int:pk>', accounts_views.profile_detail),
    path('api/rooms/', accounts_views.room_list),
    path('api/get-rooms/<int:pk>', accounts_views.get_room),
    path('api/messages/', accounts_views.message_list),
    path('api/get-chathistory/<uuid:pk>', accounts_views.get_chat),

    # chat pages
    path('index/', index, name='index'),#this is apart of testing for the implementation of the video chat
    path('meetup_point/home.html', meetup_views.meetup_home, name='home'),
    #path("meetup_point/find-halfway", meetup_views.find_halfway_view, name="find_halfway"),
    path("meetup_point/find_halfway", meetup_views.find_halfway_view, name="find_halfway_view"),
    #path("meetup_point/find_meetup_spot/?lat=<str:lat>&lng=<str:lng>&places=<str:places_query>", meetup_views.find_meetup_spot, name="find_meetup_spot")
    path("meetup_point/find_meetup_spot/", meetup_views.find_meetup_spot, name="find_meetup_spot"),
    path("meetup_point/find_meetup_spot/get-directions/", meetup_views.get_directions_view, name="get_directions")
]
