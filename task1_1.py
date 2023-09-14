from os.path import join, abspath, dirname
from datetime import datetime


def save_as_file(note_dict: dict):
    MAIN_DIR = abspath(dirname(__file__))
    file_name = join(MAIN_DIR, "notes.csv")
    with open(file_name, mode = "w", encoding = "UTF-8") as file:
        for pos, data in note_dict.items():
            file.write(f"{pos};{data[0]};{data[1]};{data[2]}\n") 

def notes_add(note_dict: dict):
    note = list()
    count = len(note_dict) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите суть заметки: ")
    date_time_now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    note.append(date_time_now)
    note.append(title)
    note.append(body)
    note_dict[count] = note
    save_as_file(note_dict)
    print("Запись сделана")

def notes_read(note_dict: dict):
    if len(note_dict) == 0:
        print("Заметок нет")
    else:
        for number, data in note_dict.items():
            print(f"{number};{data[0]};{data[1]};{data[2]}")
            print()
            
def notes_delete(note_dict: dict, number: int):
    if number is not None:
        note_dict.pop(number)
        save_as_file(note_dict)
        print("Заметка удалена")
    else:
        print("Заметка не найдена")
        
def notes_update(note_dict: dict, number_up: int):
    if number_up is None:
        print("Такой заметки нет")
    else:
        note_dict[number_up][0] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        note_dict[number_up][1] = input("Введите новый зологовок: ")
        note_dict[number_up][2] = input("Введите новую суть заметки: ")
        save_as_file(note_dict)
        print("Заметка изменена")
        
def notes_find(note_dict: dict, number: int):
    if number is None:
        print("Такой заметки нет")
    else:
        print(f"{note_dict[number][0]}:{note_dict[number][1]}:{note_dict[number][2]}")
    



def menu():
    notes_dict = dict()
    print("Введите 0, что-бы выйти")
    print("Введите 1, что-бы создать заметку")
    print("Введите 2, что-бы увидеть все заметки")
    print("Введите 3, что-бы удалить заметку")
    print("Введите 4, что-бы редактировать заметку")
    print("Введите 5, что-бы найти заметку")
    while True:
        num_func = int(input("Введите номер операции: "))
        if num_func == 0:
            break
        if num_func == 1:
            notes_add(notes_dict)
        if num_func == 2:
            notes_read(notes_dict)
        if num_func == 3:
            numb_del = int(input("Введите номер заметки, для удаления: "))
            notes_delete(notes_dict, numb_del)
        if num_func == 4:
            numb_up = int(input("Введите номер заметки для редактирования: "))
            notes_update(notes_dict, numb_up)
        if num_func == 5:
            numb_search = int(input("Введите номер искомой заметки: "))
            notes_find(notes_dict, numb_search)
        
menu()

