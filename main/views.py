from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    return render(request, 'quiz/index.html', context=context)


def play(request):
    context = {}
    return render(request, 'quiz/play.html', context=context)


def game(request):
    context = {}
    return render(request, 'quiz/game.html', context=context)


def end(request):
    context = {}
    return render(request, 'quiz/end.html', context=context)


def highscores(request):
    context = {}
    return render(request, 'quiz/highscores.html', context=context)
