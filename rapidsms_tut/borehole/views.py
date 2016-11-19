from django.shortcuts import render

from .models import Borehole

# Sends borehole_list to be used by index.html (which controls the map
def index(request):
    borehole_list_all = Borehole.objects.all()
    context = {'borehole_list_all': borehole_list_all}
    return render(request, 'borehole/index.html', context)
# Create your views here.
