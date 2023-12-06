from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def november(request):
    myDic = {
        'casinoChips':'100',
        'cardValue':'K',
        'totalValue':'491',
        }
        
    return render(request, 'blackjack.html', context = myDic)