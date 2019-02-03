from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from django.core.files.uploadedfile import UploadedFile
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from api.models import Resume
from django.contrib.auth.models import User
import json


class ResumeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(request.FILES['resume'])
        try:
            user = User.objects.get(username=request.user)
        except Exception as e:
            print(e)
            return HttpResponseBadRequest("User does not exist.")

        resume = Resume()
        resume.user = user
        resume.resume = request.FILES['resume']
        try:
            resume.save()
        except:
            return HttpResponseServerError("Could not save resume.")
        return HttpResponse("Successfully uploaded resume!")
