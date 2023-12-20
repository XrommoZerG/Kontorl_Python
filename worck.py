from datetime import date
import os, json , csv


notes_list = list()
file_name = 'notesc.csv'

notes_data = ['id', 'date', 'text']

def work_notes():
    global tasks_dict
    tasks_dict = read_csv(file_name)
    while (1):
        show_menu()
        match input():
            case '1': add_new_note()
            case '2': show_all_notes()
            case '3': show_date_note()
            case '4': change_note()
            case '5': delete_note()
            case '6': break

def show_menu():

    print('1. Добавить заметку',
          '2. Показать все заметки',
          '3. Показать за определенную дату',
          '4. Изменить заметку',
          '5. Удалить запись',
          '6. Закончить работу',"",sep = '\n')

def show_ask_menu():
        print('Сохранить изменения?',
              '1. Да',
              '2. Нет',"",sep = '\n')
        

def add_new_note():
    global notes_list
    data = []
    if (len(notes_list) == 0):
        data.append(1) 
    else:
        data.append(notes_list[-1]['id'] + 1) 
    data.append(str(date.today())) 
    data.append(input('Введите заметку: ')) 
    notes_list.append(dict(zip(notes_data, data)))
    write_csv(file_name, notes_list)



def show_all_notes():
    if (len(notes_list) == 0): 
        print ("Заметки не найдены!")
    else:
        for line in notes_list:
            print_one_line(line)

def show_date_note():
    data = input('Введите дату: ') 
    for line in notes_list:
        if (line["date"] == data):
            print_one_line(line)

def print_one_line(line):
    print(json.dumps(line))

def change_note():
    show_all_notes()
    change_one_note(input("Введите номер заметки которую хотите изменить: "))

def change_one_note(index):
    line = try_to_find(index)
    if (line):
        line["task"] = input("Введите новую заметку: ")
        write_csv(file_name, notes_list)
    else: print ('Такой заметки нет.')

def try_to_find(index):
    for line in notes_list:
        if line["id"] == int(index): return line
    return {}

def delete_note():
    show_all_notes()
    delete_one_line(input("Какую заметку будем удалять?: "))

def delete_one_line(index):
    line = try_to_find(index)
    if (line):
        print_one_line(line)
        show_ask_menu()
        match input():
            case '1': notes_list.remove(line)
            case '2': return 
        write_csv(file_name, notes_list)
    else: print('Такой заметки нет.')







def read_csv(filename):
    with open(filename) as d:
        return csv.reader(d)


def write_csv(filename , tasks_dict):
    with open (filename, 'w') as f:
        write = csv.writer(f)
        write.writerow(notes_data)
        

work_notes()

