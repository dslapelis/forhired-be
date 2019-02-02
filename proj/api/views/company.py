from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from authentication.models import Company


class CompanyView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return JsonResponse(list(Company.objects.all().values()), safe=False)
