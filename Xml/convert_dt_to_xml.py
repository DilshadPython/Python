from products.models import Item
from django.core import  serializers
from django.http import HttpResponse


def item_list(request):
	qs = Item.objects.all()
	qs = serializers.serialize('xml', qs)
	
	return HttpResponse(qs, content_typ='application/xml')