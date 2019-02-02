from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class TestView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print(request.META)
        return HttpResponse("api")
