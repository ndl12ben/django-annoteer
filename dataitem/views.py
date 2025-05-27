from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Dataitem
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Dataitem

# List View: shows all Dataitems
class DataitemListView(ListView):
    model = Dataitem
    template_name = 'dataitem/dataitem_list.html'
    context_object_name = 'dataitems'


class DataitemCreateView(CreateView):
    model = Dataitem
    fields = ['name', 'description', 'uploaded_file']
    success_url = reverse_lazy('dataitem_list')

    def form_valid(self, form):
        # Only set created_by if the user is authenticated
        if self.request.user.is_authenticated:
            form.instance.created_by = self.request.user
        # Otherwise: skip it (created_by can be null now)
        return super().form_valid(form)



