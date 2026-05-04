from django.shortcuts import render
from .models import Shop
from django.shortcuts import get_object_or_404

# Create your views here.
def my_firstApp(request) :
    s = Shop.objects.all()
    return render(request, "all_firstApp.html", {"shop_list": s})

def shop_details(request, shop_id) :
    shop = get_object_or_404(Shop, pk=shop_id)
    return render(request, "shop_detail.html", {"shop_details": shop})