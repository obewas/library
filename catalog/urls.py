from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'index',views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^mybooks/$',views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^signup/$', views.signup, name='signup'),

]