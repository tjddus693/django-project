from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

from .models import Board

def board1(request):
    return render(request,'board/board1.html')

def board2(request):
    board_list = Board.objects.all()
    return render(request, 'board/board2.html',{
        'board_list':board_list
    })
    
def board3(request):
    if request.method == 'GET':
        return render(request, 'board/board3.html')
    else:
        title = request.POST['title']
        content = request.POST['content']
        writer = request.POST['writer']
        Board(title=title, writer=writer, content=content).save()
        return HttpResponseRedirect(reverse('board:board2'))
    
def detail(request, id):
    info = Board.objects.get(id=id)
    info.incrementReadCount()
    return render(
        request,
        'board/detail.html',
        {'info':info}
    )

def delete(request, id):
    info = Board.objects.get(id=id)
    if request.method == "GET":
        return render(
            request,
            'board/delete.html',
            {'info':info}
        )
    elif request.method == 'POST':
        info.delete()
        return HttpResponseRedirect(reverse('board:board2'))

def update(request,id):
    info = Board.objects.get(id=id)
    if request.method == 'GET':
        return render(
            request,
            'board/update.html',
            {'info':info}
        )
    elif request.method == 'POST':
        info.title = request.POST['title']
        info.writer = request.POST['writer']
        info.content = request.POST['content']
        info.save()
        return HttpResponseRedirect(reverse('board:detail', args=(info.id,)))
    
    
    