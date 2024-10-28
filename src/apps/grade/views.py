from django.http import JsonResponse

from src.services.api_response import send_json_response as api_response
from src.contracts.constant import Constants

HttpCode = Constants.HttpResponseCodes

def list(request) -> JsonResponse:
    return api_response(HttpCode.SUCCESS, 'success')