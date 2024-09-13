from django.shortcuts import render

# Create your views here.

def index(request):
    # pega o tipo do metodo GET/POST
    print(request.method)
    context = {
        'msg': 'hello wolrd'
    }

    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')