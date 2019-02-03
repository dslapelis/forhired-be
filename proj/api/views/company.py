from django.shortcuts import render
from django.http import JsonResponse, HttpResponseServerError
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from authentication.models import Company


class CompanyView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            return JsonResponse(list(Company.objects.all().values()), safe=False)
        except:
            return HttpResponseServerError("Something went wrong.")
