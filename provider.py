# Файл для чтения информации из справочников
# Функция для чтения справочника как строки
def readfile_str(file_book):
    with open(file_book, "r", encoding="utf_8") as s:
         # модификатор R - чтение данных
        return list(map(lambda x: x.replace('n', ''), s.readlines()))

# Функция для чтения справочника как списка        
def readfile_list(file_book):
    with open(file_book, "r", encoding="utf_8") as s:
         # модификатор R - чтение данных
        return list(map(lambda x: x.replace('n', ''), s.read().split('\n\n')))
         # заменяет что-то? на , (запятую) 

def add_str(file_book, contact):
    with open(file_book, "a", encoding="utf_8") as s:
         # модификатор a - добавление данных
        s.write(", ".join(contact).title()+"\n")
        # joint - генератор строк
        # title -  работа с регистрами

def add_list(file_book, contact):
    with open(file_book, "a", encoding="utf_8") as s:
         # модификатор a - добавление данных
        s.write(str("\n".join(contact).title()+'\n\n'))

