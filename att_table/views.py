
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (ListView)

from att_table.models import Vacation


class TablesList(ListView):
    model = Vacation
    context_object_name = 'lists'
    # queryset = Vacation.objects.all()
    template_name = 'att_table/react_tem.html'

    def get_queryset(self):
        vacation_data = Vacation.objects.all()
        data = serializers.serialize('json', vacation_data)
        return HttpResponse(data, content_type="application/json")


def table(request):
    vacation_data = Vacation.objects.all()
    vacation_data_json = serializers.serialize('json', vacation_data)

    return render(request,
                  "att_table/react_tem.html",
                  context={'table': vacation_data_json})
