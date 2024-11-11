from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('testlist/',views.testlist,name='testapp'), 
    path('personality_test/',views.load_test,name='survey'), 
    path('master_layout/',views.load_master,name='test master'), 
    path('test_result/',views.form_handler, name='form handler')  
]


