searched_book = input()
current_book = input()
checked_books = 0
is_not_found = False
while current_book != "No More Books":
    if current_book == searched_book:
        is_not_found = True
        break
    checked_books += 1
    current_book = input()
if is_not_found:
    print(f"You checked {checked_books} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {checked_books} books.")