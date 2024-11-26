books = {
    "sci-fi":
        {
            "book": 1
        }
}

options = {
    "1": "Add a book",
    "2": "Browse the library",
    "q": "Quit"
}

print("Please choose one of the following options:")

while True:
    for num, option in options.items():
        print(f"[{num}] {option} ", end="")

    option = None
    while option not in options:
        option = input(": ").lower()
        if option not in options.keys():
            print("Please enter a valid option")

    print()

    if option == "1":
        title = input("Please enter the name of the book: ").strip().lower()
        genre = input("Please enter the genre of the book: ").strip().lower()
        print()
        books.setdefault(genre, {}).setdefault(title, 0)
        books[genre][title] += 1

    if option == "2":
        title_width = 40
        quantity_width = 15
        for genre, titles in books.items():
            print(f"{genre.capitalize():^{title_width + quantity_width}}")

            print(f"{'+':-<{title_width}}{'+':-<{quantity_width}}+")
            print(f"{"| Title":<{title_width}}{"| Quantity":<{quantity_width}}|")
            print(f"{'+':-<{title_width}}{'+':-<{quantity_width}}+")

            for title, quantity in titles.items():
                print(f"{("| " + title.capitalize()):<{title_width}}{("| " + str(quantity).capitalize()):<{quantity_width}}|")

            print(f"{'+':-<{title_width}}{'+':-<{quantity_width}}+\n")
            
    if option == "q":
        break