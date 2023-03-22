from django.shortcuts import render
from django.views import generic, View
from django.http import JsonResponse
from django.shortcuts import redirect
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

def ranking_view(request, pk, num):
    referer = request.META.get('HTTP_REFERER')
    if referer and 'preview/movies/'+str(pk) in referer:
        tournament = models.MovieTournament.objects.get(pk=pk)
        context = {
            'tournament_pk': pk,
            'link_list': tournament.link_list,
            'title_list': tournament.title_list,
            'tournament_name': tournament.name,
            'num':num
        }
        return render(request, 'test.html', context)
    else:
        return redirect('/preview/movies/'+str(pk))

def hidden_view(request, pk, num):
    referer = request.META.get('HTTP_REFERER')
    tournament = models.MovieTournament.objects.get(pk=pk)
    context = {
        'tournament_pk': pk,
        'link_list': tournament.link_list,
        'title_list': tournament.title_list,
        'tournament_name': tournament.name,
        'num':num
    }
    return render(request, 'test2.html', context)
    

class SendDataView(View):
    def post(self, request):
        mylist = json.loads(request.POST.get('mylist'))
        print(mylist)
        return JsonResponse({'status': 'success'})

class RequestDataView(View):
    def post(self, request):
        category = request.POST.get('category')
        data = {'total': 0, 'card_num':0, 'tournament':[]}
        if category == "ミュージック":
            selected_list = models.MovieTournament.objects.filter(category = 'music').order_by('-created_at')
            data['total'] = len(selected_list)
            for a in selected_list[int(request.POST.get('first')):int(request.POST.get('end'))]:
                data['tournament'].append({'name': a.name, 'comment': a.comment, 'id': a.id, 'num': len(a.link_list), 'category': a.category})
                data['card_num'] += 1

        elif category == "漫画":
            selected_list = models.MovieTournament.objects.filter(category = 'comic').order_by('-created_at')
            data['total'] = len(selected_list)
            for a in selected_list[int(request.POST.get('first')):int(request.POST.get('end'))]:
                data['tournament'].append({'name': a.name, 'comment': a.comment, 'id': a.id, 'num': len(a.link_list), 'category': a.category})
                data['card_num'] += 1
                
        elif category == "バラエティ":            
            selected_list = models.MovieTournament.objects.filter(category = 'variety').order_by('-created_at')
            data['total'] = len(selected_list)
            for a in selected_list[int(request.POST.get('first')):int(request.POST.get('end'))]:
                data['tournament'].append({'name': a.name, 'comment': a.comment, 'id': a.id, 'num': len(a.link_list), 'category': a.category})
                data['card_num'] += 1
        
        elif category == "全部":
            selected_list = models.MovieTournament.objects.all().order_by('-created_at')
            data['total'] = len(selected_list)
            for a in selected_list[int(request.POST.get('first')):int(request.POST.get('end'))]:
                data['tournament'].append({'name': a.name, 'comment': a.comment, 'id': a.id, 'num': len(a.link_list), 'category': a.category})
                data['card_num'] += 1

        elif category == "all":
            selected_list = models.MovieTournament.objects.all().order_by('-created_at')
            data['total'] = len(selected_list)
            for a in selected_list[int(request.POST.get('first')):int(request.POST.get('end'))]:
                data['tournament'].append({'name': a.name, 'comment': a.comment, 'id': a.id, 'num': len(a.link_list), 'category': a.category})
                data['card_num'] += 1
    
        return JsonResponse(data)