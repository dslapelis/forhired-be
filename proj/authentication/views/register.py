from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from authentication.models import Candidate, Company
from sqlite3 import IntegrityError
import json


@csrf_exempt
@require_http_methods(["POST"])
def register_candidate(request):
    try:
        body = json.loads((request.body).decode('utf-8'))
    except:
        HttpResponseBadRequest(json.dumps(
            {'success': 'false', 'msg': 'Request format error'}))

    user = User.objects.create_user(
        body['email'], body['email'], body['password'], first_name=body['first'], last_name=body['last'])
    try:
        user.save()
    except IntegrityError:
        return HttpResponseBadRequest(json.dumps({'success': 'false', 'msg': 'User with this email already exists.'}))

    candidate = Candidate(user=user)
    candidate.save()

    return HttpResponse(json.dumps({'success': 'true'}))


def register_company(request):
    body = json.loads((request.body).decode('utf-8'))
    print(body)

    user = User.objects.create_user(
        body['email'], body['email'], body['password'], first_name=body['first'], last_name=body['last'])
    user.save()

    company = Company(user=user)
    company.save()

    return HttpResponse(json.dumps({'success': 'true'}))
