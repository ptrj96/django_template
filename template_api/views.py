from django.http import HttpRequest, HttpResponse
import json
# Create your views here.


def hello(request: HttpRequest) -> HttpResponse:
    response_data = {"message": "Hello World"}
    return HttpResponse(json.dumps(response_data), content_type="application/json")
