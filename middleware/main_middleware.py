from typing import Any
from django.http import HttpResponse


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time Initialization: Initialized")

    def __call__(self, request):
        print(f"incomming request: {request.method}{request.path}")

        response = self.get_response(request)

        print(f"Outgoing Response Status Code: {response.status_code}")

        return response

    # def process_view(self,request,*args, **kwargs):
    #     return HttpResponse("Ended")

    def process_exception(self, request, exception):
        return HttpResponse(exception)

    def process_template_response(self,request,response):
        response.context_data['name'] = "Yashdeep"
        return response