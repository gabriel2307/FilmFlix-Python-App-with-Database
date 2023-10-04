import sqlite3

# Connect to the SQLite database or create it if it doesn't exist
conn = sqlite3.connect("filmflix.db")
cursor = conn.cursor()

def print_menu():
    print("Options Menu:")
    print("1. Add a record")
    print("2. Delete a record")
    print("3. Amend a record")
    print("4. Print all records")
    print("5. Exit")

def print_report_menu():
    print("Report Menu:")
    print("1. Print details of all films")
    print("2. Print all films of a particular genre")
    print("3. Print all films of a particular year")
    print("4. Print all films of a particular rating")
    print("5. Exit")


def add_record():
    title = input("Enter film title: ")
    year_released = input("Enter year released: ")
    rating = input("Enter rating: ")
    duration = input("Enter duration: ")
    genre = input("Enter genre: ")

    cursor.execute('''INSERT INTO tblfilms (title, yearReleased, rating, duration, genre)
                      VALUES (?, ?, ?, ?, ?)''', (title, year_released, rating, duration, genre))
    conn.commit()
    print("Record added successfully!")


def delete_record():
    film_id = input("Enter filmID to delete: ")
    cursor.execute("DELETE FROM tblfilms WHERE filmID=?", (film_id,))
    conn.commit()
    print("Record deleted successfully!")


def amend_record():
    film_id = input("Enter filmID to amend: ")
    title = input("Enter new title: ")
    year_released = input("Enter new year released: ")
    rating = input("Enter new rating: ")
    duration = input("Enter new duration: ")
    genre = input("Enter new genre: ")

    cursor.execute('''UPDATE tblfilms
                      SET title=?, yearReleased=?, rating=?, duration=?, genre=?
                      WHERE filmID=?''', (title, year_released, rating, duration, genre, film_id))
    conn.commit()
    print("Record amended successfully!")


def print_all_records():
    cursor.execute("SELECT * FROM tblfilms")
    records = cursor.fetchall()
    if records:
        print("\nAll Records:")
        for record in records:
            print(record)
    else:
        print("No records found!")


def print_all_films_by_genre():
    genre = input("Enter genre to filter: ")
    cursor.execute("SELECT * FROM tblfilms WHERE genre=?", (genre,))
    records = cursor.fetchall()
    if records:
        print("\nFilms of Genre:", genre)
        for record in records:
            print(record)
    else:
        print(f"No films found for genre: {genre}")


def print_all_films_by_year():
    year = input("Enter year to filter: ")
    cursor.execute("SELECT * FROM tblfilms WHERE yearReleased=?", (year,))
    records = cursor.fetchall()
    if records:
        print("\nFilms Released in Year:", year)
        for record in records:
            print(record)
    else:
        print(f"No films found for year: {year}")


def print_all_films_by_rating():
    rating = input("Enter rating to filter: ")
    cursor.execute("SELECT * FROM tblfilms WHERE rating=?", (rating,))
    records = cursor.fetchall()
    if records:
        print("\nFilms with Rating:", rating)
        for record in records:
            print(record)
    else:
        print(f"No films found for rating: {rating}")


while True:
    print("\nMain Options:")
    print("1. CRUD")
    print("2. Report")
    print("3. Exit")
    main_option = input("Enter your choice (1/2/3): ")


    if main_option == '1':  # CRUD
        while True:
            print_menu()
            choice = input("Enter your choice (1/2/3/4/5): ")
            if choice == '1':
                add_record()
            elif choice == '2':
                delete_record()
            elif choice == '3':
                amend_record()
            elif choice == '4':
                print_all_records()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Try again.")

        
    elif main_option == '2':  # Report
        while True:
            print_report_menu()
            choice = input("Enter your choice (1/2/3/4/5): ")
            if choice == '1':
                print_all_records()
            elif choice == '2':
                print_all_films_by_genre()
            elif choice == '3':
                print_all_films_by_year()
            elif choice == '4':
                print_all_films_by_rating()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Try again.")


    elif main_option == '3':  # Exit
        break
    else:
        print("Invalid choice. Try again.")

# Close the database connection when done
conn.close()