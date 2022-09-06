from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm


# make sure that dictionary keys are within quotes
# rooms = [
#     {'id':1, 'name': 'Math Study Room'},
#     {'id':2, 'name': 'Science Study Room'},
#     {'id':3, 'name': 'Python Study Room'},
#     {'id':4, 'name': 'Art Study Room'},
#     {'id':5, 'name': 'English Study Room'},
# ]


def home(request):
    rooms = Room.objects.all() # SELECT ALL
    context = {'rooms': rooms}
    return render(request, 'baseapp/home.html', context)



def room(request, url_id):
    # id: primary key in database; auto-generated/incremented id table field, not manually created in models.py
    # url_id: parameter name from url mapping
    rooms = Room.objects.get(id = url_id)

    # roomObject = None

    # for indiv_room in rooms:
    #     if indiv_room['id'] == int(idRequest):
    #         roomObject = indiv_room


    context = {'room': rooms}
    return render(request, 'baseapp/room.html', context)


def createRoom(request):
    form = RoomForm()

    # save/process form upon submission
    if request.method == 'POST': # when a user submits the create room form
        #print(request.POST) # show the data that submitted by the user
        form = RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('baseapproute:home')

    context = {'form': form}
    return render(request, 'baseapp/room_form.html', context)


def updateRoom(request, url_id):
    room = Room.objects.get(id = url_id)
    form = RoomForm(instance = room) # for each room object instance, fill out the form fields with the forms info; for editing room details

    # save/process form upon submission
    if request.method == 'POST': # when a user submits the create room form
        #print(request.POST) # show the data that submitted by the user
        form = RoomForm(request.POST, instance = room) # update that specific room instance, don't add a new room

        if form.is_valid():
            form.save()
            return redirect('baseapproute:home')

    context = {'form': form}
    return render(request, 'baseapp/room_form.html', context)


def deleteRoom(request, url_id):
    room = Room.objects.get(id = url_id)

    # upon confirming room deletion
    if request.method == 'POST': # when a user submits the create room form
        room.delete()
        return redirect('baseapproute:home')

    return render(request, 'baseapp/delete.html', {'obj': room})