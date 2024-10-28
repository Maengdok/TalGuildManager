from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from src.services.api_response import send_json_response as api_response
from src.decorators.request_method_validator import required_method
from src.contracts.constant import Constants


from .models import Member

HttpCode = Constants.HttpResponseCodes

@required_method('GET')
@csrf_exempt
def list(request) -> JsonResponse:
    filter = request.GET.get('isActivate', True)
    
    members = Member.objects.all().values().filter(is_activate=True)

    return api_response(HttpCode.SUCCESS, 'success')