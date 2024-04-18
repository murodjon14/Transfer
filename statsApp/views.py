from django.shortcuts import render
from .models import *

class LatesTransfersView(View):
    def get(self, request):
        contex = {
            'transferlar': Transfer.objects.order_by('-sana')
        }
        return render(request, 'latest-transfers.html', contex)
