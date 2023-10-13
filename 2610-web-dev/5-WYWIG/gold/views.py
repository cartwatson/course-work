from django.shortcuts import render

app_name = 'gold'
def index(request):
    context = {}
    return render(request, 'gold/index.html', context)
