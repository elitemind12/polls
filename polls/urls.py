from django.urls import path

from . import views
# plls app routes || urls
"""
comminicate to project urls(urlconf)

"""
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='views'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/results/', views.results, name='results'),
]