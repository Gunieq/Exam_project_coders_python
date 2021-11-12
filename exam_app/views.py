from datetime import datetime

from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from .forms import AuctionAddForm, AddUserForm, LoginForm, UserListForm
from .models import Auction

User = get_user_model()


# View which allows to see all auction listed on the website
class AuctionListView(View):
    def get(self, request):
        auctions = Auction.objects.all
        ctx = {
            'auctions': auctions,
        }
        return render(request, 'auction_list.html', ctx)


# View which allows to add an auction
class AuctionAddView(View):
    def get(self, request):
        form = AuctionAddForm()
        ctx = {'form': form}
        return render(request, 'auction_add.html', ctx)

    def post(self, request):
        name = request.POST.get("name", )
        product = request.POST.get("product", )
        start_date = datetime.now()
        end_date = request.POST.get("end_date", )
        Auction.objects.create(name=name, product=product, start_date=start_date, end_date=end_date)
        return redirect("auctionlist")


# View which allows to add an user
class AddUserView(PermissionRequiredMixin, FormView):
    template_name = 'add_user.html'
    success_url = reverse_lazy('auction-list')
    form_class = AddUserForm
    permission_required = 'auth.add_user'

    def post(self, request, **kwargs):
        login1 = request.POST.get("login", )
        username = request.POST.get("username", )
        password = request.POST.get("name", )
        User.objects.create(login=login1, username=username, password=password)
        return render("udało sie")


# Login view
class LoginView(FormView):
    template_name = 'user_login.html'
    form_class = LoginForm
    success_url = reverse_lazy('auction-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, form.user)
        return response


def check_admin(self, user):
    return user.is_superuser


# View allowing to see all the users(admin only)

class UserListView(FormView):
    template_name = 'user_list.html'
    form_class = UserListForm
    success_url = reverse_lazy('user-list')

    @user_passes_test(check_admin)
    def get(self, request, **kwargs):
        users = User.objects.all
        ctx = {
            'users': users,
        }
        return render(request, 'user_list.html', ctx)
