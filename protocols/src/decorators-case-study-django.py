from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def edit_profile(request):
    """
    Function checks whether user is_authenticated
    If not, user will be redirected to login page
    """
    if not request.user.is_authenticated:
        return render(request, 'templates/login_error.html')
    else:
        return render(request, 'templates/edit-profile.html')


@login_required
def edit_profile(request):
    """
    Decorator checks whether user is_authenticated
    If not, user will be redirected to login page
    """
    return render(request, 'templates/edit-profile.html')
