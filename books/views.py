from django.shortcuts import render,redirect
from . import models
from books.models import Book
from books.models import review,Purcehase_history,Ratings
from books.forms import reviewForm
from user.models import UserAccount
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives
from category.models import Category
from django.db.models import Avg
from django.template.defaulttags import register
from django.shortcuts import render
from django.db.models import Q
# Create your views here.
def send_transaction_email(user, subject, template):
        message = render_to_string(template, {
            'user' : user,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

from django.db.models import Avg

def symbol_to_numeric(symbol):
    # Define a mapping between symbols and numeric values
    symbol_mapping = {
        '★☆☆☆☆': 1,
        '★★☆☆☆': 2,
        '★★★☆☆': 3,
        '★★★★☆': 4,
        '★★★★★': 5,
    }
    return symbol_mapping.get(symbol, 0)  # Return 0 for unknown symbols

def booksShow(request, brand_slug=None):
    data = Book.objects.all()

    if brand_slug is not None:
        brand_name = Category.objects.get(slug=brand_slug)
        data = Book.objects.filter(category=brand_name)

    # Retrieve average ratings for each book
    book_ratings = {}
    for book in data:
        # Retrieve all ratings for the book
        ratings = Ratings.objects.filter(Book=book)

        # Calculate the average numeric rating
        if ratings.exists():
            average_numeric_rating = sum(symbol_to_numeric(rating.rating) for rating in ratings) / len(ratings)
            book_ratings[book.id] = round(average_numeric_rating)
        else:
            book_ratings[book.id] = None
    allcategory = Category.objects.all()
    return render(request, 'books.html', {'data': data, 'Category': allcategory, 'ratings': book_ratings})

@register.filter
def get_item(dictionary, key):
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    return None
def ViewDetails(request, id):
    book = Book.objects.get(pk=id)
    comments = review.objects.all()

    if request.method == 'POST':
        comment_form = reviewForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = book
            comment.save()
    else:
        comment_form = reviewForm()
    if request.user.is_authenticated:
        is_borrowed = Purcehase_history.objects.filter(user=request.user, Book=book, isBorrowd=True).exists()
        return render(request, 'view_details.html', {'object': book, 'comment_form': comment_form, 'comment': comments, 'isBorrowed': is_borrowed})
    else:
        return render(request, 'view_details.html', {'object': book})


def borrow(request, id, userid):
    userid-=1
    print(userid)
    data = Book.objects.get(pk=id)
    account = UserAccount.objects.get(pk=userid)  # Assuming there's a specific account you want to use for testing
    quntity = data.quntity
    price = data.price
    balance = account.balance
    purchase_history=False

    if balance > price and quntity > 1:
        quntity -= 1
        balance -= price
        account.balance = balance

        data.quntity = quntity
        data.save()

        # Assuming you have a ForeignKey from Purcehase_history to Book called 'Book'
        purchase_history = Purcehase_history.objects.create(user=request.user, Book=data)
        account.save()

        messages.success(
            request,
            f'You have successfully borrowed a book'
        )

        send_transaction_email(request.user, "Book Borrwed Message", "bookBorwwed.html")
        return redirect('profile')
    else:
        messages.warning(
            request,
            f'Your balance is not enough to buy this book or the book is finished'
        )
        send_transaction_email(request.user, "Book Borrwed Message Faild", "bookbowedfaild.html")

    return render(request, 'view_details.html', {'object': data, 'isBorrwod': purchase_history})



def bookReturn(request, id,userid,buyid):
    print(userid)
    data = models.Book.objects.get(pk=id)
    account = UserAccount.objects.get(pk=1)
    quntity = data.quntity
    price = data.price
    balance = account.balance
    if balance > price:
        if quntity > 1:
            quntity +=1
            balance+=price
            account.balance = balance
            data.quntity = quntity
            account.save()
            data.save()
            deleteHistory = models.Purcehase_history.objects.get(id = buyid)
            deleteHistory.delete()
            send_transaction_email(request.user, "Book Return Message succefully", "bookreturn.html")
            return redirect('profile')
    else:
        messages.warning(
            request,
            f'Your balance is not enough to buy this book or the book is finished'
        )
        send_transaction_email(request.user, "Book Return Message Failled", "bookreturnfaild.html")
    return render(request,'ViewDetaisl.html', {'object': data})



# For search emplement 

# search_query = request.GET.get('search', '') 
        # if search_query: 
        #     data = data.filter( 
        #         Q(name__icontains=search_query) | Q( 
        #             description__icontains=search_query)| Q( 
        #             category__name__icontains=search_query) 
        #     )

def Search_Book_Fillter(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        data = Book.objects.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) | 
            Q(category__name__icontains=search_query)
        )
    else:
        data = Book.objects.all()

    return render(request, 'search_Book.html', {'data': data})