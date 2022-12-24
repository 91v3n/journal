import csv
import interface as itf
from typing import List, Optional
import find  #подключен раздел

def get_id_sub(sub:str) -> int:
    """Функция дает идентификатор из таблиц
    Args:
        filename - имя файла для чтения
        element_to_search - элемент для выбора
    Returns:
        id[int] идентификатор ученика или идентификатор предмета
    """
    with open('school_subject.csv', "r", encoding='UTF-8') as data_file:
       
        for line in data_file.readlines():
            if sub in line:
                i = 0
                id_sub = ''
                while line[i] != "|":
                    id_sub = id_sub + line[i]
                    i += 1
                return id_sub
        else:
            return -1    
            

def read_file(filename:str):
    """
    Считывает csv файл и возвращает строку 
    Args:
    Args:
        filename - имя файла для чтения
    Returns:
        List[str] - список
    """ 
    file_list = []
    with open(filename, 'r', encoding='utf-8') as file_reed:    
        file_reader = csv.reader(file_reed, delimiter='|')  
        for row in file_reader:
            if row != []:
                file_list.append(row) 
    #print(file_list)            
    return file_list

def add_grade():
    """
    Функция запрашивает у пользователя фамилию ученика, предмет, оценку по предмету и заносит в ведомость.
    Return:
    вносит оценки в ведомость (файл)
    """  
         
    student = itf.get_surname()
    student_id = str(find.find_id_student(student))
    #print(student)
    #print(student_id)
    subject = itf.get_subject()   
    #print(subject)
    subject_id = str(get_id_sub(subject))
    #print(subject_id)
    #quarter = itf.give_num('Введите номер четверти:',1,4) #тут твоя функция из интерфейса , я писала свою - можно оставить любую главное что бы четверть была int
    quarter = int(itf.give_num_quarter())
    #grade = str(itf.give_num('Введите оценку:',2,5)) #тут твоя функция из интерфейса , я писала свою - можно оставить любую 
    grade = itf.give_num()
    grade_list = read_file('grades.csv')  #записываем файл в лист
    not_found = 0
    #print(grade_list)
    sw = 0 
    for row in grade_list:          #ищем студента и предмет , если его нет то сообщение что этот студент еще не учит этот предмет
        
        if row[0] == student_id and row[1] ==subject_id :
            row[quarter+1] = grade
            sw = 1
            #print(row)
            #print('нашли')
            with open('grades.csv', 'w', encoding='utf-8') as file_4: 
                for i in range(len(grade_list)):
                    a = grade_list[i][0]+'|'+grade_list[i][1]+'|'+grade_list[i][2]+'|'+grade_list[i][3]+'|'+grade_list[i][4]+'|'+grade_list[i][5]                    
                    file_4.write(f'{a}\n')
    if sw == 1:                 
        print('Оценка успешно выствлена!')    # лучше в интерфейс вынести
    else:
        print('Ученик еще не обучается этому предмету, загляните через год')

       



def get_subject_file():
    """
    Функция осуществляет ввод данных от пользователя и запись в файл
    Returns:
        school_subject.csv- файл с данными о предметах
    """

    csv.register_dialect('subject', delimiter='|', lineterminator="\r")
    with open("school_subject.csv", mode="w", encoding='utf-8') as file:
        file_writer = csv.writer(file, 'subject')
        file_writer.writerow(["id", "Предмет"])
        file_writer.writerow(["001", "литература"])
        file_writer.writerow(["002", "русский язык"])
        file_writer.writerow(["003", "математика"])
        file_writer.writerow(["004", "музыка"]) 
        file_writer.writerow(["005", "физкультура"]) 
        file_writer.writerow(["006", "иностранный язык"]) 
        file_writer.writerow(["007", "природоведение"]) 
        file_writer.writerow(["008", "биология"])     
        file_writer.writerow(["009", "история"])
        file_writer.writerow(["010", "информатика"]) 
        file_writer.writerow(["011", "обществознание"]) 
        file_writer.writerow(["012", "экология"]) 
        file_writer.writerow(["013", "физика"]) 
        file_writer.writerow(["014", "химия"])     


#read_file('grades.csv')        
#add_grade()   

