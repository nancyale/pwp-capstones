class User():

  def __init__(self, name, email):

    self.name=str(name)

    self.email=str(email)

    self.books={}

 

  def get_email(self):

    return self.email

 

  def change_email(self, address):

    if self.email != address:

      self.email=address

      return "This user's name has been updated to: {address}".format(address=address)

    else:

      return "Email address remains the same"

 

  def __repr__(self):

    return "User {name} , email {email} , books read : {books}.".format(name=self.name, email=self.email, books=self.books)

 

  def __eq__(self, name, email):

    self.other_user=other_user

 

    for person in self.name:

      if person==self.other_user and self.email==other_user:

        return "Welcome back {name}!".format(name=self.name)

      else:

        return "Welcome {name}!".format(name=self.name)

     

  def read_book(self, book, rating=None):

    self.book=book

    if rating:

      self.books[book]=rating

 

  def get_average_rating(self):

    suma=0

    for value in self.books.items():

      suma+=value

    return suma / len(self.books)

 

#******************************************

UserNancy=User("Nancy Luque Osuji", "nancyale@yahoo.com")

NewMailNancy=UserNancy.change_email("nluque@wnpl.info")

SameMailNancy=UserNancy.change_email("nluque@wnpl.info")

 

#print(UserNancy.__eq__("nluque@wnpl.info"))

#print(UserNancy)

#print (NewMailNancy)

#print (SameMailNancy)

#******************************************

 

class Book():

  def __init__(self, title, isbn):

    self.title=str(title)

    self.isbn=int(isbn)

    self.ratings=[]

 

  def get_title(self):

    return self.title

 

  def get_isbn(self):

    return self.isbn

 

  def set_isbn(self, new_isbn):

    self.new_isbn=int(new_isbn)

   

    if self.isbn != new_isbn:

      self.isbn=new_isbn

      return ("This book's ISBN has been updated to: {new_isbn}:".format(new_isbn=self.new_isbn))

    else:

      return "ISBN already on record."

   

  def add_rating(self, rating):

    self.rating=int(rating)

   

    if rating >= 0 and rating <= 4:

      self.ratings.append(rating)

    else:

      return "Invalid rating"

   

  def __eq__(self, comp_title, comp_isbn):

    self.comp_title=str(comp_title)

    self.comp_isbn=int(comp_isbn)

 

    for tit in self.comp_title:

     if tit != self.title:

      return "New book"

     else:

       for num in self.comp_isbn:

         if num == self.isbn:

          return "Already registered book!"

         else:

           return "New edition"

     

  def __repr__(self):

    return "Title: {title}, ISBN {isbn}.".format(title=self.title, isbn=self.isbn)

 

  def get_average_rating(self):

    suma=0

    for valor in self.ratings:

      suma+=valor

    return suma / len(self.ratings)

 

  def __hash__(self):

    return hash((self.title, self.isbn))

 

#******************************************

#Ove1=Book("A man called Ove", 9781476738017)

#Ove2=Book("A man called Ove", 9781476738024)

#Ove3=Book("A man called Ove", 9781476738024)

 

#Beartown=Book("Beartown", 9781501160769)

 

#print(Ove1)

#print(Ove1.__eq__("A man called Ove", 9781476738024))

#print(Ove2.__eq__("A man called Ove", 9781476738024))

 

#******************************************

class Fiction (Book):

  def __init__(self, title, author, isbn):

    super().__init__(title, isbn)

    self.author=author

   

  def get_author(self, author):

    return self.author

 

  def __repr__(self):

    return "{title} by {author}; ISBN {isbn}.".format(title=self.title, author=self.author, isbn=self.isbn)

 

#******************************************

 

class NonFiction(Book):

  def __init__(self, title, subject, level, isbn):

    super().__init__(title, isbn)

    self.subject=str(subject)

    self.level=str(level)

   

  def get_subject(self, subject):

    return self.subject

 

  def get_level(self, level):

    return self.level

 

  def __repr__(self):

    return "{title}, a {level} manual on {subject}; ISBN {isbn}.".format(title=self.title, level=self.level, subject=self.subject, isbn=self.isbn)

 

 

#******************************************

class Tome_Rater:

  def __init__(self):

    self.users={}#empty dictionary that will map a user's email to the corresponding User object

    self.books={}#empty dictionary that will map a Book object to the number of users that have read it

 

  def create_book (self, title, isbn):
 
    self.title=title
    self.isbn=isbn

    self.books[self.title, self.isbn]=1
    
    new_book=Book([self.title])
    return new_book
   
 
  def create_novel(title, author, isbn):
      
    self.title=title
    self.author=author
    self.isbn=isbn
    
    new_fiction=Fiction(new_fiction)

    self.books[title, author, isbn]=1

    return new_fiction

 

  def create_non_fiction(title, subject, level, isbn):
      
    self.title=title
    self.subject=subject
    self.level=level
    self.isbn=isbn

    self.books[title, subject, level, isbn]=1
    
    new_non_fiction=NonFiction()
    return NonFiction(new_non_fiction)

 

           

  def add_book_to_user(self, book, email, rating=None):

 

    if not self.users[email]:         

        print("No user with email {email}!?".format(email=self.email))

    else:

      email.read_book(book, rating) #call read_book on the user, with book and rating

      #add_rating on book, with rating:

      book.add_rating(book, rating)

      

      if rating:

       self.rating=rating
       email.add_rating(rating)
       

      if not self.books[book]: #why [book]? Because it refers to the key.

        self.books[book] = 1

      else:

        self.books[book] += 1

 

  def add_user(name, email, user_books=None):

    this_user = User(name, email)

    if user_books:

      for book in user_books:

        add_book_to_user(self.book, self.email, self.rating)

    return this_user

       

  def print_catalog(self):

    for a, b in self.books.items():

      return self.a + "***" + self.b

 

  def print_users(self):

    for usuarios, correo in self.users.items():

      return "User Name: " + self.usuarios + "Email: " + self.correo

 

  def most_read_book(self):

    most_read={}

    for read, num in self.books.items():

      if self.num > most_read.values():

        most_read.clear()

        most_read[self.read]= self.num

        return most_read

       

  def highest_rated_book(self): #return the book with highest average rating

    bk_hi_ratings={}

    for bk, rat in self.books.items(): #books are keys and ratings are values

      bk_hi_rating[bk]=rat.get_average_rating 

      if bk > bk_avg_ratings.values:

        bk_ratings.clear()

        bk_ratings[bk]=rat          

    return "Highest rated book: {book}, rated at {rating}.".format(book=bk_hi_ratings.keys(), rating=bk_hi_ratings.values())

 

  def most_positive_user(self): #return the user that has the highest average rating

    user_rating={}

    for usuario in self.users: #(book, email, rating)

      user_rating[email]=email.get_average_rating

    sorted = sorted((value, key) for (key,value) in user_rating.items())
    
    return list(user_rating.keys())[0]
    #return max([i for i in user_rating.values()])
      


      

      

#Create some books:

book1 = Tome_Rater.create_book("Society of Mind", 12345678)

#novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)

#novel1.set_isbn(9781536831139)

#nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)

#nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)

#novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)

#novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

print (book1)

 

#Create users:

#one=Tome_Rater.add_user("Alan Turing", "alan@turing.com")

#print(one)

#Tome_Rater.add_user("David Marr", "david@computation.org")

 

#Add a user with three books already read:

#two=Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#print(two)

#Add books to a user one by one, with ratings:

#Tome_Rater.add_book_to_user("book1", "alan@turing.com", 1)

#Tome_Rater.add_book_to_user("novel1", "alan@turing.com", 3)

#Tome_Rater.add_book_to_user("nonfiction1", "alan@turing.com", 3)

#Tome_Rater.add_book_to_user("nonfiction2", "alan@turing.com", 4)

#Tome_Rater.add_book_to_user("novel3", "alan@turing.com", 1)

 

#Tome_Rater.add_book_to_user("novel2", "marvin@mit.edu", 2)

#Tome_Rater.add_book_to_user("novel3", "marvin@mit.edu", 2)

#Tome_Rater.add_book_to_user("novel3", "david@computation.org", 4)

 

 

#Uncomment these to test your functions:

#Tome_Rater.print_catalog()

#Tome_Rater.print_users()

 

# print("Most positive user:")

# print(Tome_Rater.most_positive_user())

#print("Highest rated book:")

#print(Tome_Rater.highest_rated_book())

#print("Most read book:")

#print(Tome_Rater.get_most_read_book())
