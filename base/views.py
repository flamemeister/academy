from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

# rooms = [
#     {'id': 1, 'name':'Lets learn science!'},
#     {'id': 2, 'name': 'Math with me'},
#     {'id': 3, 'name': 'Students'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms' : rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    context = {'form' : form}
    return render(request, 'base/room_form.html', context)
