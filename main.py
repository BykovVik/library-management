from book import add_book, remove_book, search_books, display_books, update_status

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: "))
            add_book(title, author, year)
        elif choice == '2':
            book_id = int(input("Введите ID книги для удаления: "))
            remove_book(book_id)
        elif choice == '3':
            query = input("Введите название, автора или год для поиска: ")
            results = search_books(query)
            if results:
                for book in results:
                    print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")
            else:
                print("Книги не найдены.")
        elif choice == '4':
            display_books()
        elif choice == '5':
            book_id = int(input("Введите ID книги для изменения статуса: "))
            status = input('Введите новый статус ("в наличии" или "выдана"): ')
            update_status(book_id, status)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()