import os
from provider import readfile_str, readfile_list, add_str, add_list
from view import print_str, print_list
from user import input_contact, find_string, print_contact, search_ru, find_ru, delete_contact, change_contact

file_book = {"str": 'book1.txt', "1st": 'book2.txt'}

def init_dict(book, key):
    if key == "1st":
        book[key] = readfile_list(file_book[key])
    else:
        book[key] = readfile_list(file_book[key])
# Функция для вывода контактов
def print_book(data):
    print_list(data['1st'])
    print()
    print_str(data["str"])

# Функция для работы со справочником book1
def write_new_contact_str(book):
    add_str(file_book['str'], input_contact())
    init_dict(book, 'str')
    print()
    print("Добавлен")

# Функция для работы со справочником book2
def write_new_contact_list(book):
    add_list(file_book['list'], input_contact())
    init_dict(book, 'list')
    print()
    print("Добавлен")

# def replace_contact_str(book):
#     repl = change_contact(book['str']) # функция из файла user
#     if repl[1] != '':

