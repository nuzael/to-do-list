from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import ToDo

    
class AllList(LoginRequiredMixin, CreateView, ListView):
    model = ToDo
    fields = ['task']
    template_name = 'list/all.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('all')
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user).order_by('-id')
        return qs
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class ActiveList(LoginRequiredMixin, CreateView, ListView):
    model = ToDo
    fields = ['task']
    template_name = 'list/active.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('active')
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user, completed=False).order_by('-id')
        return qs
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
   
class CompletedList(LoginRequiredMixin, CreateView, ListView):
    model = ToDo
    fields = ['task']
    template_name = 'list/completed.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('completed')
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user, completed=True).order_by('-id')
        return qs
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = ToDo
    fields = ['task', 'completed']
    context_object_name = 'tasks'
    template_name = 'list/edit.html'
    success_url = reverse_lazy('all')
    
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = ToDo
    template_name = 'list/delete.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('all')