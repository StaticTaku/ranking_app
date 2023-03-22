"""load django"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()
"""complete loading"""

from ranking.models import MovieTournament
new_object = MovieTournament.objects.get(name="KPOP 2023 - K-POP Songs 2023")

delet_list = [1, 2, 4, 5, 10, 11, 13, 18, 20, 22, 23, 27, 29, 30, 33, 34, 35, 36, 37, 38, 39, 41, 43, 44, 45, 47, 48, 54, 56, 58, 60, 61, 62, 66, 68, 71, 74, 75, 76, 83, 86, 87, 89, 90, 92, 93, 95, 96, 98, 99, 104, 109, 110, 111, 114, 116, 119, 120, 121, 127, 130, 132, 139, 140, 144, 145, 147, 149]

list_title = new_object.title_list
list_link = new_object.link_list

reduction = 0
for i in delet_list:
    list_title.pop(i - reduction)
    list_link.pop(i - reduction)
    reduction += 1


new_object.title_list = list_title
new_object.link_list = list_link

new_object.save()