from django.shortcuts import render
from .models import Accessorie
from django.http import JsonResponse
import json


# Create your views here.
def accessories(request):
    accessories=Accessorie.objects.all()
    data ={
        'accessories' : accessories,
    }
    return render(request, 'accessories/accessories.html',data)

def checkout(request, pk):
	accessories = Accessorie.objects.get(id=pk)
	data = {
        'accessories' : accessories,
    }
	return render(request, 'accessories/checkout.html',data)
def simpleCheckout(request):
    return render(request, 'accessories/simple_checkout.html')

def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	accessories = Accessorie.objects.get(id=body['accessoriesId'])
	Order.objects.create(
		accessories=accessories
		)
	return JsonResponse('Payment completed!', safe=False)