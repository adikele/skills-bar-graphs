from django.urls import path
from . import views
from django.urls import include

urlpatterns = [   
path('', views.index, name='index'),
path('api_info/', views.api_info, name='api_info'), 
path('valstreetdesign/', views.valstreetdesign, name='valstreetdesign'),
path('../reactdataexplorer', views.index, name='reactdataexplorer'),

#path('linegraphs/', views.select_countries_form, name='countries_form'),  #go to path linegraphs
#path('bargraphs/', views.select_country_form, name='country_form'),  #for bargraphs

#path('ref_plotly/', views.ref_plotly, name='ref_plotly'),  #go to path linegraphs
#path('grwa/', views.show_graph, name='show_graph'),  #go to path linegraphs

path('graphs/', views.show_skills, name='show_skills'),  #real one!


]
