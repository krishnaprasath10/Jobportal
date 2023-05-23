from django.urls import path,include
from .import views

urlpatterns = [
    path('login/',views.login_page,name="login"),
    path('register/',views.register,name="register"),
    path('jobdetails/<int:pk>',views.Jobdetails,name="jobdetails"),

    path('postjob/',views.postjob,name="postjob"),
     
    path('',views.Home,name="home"),
    path('about/',views.About,name="about"),
    path('contact/',views.Contact,name="contact"),
    path('portfolio/',views.Portfolio,name="portfolio"),
    path('services/',views.Services,name="services"),

    path('joblisting/',views.joblisting,name="jobslisting"),
    path('search_result/',views.jobsearch,name="search_result")



]
