from django.shortcuts import render
from django.views import View
from .models import *


class Home(View):
    def get(self, request):
        return render(request, 'index.html')

class Clubs(View):
    def get(self, request):
        contex = {
            'clublar':Club.objects.order_by('kapital')
        }
        return render(request, 'clubs.html', contex)

class LatesTransfersView(View):
    def get(self, request):
        contex = {
            'transferlar': Transfer.objects.order_by('-sana')
        }
        return render(request, 'latest-transfers.html', contex)

class U20players(View):
    def get(self, request):
        all_players = Player.objects.all()
        players = []
        for player in all_players:
            if player.yosh() <= 20:
                players.append(player)
        contex = {
            'players':players
        }
        return render(request, 'U-20 players.html')