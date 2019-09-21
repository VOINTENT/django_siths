from django.urls import path

from .views import RecruitCreateView, IndexView, test_view, SithListView, BonusView, recruits_list_view

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('recruit/', RecruitCreateView.as_view(), name='recruit_create_view'),
    path('recruit/<int:recruit_id>/', test_view, name='test_view'),
    path('sith/', SithListView.as_view(), name='sith'),
    path('sith/<int:sith_id>', recruits_list_view, name='recruits_list_view'),
    path('bonus/', BonusView.as_view(), name='bonus'),
]
