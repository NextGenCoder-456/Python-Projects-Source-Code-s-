from django.shortcuts import render
from .models import Puzzle

def play(request, pid):
    p = Puzzle.objects.get(id=pid)
    board = [int(x) for x in p.board]
    return render(request, 'sudoku/play.html', {'board':board})
