from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime

from .forms import AuctionAddForm
from .models import Auction

User = get_user_model()


class AuctionListView(View):
    def get(self, request):
        auctions = Auction.objects.all
        ctx = {
            'auctions': auctions,
        }
        return render(request, 'auction_list.html', ctx)


class AuctionAddView(View):
    def get(self, request):
        form = AuctionAddForm()
        ctx = {'form': form}
        return render(request, 'auction_add.html', ctx)

    def post(self, request):
        name = request.POST.get("name")
        product = request.POST.get("product")
        start_date = datetime.now()
        end_date = request.POST.get("end_date")
        Auction.objects.create(name=name, product=product, start_date=start_date, end_date=end_date)
        return redirect("auctionlist")
