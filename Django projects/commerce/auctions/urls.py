from django.urls import path,include


from . import views

app_name = 'auctions'
urlpatterns = [
    path("",include('django.contrib.auth.urls')),
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("listings/<int:listing_id>", views.listing, name="listing"),
    path("listings/<int:listing_id>/close_auction", views.closeauction, name="closeauction"),
    path("listings/<int:listing_id>/bid",views.bid,name="bid"),
    path("listings/<int:listing_id>/comment",views.comment,name="comment"),
    path("listings/<int:listing_id>/addwatchlist",views.addwatchlist, name="addwatchlist"),
    path("makelistings",views.makelistings,name="makelistings"),
    path("watchlist",views.watchlist, name="watchlist"),
    path("watchlist/<int:listing_id>",views.removewatchlist, name="removewatchlist"),
    path("categories", views.categories,name="categories"),
    path("categories/<int:category_id>", views.category,name="category"),
]
