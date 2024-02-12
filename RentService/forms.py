from django.forms import ModelForm
from .models import Order
from django.db.models import ForeignKey

class Order_form(ModelForm):
    class Meta:
        model = Order
        fields = ['lake','beach','rent_day','equipment_id']
