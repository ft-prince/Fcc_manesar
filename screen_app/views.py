# views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Station, Product, ProductMedia
from .forms import StationForm

class StationListView(ListView):
    model = Station
    template_name = 'station_list.html'
    context_object_name = 'stations'

class StationDetailView(DetailView):
    model = Station
    template_name = 'station_detail.html'
    context_object_name = 'station'

class StationCreateView(CreateView):
    model = Station
    form_class = StationForm
    template_name = 'station_form.html'

class StationUpdateView(UpdateView):
    model = Station
    form_class = StationForm
    template_name = 'station_form.html'

class StationDeleteView(DeleteView):
    model = Station
    template_name = 'station_confirm_delete.html'
    success_url = reverse_lazy('station_list')

def get_product_media(request):
    product_ids = request.GET.getlist('products[]')
    media = ProductMedia.objects.filter(product__in=product_ids)
    
    media_list = [
        {
            'id': media.id,
            'url': media.file.url,
            'type': media.file.name.split('.')[-1].lower(),
            'duration': media.duration
        }
        for media in media
    ]
    
    return JsonResponse({'media': media_list})

def get_station_media(request, station_id):
    station = Station.objects.get(pk=station_id)
    selected_media = station.selected_media.all()
    
    media_data = [
        {
            'url': m.file.url,
            'type': m.file.name.split('.')[-1].lower(),
            'duration': m.duration
        }
        for m in selected_media
    ]

    return JsonResponse({'media': media_data})

def station_media_slider(request, station_id):
    station = get_object_or_404(Station, pk=station_id)
    return render(request, 'station_slider.html', {'station': station})
