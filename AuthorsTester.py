#Cesar Neri
#December 18, 2016

#Authors Tester

#Use of the __iter__(), __str(), and __next__()



#!/usr/bin/env python3


from objectsA import Book, Author, Authors

def main():
    print("The Authors Tester program")
    print()
    
    author1 = Author("Mark", "Twain")
    author2 = Author("Charles", "Warner")
    authors = Authors()
    authors.add(author1)
    authors.add(author2)
    book = Book("The Gilded Age", authors)

    # display the book data
    print("BOOK DATA - SINGLE LINE")
    print(book)
    print()

    print("BOOK DATA - MUTLIPLE LINES")
    print("Title:   ", book.title)

    #check using the count property
    if book.authors.count > 1: 
        print("Authors: ",  book.authors)
    else:
        print("Author: ",  book.authors)

    #test iterator to print each author
    print("\nAUTHORS")
    for author in authors:
        print(author)
        
if __name__ == "__main__":
    main()
