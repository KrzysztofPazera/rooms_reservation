from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

# Create your views here.
from Reservation_app.models import ConferenceRoom


def index(request):
    return render(request, 'base.html')


class AddRoomView(View):
    def get(self,request):
        rooms = ConferenceRoom.objects.all()
        return render(request, 'add_room.html', {'rooms':rooms})


    def post(self,request):
        name= request.POST['name']
        capacity= request.POST['capacity']
        projector_availability= request.POST.get('projector_availability') =='True'
        ConferenceRoom.objects.create(name=name, capacity=capacity ,projector_availability=projector_availability)
        return redirect(reverse('rooms_list'))

def rooms_list(request):
    objects = ConferenceRoom.objects.all()
    return render(request,'show_objects.html', {'objects':objects})

def room_detail_view(request, id):
    object = ConferenceRoom.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'room_detail.html', {'objects':object})
    else:
        name= request.POST['name']
        capacity = request.POST['capacity']
        projector_availability= request.POST['projector_availability']
        object.name = name
        object.capacity = capacity
        object.projector_availability = projector_availability
        object.save()
        return redirect('/rooms_list/')
