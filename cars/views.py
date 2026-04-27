from django.views.generic import ListView
from .models import Car

class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'
