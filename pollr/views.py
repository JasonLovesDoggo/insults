from django.shortcuts import render


def handler404(request, exception):
    context = {}
    response = render(request, "../static/error-pages/404.html", context=context)
    response.status_code = 404
    return response


def home(request):
    return render(request,'home.html')