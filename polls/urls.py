from django.urls import path

from . import views
# plls app routes || urls
"""
comminicate to project urls(urlconf)

"""
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='views'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]