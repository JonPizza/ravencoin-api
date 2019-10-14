from django.http import JsonResponse

def index(reqest):
    return JsonResponse({'it': 'works!'})