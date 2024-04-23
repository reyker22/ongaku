from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('performer/', views.PerformersView.as_view(), name='performer'),
    path('library/', views.LibraryView.as_view(), name='library'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
