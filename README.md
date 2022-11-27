# django_demo
django_demo

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

OneToOneField demo
```
(blueking) xiexianbin:django_demo xiexianbin$ python manage.py shell
>>> from account_application.models import Author, Book
>>> a1 = Author.objects.create(name="a1", address="addr1")
>>> a1.save()
>>> b1 = Book.objects.create(name="b1", author=a1)
>>> b1.save()
>>> b1
<Book: Book object>
>>> b1.author
<Author: Author object>
>>> b1.author.name
'a1'
>>> b1.author.address
'addr1'
>>> a1.book
<Book: Book object>
>>> a1.book.name
'b1'
>>> exit()
```