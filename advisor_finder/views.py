from django.shortcuts import render
from django.shortcuts import HttpResponse


def sitemap(request):
    """
    View to render the xml sitemap.
    """
    return HttpResponse(open('sitemap.xml').read(), content_type='text/xml')


def robots(request):
    """
    View to render the robots.txt.
    """
    return HttpResponse(open('robots.txt').read(), content_type='text/plain')


def handler404(request, exception):
    """
    Error Handler 404 - Page Not Found
    """
    return render(request, "errors/404.html", status=404)


def handler500(request, exception=None):
    """
    Error Handler 500 - Server error
    """
    return render(request, "errors/500.html", status=500)
