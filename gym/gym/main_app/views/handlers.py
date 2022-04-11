from django.shortcuts import render


def error_404(request, exception):
    data = {'exception': exception}
    return render(request, 'errors/404.html', data)


def error_403(request, exception):
    data = {'exception': exception}
    return render(request, 'errors/403.html', data)


def error_401(request, exception):
    data = {'exception': exception}
    return render(request, 'errors/500.html', data)
