

from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index,name="home"),
    path("articles", views.articles, name="articles"),
    path("practiceset",views.practiceset, name = "practiceset"),
    path("interviewquestionset",views.interviewquestionset,name = "interviewquestionset"),
    path("introductiontodatascience",views.introductiontodatascience, name = "introductiontodatascience"),
    path("differencesupervisedunsupervised",views.differencesupervisedunsupervised, name = "differencesupervisedunsupervised"),
    path("featureengineering",views.featureengineering, name = "featureengineering"),
    path("datasciencemistakes",views.datasciencemistakes, name = "datasciencemistakes"),
    path("machinelearningmcq",views.machinelearningmcq, name = "machinelearningmcq"),
    path("pythoncoding",views.pythoncoding, name = "pythoncoding"),
    path("statisticquiz",views.statisticquiz, name = "statisticquiz"),
    path("projectTips",views.projectTips, name = "projectTips"),
    path("numpypandas",views.numpypandas, name = "numpypandas")

]