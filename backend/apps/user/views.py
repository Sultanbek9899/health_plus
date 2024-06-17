from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from backend.apps.user.models import User
from backend.apps.user.forms import CustomUserCreationForm, UserPasswordChangeForm


# Create your views here.
class CustomLoginView(LoginView):
    model = User
    template_name = "login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('products_list_url')
        return reverse_lazy('products_list_url')


class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('products_list_url')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


@login_required
def change_password(request):
    if request.method == "POST":
        form = UserPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            return redirect("login")
        return render(request, "change_password.html", {"form": form})
    else:
        form = UserPasswordChangeForm(request.user)
        context = {
            "form": form
        }
        return render(request, "change_password.html", context)