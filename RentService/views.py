from django.shortcuts import render
from django.views import View


class RentServiceView(View):
    template_name = 'RentService/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)