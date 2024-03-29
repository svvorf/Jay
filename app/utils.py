import json
import os
from PIL import Image
from django.http import HttpResponse
from project import settings as _settings
from shutil import copyfile

media_root = _settings.MEDIA_ROOT


def compose_and_save_avatar(pk):
    img_path = media_root + 'avatars/' + str(pk)
    img = Image.open(img_path)

    small = 50
    medium = 200

    width, height = img.size
    ratio = width / height

    img.save(img_path + "_full.png", "PNG")

    if ratio < 1:
        new_small_size = (small * ratio, small)
        new_med_size = (medium * ratio, medium)
    else:
        new_small_size = (small, small * ratio)
        new_med_size = (medium, medium * ratio)

    img.thumbnail(new_med_size, Image.ANTIALIAS)
    img.save(img_path + '_med.png', "PNG")

    img.thumbnail(new_small_size, Image.ANTIALIAS)
    img.save(img_path + '_small.png', 'PNG')

    os.remove(img_path)


def create_avatar_placeholder(pk):
    copyfile(media_root + 'avatars/no_med.png', media_root + 'avatars/' + str(pk) + '_med.png')
    copyfile(media_root + 'avatars/no_small.png', media_root + 'avatars/' + str(pk) + '_small.png')



def json_response(obj):
    return HttpResponse(json.dumps(obj), content_type='application/json')
