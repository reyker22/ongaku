from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from main.forms import SearchForm
from main.models import Performers, TrackList


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracks'] = TrackList.objects.all()[:5]
        context['releases'] = TrackList.objects.all()[:5]
        context['performers'] = Performers.objects.all()[:3]
        return context


class PerformersView(TemplateView):
    template_name = 'main/performer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracks'] = TrackList.objects.all()[:5]
        context['releases'] = TrackList.objects.all()[:5]
        context['performers'] = Performers.objects.all()[:3]
        return context


class LibraryView(TemplateView):
    template_name = 'main/library.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracks'] = TrackList.objects.all()[:5]
        context['releases'] = TrackList.objects.all()[:5]
        context['performers'] = Performers.objects.all()[:3]
        return context


class SearchResultsView(ListView):
    model = TrackList
    template_name = 'main/search.html'
    context_object_name = 'releases'
    paginate_by = 10

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = TrackList.objects.filter(
            Q(track_name__icontains=query) | Q(performer__performer_name__icontains=query)
        )
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['performers'] = Performers.objects.all()[:3]
        context['query'] = self.request.GET.get('q')
        return context