from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Item


class ItemListView(ListView):
    model = Item
    template_name = "demo/item_list.html"


class ItemCreateView(CreateView):
    model = Item
    fields = ["name", "description"]
    template_name = "demo/item_form.html"
    success_url = reverse_lazy("item-list")
