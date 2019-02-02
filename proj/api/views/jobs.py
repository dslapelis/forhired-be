from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from api.models import Job


class JobsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        return HttpResponse("api")
