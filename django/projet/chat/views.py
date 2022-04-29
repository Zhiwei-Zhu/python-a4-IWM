import imp
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from chat.models import Room
from chat.form import RoomForms
from chat.models import Message
def index(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms,}
    return render(request,'chat/index.html',context)

def room(request, room_name):


    messages = Message.objects.filter(room=room_name)[0:25]
    
    chat_room = get_object_or_404(Room, name=room_name)
    context = {'room': chat_room,'messages': messages}
    return render(request,'chat/room.html',context)

def createroom(request):
    context ={}
 
    form = RoomForms(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
        
         
    context['form']= form
    return render(request,'chat/createroom.html',context)