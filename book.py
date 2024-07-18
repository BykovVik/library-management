import json
import os
from typing import List, Dict, Optional

# Path to the JSON file
DATA_FILE = 'library_data.json'

# Book data structure
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.id = self.generate_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = 'в наличии'
    
    def generate_id(self) -> int:
        existing_books = load_books()
        if not existing_books:
            return 1
        max_id = max(book['id'] for book in existing_books)
        return max_id + 1
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

# Load books from JSON file
def load_books() -> List[Dict]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)

# Save books to JSON file
def save_books(books: List[Dict]) -> None:
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

# Add a new book
def add_book(title: str, author: str, year: int) -> None:
    books = load_books()
    new_book = Book(title, author, year)
    books.append(new_book.to_dict())
    save_books(books)
    print(f'Книга "{title}" добавлена в библиотеку с ID {new_book.id}.')

# Remove a book by ID
def remove_book(book_id: int) -> None:
    books = load_books()
    updated_books = [book for book in books if book['id'] != book_id]
    if len(books) == len(updated_books):
        print(f'Книга с ID {book_id} не найдена.')
    else:
        save_books(updated_books)
        print(f'Книга с ID {book_id} удалена из библиотеки.')

# Search books by title, author or year
def search_books(query: str) -> List[Dict]:
    books = load_books()
    result = [book for book in books if query.lower() in book['title'].lower() or query.lower() in book['author'].lower() or str(book['year']) == query]
    return result

# Display all books
def display_books() -> None:
    books = load_books()
    if not books:
        print('В библиотеке нет книг.')
        return
    for book in books:
        print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")

# Update book status
def update_status(book_id: int, status: str) -> None:
    if status not in ['в наличии', 'выдана']:
        print('Недопустимый статус. Используйте "в наличии" или "выдана".')
        return
    books = load_books()
    for book in books:
        if book['id'] == book_id:
            book['status'] = status
            save_books(books)
            print(f'Статус книги с ID {book_id} обновлен на "{status}".')
            return
    print(f'Книга с ID {book_id} не найдена.')