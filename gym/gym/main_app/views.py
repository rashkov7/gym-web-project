from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from gym.main_app.models import GymInfoModel, StarCoach
from gym.profile_app.models import ProfileModel

UserModel = get_user_model()


def index_test(request):
    a = ProfileModel.objects.filter(user__trainer=True)
    exist_gym_info = GymInfoModel.objects.exists()
    if not exist_gym_info:
        new_in = GymInfoModel.objects.create(h1='Update web site info !')
    context = {'is_true': "Abra kadabra"}
    return render(request, 'index.html', context)


class CoachListView(ListView):
    model = ProfileModel
    template_name = 'coaches-list.html'
    paginate_by = 3

    def get_queryset(self):
        if self.queryset is None:
            if self.model:
                return self.model._default_manager.filter(user__trainer=True)
            else:
                raise ImproperlyConfigured(
                    "%(cls)s is missing a QuerySet. Define "
                    "%(cls)s.model, %(cls)s.queryset, or override "
                    "%(cls)s.get_queryset()." % {
                        'cls': self.__class__.__name__
                    }
                )
        return self.queryset.all()


def star_coach(request, pk):
    coach = get_object_or_404(ProfileModel, pk=pk)
    user = request.user
    star = StarCoach.objects.filter(owner__user_id=pk)
    if star:
        star.delete()
    else:
        StarCoach.objects.create(owner=coach, sender=user)
    return redirect('trainers')
