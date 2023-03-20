from django.shortcuts import render
from django.views import generic, View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from . import models
import json

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'

class MoviePeviewView(generic.TemplateView):
    template_name = 'list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tournament_pk = self.kwargs.get('pk')
        tournament = models.MovieTournament.objects.get(pk=tournament_pk)
        context['tournament_pk'] = tournament_pk
        context['link_list'] = tournament.link_list
        context['thumbnail_list'] = tournament.thumbnail_list
        context['title_list'] = tournament.title_list
        context['tournament_name'] = tournament.name
        return context

class ResultView(generic.TemplateView):
    template_name = 'list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tournament_pk = self.kwargs.get('pk')
        tournament = models.MovieTournament.objects.get(pk=tournament_pk)
        context['tournament_pk'] = tournament_pk
        context['link_list'] = tournament.link_list
        context['thumbnail_list'] = tournament.thumbnail_list
        context['title_list'] = tournament.title_list
        context['tournament_name'] = tournament.name
        context['winner_id'] = self.kwargs.get('winner_id')+1
        return context

class RankingView(generic.TemplateView):
    template_name = 'test.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tournament_pk = self.kwargs.get('pk')
        context['tournament_pk'] = tournament_pk
        tournament = models.MovieTournament.objects.get(pk=tournament_pk)
        context['link_list'] = tournament.link_list
        context['tournament_name'] = tournament.name
        return context

class SendDataView(View):
    def post(self, request):
        mylist = json.loads(request.POST.get('mylist'))
        print(mylist)
        return JsonResponse({'status': 'success'})

class RequestDataView(View):
    def post(self, request):
        category = request.POST.get('category')
        print(category)
        if category == "ミュージック":
            data = {'total': 0, 'database': 'MovieTournament', 'tournament':[]}
            for a in models.MovieTournament.objects.filter(category = 'music').order_by('-created_at'):
                data['tournament'].append({'name': a.name, 'comment': a.comment, 'id': a.id, 'num': len(a.link_list), 'category': a.category})
                data['total'] += 1
        elif category == "漫画":
            data = {'total': 0, 'database': 'Text_PictureTournament', 'tournament':[]}
            for a in models.MovieTournament.objects.filter(category = 'commic').order_by('-created_at'):
                data['tournament'].append({'name': a.name, 'comment': a.comment, 'id': a.id, 'num': len(a.link_list), 'category': a.category})
                data['total'] += 1
        elif category == "バラエティ":            
            data = {'total': 0, 'database': 'Text_PictureTournament', 'tournament':[]}
            for a in models.MovieTournament.objects.filter(category = 'variety').order_by('-created_at'):
                data['tournament'].append({'name': a.name, 'comment': a.comment, 'id': a.id, 'num': len(a.link_list), 'category': a.category})
                data['total'] += 1
        return JsonResponse(data)