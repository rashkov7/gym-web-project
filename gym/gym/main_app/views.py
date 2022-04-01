from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import CreateView

UserModel = get_user_model()

def index_test(request):
    context = {'is_true': True}
    return render(request, 'index.html', context)

