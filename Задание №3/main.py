# Программа для объединения текстовыъ файлов в 1
with open('1.txt', 'r', encoding='UTF-8') as f:
    f = list(f)
    book1 = ['1.txt', len(f)]
book1 += f

with open('2.txt', 'r', encoding='UTF-8') as f:
    f = list(f)
    book2 = ['2.txt', len(f)]
book2 += f

with open('3.txt', 'r', encoding='UTF-8') as f:
    f = list(f)
    book3 = ['3.txt', len(f)]
book3 += f

all_books = [book1, book2, book3]
all_books.sort(key=lambda book: book[1])
print(all_books)

with open('Итоговый файл.txt', 'w', encoding='UTF-8') as f:
    for books in all_books:
        for strings in books:
            f.write(f'{strings}\n')
