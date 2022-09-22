from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UserForm


class UserCreate(CreateView):
    form_class = UserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('all')