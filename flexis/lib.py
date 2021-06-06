from django.http import JsonResponse
from flexis.models import Flexi
from django.core.exceptions import ObjectDoesNotExist
try:
    from django.conf import settings
    FLEXIS_SETTING_MAP = settings.FLEXIS_SETTING_MAP 
except (AttributeError, ImportError):
    FLEXIS_SETTING_MAP = None


def flexis_view(request, flexi_key):
    flexi = None
    content = {'status': 'ok'}

    if FLEXIS_SETTING_MAP:
        for k, v in FLEXIS_SETTING_MAP.items():
            if flexi_key == k:
                content.update(v)
                return JsonResponse(content)


    print(flexi_key) 
    try:
        flexi = Flexi.objects.get(key=flexi_key)
    except (ObjectDoesNotExist):
        content = {'errors': 'object_not_found', 'status': 'error'} 
        return JsonResponse(content)

    content.update(flexi.value) 
    return JsonResponse(content)


