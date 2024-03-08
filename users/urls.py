from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from users import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('communities/', views.CommunityList.as_view()),
    path('communities/<uuid:pk>/', views.CommunityDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
