from django.conf.urls import url
from beer.views import BeerView, WhiskeyView

urlpatterns = [
    url(r'^beer/$', BeerView.as_view(), name='beer-post'),
    url(r'^beer/(?P<pk>.*)/$', BeerView.as_view(), name='beer-get'),
    url(r'^whiskey', WhiskeyView.as_view(), name='whiskey-post-get-views')
]

beer_api_urls = urlpatterns
