from django.shortcuts import render

from core.seo import page_context


def page_not_found(request, exception):
    context = page_context(
        "Page Not Found | GyLo Softwares",
        "The page you are looking for could not be found.",
        request.path,
    )
    return render(request, "404.html", context, status=404)


def server_error(request):
    context = page_context(
        "Server Error | GyLo Softwares",
        "Something went wrong while loading this page.",
        request.path,
    )
    return render(request, "500.html", context, status=500)
