from django.core.management.base import BaseCommand, CommandError
from exam_app import models
from datetime import datetime

class Command(BaseCommand):
    help = 'Delete objects'

    def handle(self, *args, **options):
        models.Auction.objects.filter(end_date__lte=datetime.now()).delete()
        self.stdout.write('Deleted old auctions')
