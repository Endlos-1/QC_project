from django.urls import path

from . import views
app_name = 'home'


urlpatterns = [
    path('', views.index, name='index'),
    path('agent', views.agent_Faq, name='agent_Faq'),
    path('broker', views.broker_Faq, name='broker_Faq'),
    path('applynow', views.applynow, name='applynow'),
    path('contactus',views.contactUs,name='contactUs'),
    path('aboutUs',views.aboutUs, name='aboutUs'),
]
