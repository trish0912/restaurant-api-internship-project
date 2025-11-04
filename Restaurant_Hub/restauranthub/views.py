from django.shortcuts import render

def page_not_found(request, exception):
    """Custom 404 error page"""
    return render(request, '404.html', status=404)
