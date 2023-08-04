from django.shortcuts import render
from django.views import View
from RentService.models import Order, Customer, Lake, Beach, Schedule, Equipment
import logging
import json


class RentServiceView(View):
    template_name = 'RentService/index.html'

    def get(self, request, *args, **kwargs):
        lakes = Lake.objects.all()
        beaches = Beach.objects.all()
        dates = Schedule.objects.all()
        equipment_list = Equipment.objects.all()
        data = [[{'cost_for_hour': eq.cost_for_hour,
                  'cost_for_3_hours': eq.cost_for_3_hours,
                  'cost_for_day': eq.cost_for_day}] for eq in equipment_list]
        date_data = [{'dates':
                          {
                              f'{date.id}': {
                                  'beaches': [beach.name for beach in date.beaches.all()]
                              } for date in Schedule.objects.all()
                          }
        }]
        lakes_data = [{'lakes':
                           {
                               f'{beach.name}': {
                                   'lake': beach.lake.id
                               } for beach in Beach.objects.all()
                           }
        }]
        context = {'lakes': lakes,
                   'beaches': beaches,
                   'dates': dates,
                   'equipment_list': equipment_list,
                   'data': json.dumps(list(data)),
                   'date_data': json.dumps(list(date_data)),
                   'lakes_data': json.dumps(list(lakes_data))}
        return render(request, self.template_name, context)

    def post(self, request):
        lake = request.POST.get('lake')
        beach = request.POST.get('beach')
        date = request.POST.get('date')
        equipment_id = request.POST.get('equipment_id')
        time = request.POST.get('time')
        rent_time = request.POST.get('rent_time')
        cost = request.POST.get('cost')
        comment = request.POST.get('comment')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        logging.critical(lake, beach, date, equipment_id, time, rent_time, cost, comment, username, phone)
        # new_customer = Customer()
        # new_order = Order()
        return render(request, self.template_name)