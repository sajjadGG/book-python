from django.shortcuts import render

def edit_profile(request):
    if not request.user.is_authenticated:
        return render(request, 'myapp/login_error.html')
    else:
        return render(request, 'myapp/edit-profile.html')



from django.contrib.auth.decorators import login_required


@login_required
def edit_profile(request):
    return render(request, 'myapp/edit_profile.html')


@login_required(login_url='/accounts/login/')
def edit_product(request):
    return render(request, 'myapp/edit_product.html')





from django.contrib.auth.mixins import LoginRequiredMixin


class EditProductView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'myapp/edit_product.html'