from django.contrib import admin

# Register your models here.
from abids.models import Auction, Competitor

class AuctionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'pub_date', 'owner', 'ip')
    list_display_links = ('id', 'title')
    list_filter = ('pub_date', 'owner')
    search_fields = ['id', 'title', 'desc']

class CompetitorAdmin(admin.ModelAdmin):
    list_display = ('auction', 'bid', 'bid_owner', 'bid_comment', 'bid_ip')
    list_filter = ('auction__id', 'bid_owner', 'auction', 'pub_date')
    search_fields = ['auction__id', 'auction__owner']


    def auction_id(self, instance):
        return instance.auction.owner

admin.site.register(Auction, AuctionAdmin)
admin.site.register(Competitor, CompetitorAdmin)
