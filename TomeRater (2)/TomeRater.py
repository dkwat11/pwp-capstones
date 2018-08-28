class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("{name}'s email has been updated.".format(name=self.name))

    def __repr__(self):
        return "User: {name}, email: {email}, books read: {books}.".format(name=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            print("This is the same person!")
        else:
            print("These two people are not the same!")

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        rating_list = []
        try:
            for rating in self.books.values():
                if rating != None:
                    rating_list.append(rating)
            return sum(rating_list) / len(rating_list)   
        except ZeroDivisionError:
            return 0

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new):
        self.isbn = new
        print("The ISBN of \"{title}\" has been updated.".format(title=self.title))

    def add_rating(self, rating):
        if rating != None:
            if 0 <= rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

    def __repr__(self):
        return "{title}, {isbn}".format(title=self.title, isbn=self.isbn)

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            print("This the the same book!")
        else:
            print("These two books are not the same!")

    def get_average_rating(self):
        return sum(self.ratings) / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a(n) {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        try:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        except KeyError:
            print("No user with email {email}!".format(email=email))

    def add_user(self, name, email, user_books=None):
        self.users[email] = User(name, email)
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def get_most_read_book(self):
        m_r_book = ""
        highest_value = -1
        for book, key in self.books.items():
            if key > highest_value:
                highest_value = key
                m_r_book = book
        return m_r_book
            
    def highest_rated_book(self):
        highest_value = -1
        h_r_book = ""
        for book in self.books.keys():
            if book.get_average_rating() > highest_value:
                highest_value = book.get_average_rating()
                h_r_book = book
        return h_r_book

    def most_positive_user(self):
        highest_value = -1
        m_p_user = ""
        for user in self.users.values():
            if user.get_average_rating() > highest_value:
                highest_value = user.get_average_rating()
                m_p_user = user
        return m_p_user

            
            
                
            
            
                











