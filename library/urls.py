from django.urls import path
from .import views

#from .views import BookDetailView, BookListView

urlpatterns=[
    path("books/",views.book_list,name='book_list'),
    path("book/<str:book_id>/",views.book_detail,name='book_detail'),
    path("author/<str:author_id>/book",views.book_by_author,name='book_by_author'),
    path("books/add/",views.add_book,name='add_book'),

    # path("book/",BookListView.as_view(),name='book-list'),
    # path("book//",BookDetailView.as_view(),name='book_detail'),
]