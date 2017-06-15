from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.index, name='index'),
    #url(r'^participant/', views.participant_all, name='participant'),
    #url(r'^register/', views.registern, name='regiter')
]
