import os
from pprint import pprint

from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from megano import settings
from .models import *
from products.models import Image

User = get_user_model()


def signIn(request):
    if request.method == "POST":
        body = json.loads(request.body)

        username = body['username']
        password = body['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=500)


def signUp(request):
    if request.method == "POST":
        body = json.loads(request.body)

        username = body['username']
        password = body['password']

        if not User.objects.filter(username=username):
            User.objects.create_user(username=username, password=password)
            UserInfo.objects.create(user_id=User.objects.filter(username=username)[0].id)

            user = authenticate(request, username=username, password=password)
            login(request, user)

            return HttpResponse(status=200)
        else:
            return HttpResponse(status=500)


def signOut(request):
    logout(request)
    return HttpResponse(status=200)


def profile(request):
    if request.method == 'GET':
        data = model_to_dict(UserInfo.objects.get(user=request.user))
        data['avatar'] = model_to_dict(Image.objects.get(id=data['avatar']))

        return JsonResponse(data)

    elif request.method == 'POST':
        data = json.loads(request.body)
        UserInfo.objects.filter(user=request.user).update(**data)

        return JsonResponse(data)

    return HttpResponse(status=500)


def profilePassword(request):

    return HttpResponse(status=200)


def profileAvatar(request):
    avatar = request.FILES['avatar']

    path = default_storage.save(avatar.name, ContentFile(avatar.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path).replace("\\", '/')
    ind = tmp_file.find('/static/')
    tmp_file = tmp_file[ind:]

    UserInfo.objects.filter(user=request.user).update(
        avatar=Image.objects.create(src=tmp_file.replace("\\", '/'), alt='avatar'))

    return HttpResponse(status=200)
