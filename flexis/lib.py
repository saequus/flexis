from django.http import JsonResponse
from flexis.models import Flexi

def flexis_view(request, flexi_key):
    flexi = None
    print(flexi_key) 
    try:
        flexi = Flexi.objects.get(key=flexi_key)
    except (ObjectDoesNotExist):
        return JsonResponse({'errors': 'flexi_object_not_found'})
    return JsonResponse(flexi.value)


