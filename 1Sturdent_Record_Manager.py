import json
import os

class Books():
    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages
    
    def Shows_info(self): #It will shows Books Informations
        print(f"Book's Title: {self.title}")
        print(f"Book's Author: {self.author}")
        print(f"Book's Total Pages Numeber: {self.pages}")

class My_Library():
    def __init__(self):

        self.books = []

    def Add_New_Books(self, Book):
        self.books.append(Book)
        with open("My_library_data.json", "w") as file:
            json.dump([{"title": s.title, "author": s.author, "pages": s.pages} for s in self.books], file, indent= 1)

    def View_all_Books(self):
        if os.path.exists("My_library_data.json"):
            with open("My_library_data.json", "r") as file:
                data = json.load(file)
                for i, items in enumerate(data, start= 1):
                    print(f"BOOK NO. {i}")
                    print(f"Book's Title: {items['title']}")
                    print(f"Book's Author: {items['author']}")
                    print(f"Book's Total Page Number: {items['pages']}")
    

    def Search_Book(self, search_term):
        if os.path.exists("My_library_data.json"):
            with open("My_library_data.json", "r") as file:
                Book_s = json.load(file)
                result = []

                for Book in Book_s:
                    if search_term.lower() in Book["title"].lower():
                        result.append(Book)

                if result:
                    print("Matches Found:-")
                    for i, books in enumerate(result, start= 1):
                        print(f"\n Match Found No.{i}")
                        print(f"Book's Title: {books["title"]}")
                        print(f"Book's Author: {books["author"]}")
                        print(f"Book's Total Page Numbers: {books["pages"]}")
                else:
                    print("No Match Found")

        else:
            print("No Book Found!")

Library = My_Library()

def My_menu():
    print("\n_____WELCOME TO THE LIBRARY_____")
    print("1. For Adding a New Book to Library")
    print("2. For Viewing All the Books in the Library")
    print("3. For Checking the Book's Name Available or Not")
    print("4. For Updating the Book's Details")
    print("5. For Deleting the Books")
    print("6. For Exiting")

while True:
    My_menu()
    try:
        user_input = int(input("\nEnter: "))  

    except ValueError:
        pass

    if user_input == 1:
        try:
            user_1 = input("Enter the Book's Title: ")
            user_2 = input("Enter the Book' Author Name: ")
            user_3 = int(input("Enter the Total Pages Number of Book: "))
        except ValueError:
            pass
        New_Book = Books(user_1, user_2, user_3)
        Library.Add_New_Books(New_Book)
        print("New Books Added Sucessfully!")
    
    elif user_input == 2:
        print("\nAll Books:-")
        Library.View_all_Books()

    elif user_input == 3:
        user_search = input("Enter Your Book's Title: ")
        with open("My_library_data.json", "r") as file:
            data = json.load(file)
            found = False
            for item in data:
                if user_search.lower():
                    found = True
                    break
            if found:
                print("Yes,This Books is present in the Library")
            else:
                print("No, This Books is not present in the Library")

    elif user_input == 4:
                
        def update():
            print("\nWhat do you want to update")
            print("1.Book's Title")
            print("2.Book's Author Name")
            print("3.Book's Total Page Number")

        update()
        
        try:
            user_4 = int(input("Enter, What do you Want to Update: "))
        except ValueError:
            print("Enter Valid Options")
            user_4 = None
        
        if user_4 == 1:
            if os.path.exists("My_library_data.json"):
                with open("My_library_data.json", "r") as file:
                    content = json.load(file)
                    for i, titles in enumerate(content, start=1):
                        print(f"{i}. {titles}")


            user_4_in = input("Enter the Book's Title which you want to update: ")
            user_t_name = input("Now Enter Book's Updated Title: ")
            if os.path.exists("My_library_data.json"):
                with open("My_library_data.json", "r") as file:
                    book_data = json.load(file)

                    found = False
                    for books in book_data:
                        if books["title"].lower() == user_4_in.lower():
                            books["title"] = user_t_name
                            found = True
                    if found:
                        with open("My_library_data.json", "w") as file:
                            json.dump(book_data, file, indent = 1)
                        print("Book Title Updated Sucessfully!")
                    else:
                        print("No Book Found by these title")
            else:
                print("No Book Found")
    
        elif user_4 == 2:
            if os.path.exists("My_library_data.json"):
                with open("My_library_data.json", "r") as file:
                    content = json.load(file)
                    for i, titles in enumerate(content, start=1):
                        print(f"{i}. {titles}")
            user_4_an = input("Enter the Book's Title which you want to update: ")
            user_4_can = input("Now Enter the Book's Updated Author Name: ")
            if os.path.exists("My_library_data.json"):
                with open("My_library_data.json", "r") as file:
                    book_data = json.load(file)   

                    found = False
                    for books in book_data:
                        if books["author"].lower() == user_4_an.lower():
                            books["author"] = user_4_can
                            found = True
                    if found:
                        with open("My_library_data.json", "w") as file:
                            json.dump(book_data, file, indent = 1)
                        print("Book Title Updated Sucessfully!")
                    
                    else:
                        print("No Book Found by these title")             
            
            else:
                print("No Book Found")

                
        elif user_4 == 3:
            if os.path.exists("My_library_data.json"):
                with open("My_library_data.json", "r") as file:
                    content = json.load(file)
                    for i, titles in enumerate(content, start=1):
                        print(f"{i}. {titles}")
            user_4_an = input("Enter the Book's Title which you want to update: ").capitalize()
            user_4pn = int(input("Enter The Page Number for updating: "))
            if os.path.exists("My_library_data.json"):
                with open("My_library_data.json", "r") as file:
                    book_data = json.load(file)  

                    found = False
                    for books in book_data:
                        if books["title"].lower() == user_4_an.lower():
                            books["pages"] = user_4pn
                            found = True
                    if found:
                        with open("My_library_data.json", "w") as file:
                            json.dump(book_data, file, indent = 1)
                        print("Book Title Updated Sucessfully!")
                    else:
                        print("No Book Found by these title")

            else:
                print("No Books Found")        

    elif user_input == 5:
        def delete_menu():
            print("If you want to delete all,So Enter \'Yes\' if no so \'No\' ").lower()

        delete_menu()

        user_1 = input("Enter: ")
        if user_1 == "no":
            if os.path.exists("My_library_data.json"):
                with open("My_library_data.json", "r") as file:
                    data = json.load(file)
                    print(data)
                user_inde = input("Enter the Book's Title to Delete: ")
                new_data = [student for student in data if student["title"] != user_inde]
                with open("My_library_data.json", "w") as file:
                    json.dump(new_data, file, indent = 1)
                print("Book Deleted From the Library")
            else:
                print("No Books Found in the Library")

        elif user_1 == "yes":
            if os.path.exists("My_library_data.json"):
                with open("My_library_data.json", "w") as file:
                    json.dump([],file, indent =1)
                print("All Books Deleted")
            else:
                print("No Books found.")
        else:
            print("Invalid Input.")
                    

    elif user_input == 6:
        print("GoodBye!")
        break

    else:
        print("Invalid Input")



                        


                
            
        
            


    


