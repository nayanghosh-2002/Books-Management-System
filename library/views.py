from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView #this is for the class view option
from .forms import BookForm

from .models import Book,Author

"""function based book details"""


def book_list(request):
    books=Book.objects.all()
    context={'books':books}
    return render(request,"library/book_list.html",context)

def book_detail(request,book_id):
    book=get_object_or_404(Book,id=book_id)
    context={'book':book}
    return render(request,"library/book_detail.html",context)

def book_by_author(request,author_id):
    author=get_object_or_404(Author,id=author_id)
    books=Book.objects.filter(author=author)
    context={'author':author,'books':books}
    return render(request,'library/book_by_author.html',context)

def add_book(request):
    if (request, method="POST"):
        form=BookForm(request,POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        else:
            form=BookForm()
        return render(request, 'library/add_book.html',{'form':form})


#class BookListView(ListView):
 #   model=Book
  #  template_name='library/book_list.html'
   # context_object_name='book'

#class BookDetailView(DetailView):
 #   model=Book
  #  template_name="library/book_detail.html"
   # context_object_name='book'