from django.http import JsonResponse, HttpResponseRedirect
import requests
import json 

def index(reqest):
    return HttpResponseRedirect('https://jon.network/project/61/Ravencoin-Price-API-Reference/')


def rvn_usd(request):
    try:
        markets = json.loads(requests.get('https://tradeogre.com/api/v1/markets').content.decode('utf-8')) 
        for market in markets:
            try:
                rvn_btc = market['BTC-RVN']['price']
                break
            except KeyError:
                continue
            
        btc_usd = json.loads(requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').content.decode('utf-8'))['bpi']['USD']['rate_float']
        return JsonResponse({'success': True, 'usd': float(btc_usd) * float(rvn_btc)})
    except:
        return JsonResponse({'success': False, 'error': 'try again later'})