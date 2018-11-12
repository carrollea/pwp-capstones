class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("This user's email has been updated")

    def __repr__(self):
        return "User {name}, email: {email}, books read: {books}".format(name=self.name, email=self.email, books = len(self.books))

    def __eq__(self, other_user):
        return(self.name == other_user.name and self.email == other_user.email)

    def read_book(self, book, rating =0):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        number = 0
        for val in self.books.values():
            total += val
            number += 1
        rating_average = total/number
        return rating_average

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("This book's ISBN has been updated.")

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.rating = []
            self.rating.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            self == other_book
        else:
            self != other_book

    def get_average_rating(self):
        total = 0
        for rating in self.rating:
            total += rating
        return total/len(self.rating)

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        self.title = title
        self.isbn = isbn
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        self.title = title
        self.isbn = isbn
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)


class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = 0):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with email {}".format(email=email))


    def add_user(self, name, email, user_books = []):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print book

    def print_users(self):
        for user in self.users.values():
            print user

    def get_most_read_book(self):
        for book in self.books.keys():
            if self.books.get(book) == max(list(self.books.values())):
                return book

    def highest_rated_book(self):
        ratings = []
        for book in self.books.keys():
            ratings.append(book.get_average_rating())
        for book in self.books.keys():
            if self.books.get(book) == max(ratings):
                return book

    def most_positive_user(self):
        rating = []
        for user in self.users.values():
            rating.append(user.get_average_rating())
        for user in self.users.values():
            if user.get_average_rating() == max(rating):
                return user




