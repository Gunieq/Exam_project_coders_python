from datetime import datetime

from django.contrib.auth import get_user_model, login
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView

from .forms import AuctionAddForm, AddUserForm, LoginForm, UserListForm
from .models import Auction, Product

User = get_user_model()


# View which allows to see all auction listed on the website
class AuctionListView(View):
    def get(self, request, *args, **kwargs):
        auctions = Auction.objects.all
        ctx = {
            'auctions': auctions,
        }
        return render(request, 'auction_list.html', ctx)


# View which shows auction details
class AuctionView(View):
    def get(self, request, *args, **kwargs):
        auction_id = kwargs['auction_id']
        auction = get_object_or_404(Auction, pk=auction_id)
        product = Product.objects.filter(auction_id=auction)
        ctx = {
            'auction': auction,
            'product': product
        }
        return render(request, 'auction.html', ctx)


# View which allows to add an auction
class AuctionAddView(View):
    def get(self, request):
        form = AuctionAddForm()
        ctx = {'form': form}
        return render(request, 'auction_add.html', ctx)

    def post(self, request, **kwargs):
        name = request.POST.get("name", )
        start_date = datetime.now()
        end_date = request.POST.get("end_date", )
        prod_desc = request.POST.get("prod_desc", )
        cat_name = request.POST.get('cat_name', )
        new_auction = Auction.objects.create(name=name, start_date=start_date, end_date=end_date)

        # new_product = Product.objects.create(auction_id=new_auction.pk, description=prod_desc, category_id=category.pk)
        ctx = {
            'category': cat_name,
            'new_auction': new_auction
        }
        return redirect(reverse('auction-view', kwargs={'auction_id': new_auction.pk}))


# View which allows to add an user
class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        ctx = {'form': form}
        return render(request, 'add_user.html', ctx)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        User.objects.create(username=username, password=password)
        return redirect("user-list")

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
    form_class = UserListForm()
    success_url = reverse_lazy('user-list')

    def get(self, request, **kwargs):
        users = User.objects.all
        ctx = {
            'users': users,
        }
        return render(request, 'user_list.html', ctx)


class UserView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs['user_id']
        user = get_object_or_404(User, pk=user_id)
        return render(request, 'user.html', {'user': user, 'auctions': Auction.objects.filter(user_id=user.pk)})


class DeleteAuctionView(View):
    def get(self, request, **kwargs):
        auction_id = kwargs['auction_id']
        auction = Auction.objects.get(id=auction_id)
        auction.delete()
        return HttpResponse('udaosie')
