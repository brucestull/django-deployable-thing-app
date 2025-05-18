# things/views.py

from django.urls import reverse_lazy
from django.views import generic

from .forms import ThingForm
from .models import Thing


class ThingListView(generic.ListView):
    model = Thing


class ThingDetailView(generic.DetailView):
    model = Thing


class ThingCreateView(generic.CreateView):
    model = Thing
    form_class = ThingForm
    success_url = reverse_lazy("things:thing_list")


class ThingUpdateView(ThingCreateView, generic.UpdateView):
    pass


class ThingDeleteView(generic.DeleteView):
    model = Thing
    success_url = reverse_lazy("things:thing_list")
