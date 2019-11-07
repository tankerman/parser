import sys
sys.path.insert(0, "/home/nekiwi/django/pars/scripts/")

import json

from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q

from parser import *

from .models import *
from .forms import *

# Create your views here.

class IndexView(View):
    template_name = 'index.html'
    
    def get(self, request):
        form = AddressForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        form = AddressForm(request.POST)
        if form.is_valid():
            try:
                data_dict = request.POST.dict()
                del data_dict['csrfmiddlewaretoken']
                url = advanced_search(data_dict) #ссылка для парсинга
                data = get_main_data(url) #данные из парсинга
                address = form.save(commit=False)
                info = self.create_info(data)
                address.info = info
                address.save()
            except:
                return render(request, '404.html')
        return redirect('list_view')

    def create_info(self, data):
        info = Info.objects.create()
        info.area = data[0]
        info.stages = data[1]
        info.year_exp = data[2]
        info.last_changes = data[3]
        info.year_build = data[4]
        info.year_exp1 = data[5]
        info.serial = data[6]
        info.house_type = data[7]
        info.fond = data[8]
        info.danger = data[9]
        info.wall_type = data[10]
        info.wall_mat = data[11]
        info.save()
        return info
    
class ListView(View):
    template_name = 'list.html'
    
    def get(self, request):
        address_list = Address.objects.all()
        form = SearchForm()
        max = Info.objects.order_by('-stages')[0].stages
        context = {
            'address_list': address_list,
            'form': form,
            'max': max
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        address_list = Address.objects.filter(info__wall_mat__icontains=request.POST['field'])
        if request.POST['field'] == 'all' or request.POST['field'] == '':
            address_list = Address.objects.all()
        form = SearchForm()
        context = {
            'address_list': address_list,
            'form': form
        }
        return render(request, self.template_name, context)