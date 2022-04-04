from django.contrib.auth import get_user_model
from django.shortcuts import render

from gym.main_app.models import GymInfoModel

UserModel = get_user_model()


def index_test(request):
    exist_gym_info = GymInfoModel.objects.exists()
    if not exist_gym_info:
        new_in = GymInfoModel.objects.create(h1='Update web site info !')
    context = {'is_true': "Abra kadabra"}
    return render(request, 'camps-list.html', context)
