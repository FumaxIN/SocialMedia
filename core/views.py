from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class Index(View):
    # template_name = 'core/index.html'
    def get(self,request):
        return render(request, 'index.html')


