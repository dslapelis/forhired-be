from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from api.models import Job
from authentication.models import Company
from django.contrib.auth.models import User
import json


class JobView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return JsonResponse(list(Job.objects.all().values()), safe=False)

    def post(self, request):
        user = User.objects.get(username=request.user)
        try:
            company = Company.objects.get(user=user)
        except:
            return HttpResponseBadRequest("You're not authorized to post a job.")

        body = json.loads((request.body).decode('utf-8'))

        job = Job(name=body['name'],
                  description=body['description'], company=company)
        try:
            job.save()
        except:
            HttpResponseServerError(
                "Something went wrong and we couldn't save this job.")
        return JsonResponse({'success': 'true'})
