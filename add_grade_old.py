import shutil
import csv
import interface as itf
from typing import List, Optional
# from functions import read_from_csv, write_list_to_csv, give_int_num
# from get_pupil_list import get_pupil_list

def get_id(filename:str, element_to_search) -> int:
    """Функция дает идентификатор из таблиц
    Args:
        filename - имя файла для чтения
        element_to_search - элемент для выбора
    Returns:
        id[int] идентификатор ученика или идентификатор предмета
    """
    with open(filename, 'r', encoding='utf-8') as file:  
        czvfilereader = csv.reader(file, delimiter='|')
        i=0
        for r in czvfilereader:
            if element_to_search in r:
                id = r[0]                 
                i+=1   
                return id                               
        if not element_to_search in czvfilereader:
            itf.error()
            
                 
                
                


# subject = itf.get_subject()       
# print(f"id_sub {get_id('school_subject.csv', subject)}")
# subject_id = get_id('school_subject.csv', subject)
# student = itf.get_surname()
# print(f"id_st {get_id('student.csv', student)}")



# def get_subject_list() -> str:
#     """
#     Считывает csv файл и возвращает строку c предметами (без ID)
#     Returns:
#     str - список в виде строки
#     """ 

#     path_file = 'subjects.csv'
#     subjects_list = read_from_csv(path_file, coding = 'utf-8', delim = '|')
#     string =''
#     for row in subjects_list:
#         string += row[1] +'\n'    
#     return string
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
    return file_list

# def add_grade():
#     """
#     Функция запрашивает у пользователя фамилию ученика, предмет, оценку по предмету и заносит в ведомость.
#     Return:
#     вносит оценки в ведомость (файл)
#     """  
         
#     student = itf.get_surname()
#     student_id = str(get_id('student.csv', student))
#     print(student)
#     print(student_id)
#     subject = itf.get_subject()   
#     print(subject)
#     subject_id = str(get_id('subject.csv', subject))
#     print(subject_id)
#     quarter = itf.give_num('Введите номер четверти:',1,4)
#     grade = str(itf.give_num('Введите оценку:',2,5))

#     if quarter == 1:
#         with open('grades_1_quarter.csv', 'r', encoding='utf-8') as file:  
#             czvfilereader = csv.reader(file, delimiter='|')
#             for r in czvfilereader:
#                 if not student_id in r and not student_id in r:
#                     with open('grades_1_quarter.csv',  'a', newline='', encoding='utf-8') as file: 
#                         data = student_id + '|' + subject_id + '|' + grade
#                         file.write('\n' + data )                    
#                 else:
#                     itf.error1()


#     if quarter == 2:
#         quarter_1 = read_file('grades_1_quarter.csv')
#         for row in quarter_1:
#             if student_id == row[0] and subject_id == row[1] :
#                 grade_quarter_1 = str(*row[2].split(', '))
                 
#         with open('grades_2_quarter.csv', 'a', newline='', encoding='utf-8') as file_2:    
#             data = student_id + '|' + subject_id + '|' + grade_quarter_1+ '|' + grade       
#             file_2.write('\n' + data)   
#     if quarter == 3:
#         quarter_2 = read_file('grades_2_quarter.csv')
#         for row in quarter_2:
#             if student_id == row[0] and subject_id == row[1]:
#                 grade_quarter_1 = str(*row[2].split(', '))
#                 grade_quarter_2 = str(*row[3].split(', '))
#             grade_quarter_1 = str(*row[2].split(', '))
#             grade_quarter_2 = str(*row[3].split(', '))    
#         with open('grades_3_quarter.csv', 'a', newline='', encoding='utf-8') as file_3:    
#             data = student_id + '|' + subject_id + '|' + grade_quarter_1 + '|' + grade_quarter_2 + '|' + grade       
#             file_3.write('\n' + data) 
#     if quarter == 4:
#         quarter_3 = read_file('grades_3_quarter.csv')
        
#         for row in quarter_3:
#             if student_id == row[0] and subject_id == row[1]:
#                 grade_quarter_1 = str(*row[2].split(', '))
#                 grade_quarter_2 = str(*row[3].split(', '))
#                 grade_quarter_3 = str(*row[4].split(', '))
#             grade_quarter_1 = str(*row[2].split(', '))
#             grade_quarter_2 = str(*row[3].split(', ')) 
#             grade_quarter_3 = str(*row[3].split(', '))    
#         with open('grades_all.csv', 'a', newline='', encoding='utf-8') as file_4:    
#             data = student_id + '|' + subject_id + '|' + grade_quarter_1 + '|' + grade_quarter_2 + '|'+ grade_quarter_3 + '|' + grade       
#             file_4.write('\n' + data) 

#     return data


def get_subject_file():
    """
    Функция осуществляет ввод данных от пользователя и запись в файл
    Returns:
        subject.csv - файл с данными о предметах
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

# print(get_subject_file())        
  


def add_grade():
    """
    Функция запрашивает у пользователя фамилию ученика, предмет, оценку по предмету и заносит в ведомость.
    Return:
    вносит оценки в ведомость (файл)
    """  
         
    student = itf.get_surname()
    student_id = str(get_id('student.csv', student))
    # print(student)
    # print(student_id)
    subject = itf.get_subject()   
    # print(subject)
    subject_id = str(get_id('school_subject.csv', subject))
    # print(subject_id)
    # quarter = itf.give_num('Введите номер четверти:',1,4)
    
    with open('grades.csv', 'r', encoding='utf-8') as file_1, open ('grades.csv',  'w', newline='', encoding='utf-8') as file:  
            csvfilereader = csv.reader(file_1, delimiter='|')
            for r in csvfilereader:
                if student_id == r[0] and subject_id == r[1]:
                    if r[2] == 0:
                        grade_1= str(itf.give_num('Введите оценку за 1 четверть:',2,5))
                        data = student_id + '|' + subject_id + '|' + grade_1
                        file.write('\n' + data )     
                    elif r[3] == 0:
                        grade_2= str(itf.give_num('Введите оценку за 2 четверть::',2,5))
                        data = student_id + '|' + subject_id + '|' + grade_1+ '|' + grade_2
                        file.write('\n' + data )  
                    elif r[4] == 0:
                        grade_3= str(itf.give_num('Введите оценку за 3 четверть::',2,5))
                        data = student_id + '|' + subject_id + '|' + grade_1+ '|' + grade_2+ '|' + grade_3
                        file.write('\n' + data )  
                    elif r[5] == 0:
                        grade_3= str(itf.give_num('Введите оценку за 4 четверть::',2,5))
                        data = student_id + '|' + subject_id + '|' + grade_1+ '|' + grade_2+'|' + grade_3+'|' + grade_4
                        file.write('\n' + data )
                        
                         
    # if quarter == 1:
    #     with open('grades_1_quarter.csv', 'r', encoding='utf-8') as file:  
    #         czvfilereader = csv.reader(file, delimiter='|')
    #         for r in czvfilereader:
    #             if not student_id in r and not student_id in r:
    #                 with open('grades_1_quarter.csv',  'a', newline='', encoding='utf-8') as file: 
    #                     data = student_id + '|' + subject_id + '|' + grade
    #                     file.write('\n' + data )                    
    #             else:
    #                 itf.error1()


    # if quarter == 2:
    #     quarter_1 = read_file('grades_1_quarter.csv')
    #     for row in quarter_1:
    #         if student_id == row[0] and subject_id == row[1] :
    #             grade_quarter_1 = str(*row[2].split(', '))
                 
    #     with open('grades_2_quarter.csv', 'a', newline='', encoding='utf-8') as file_2:    
    #         data = student_id + '|' + subject_id + '|' + grade_quarter_1+ '|' + grade       
    #         file_2.write('\n' + data)   
print(add_grade())

# def change_students(ID_student, ID_subject, gdade):
#     count = 0
#     student = itf.get_surname()
#     student_id = str(get_id('school_subject.csv', student))
#     with open('student.csv', 'r', encoding='utf-8') as file:
#         for line in file:
#             if student in line:
#                 count = count + 1
#                 continue
#             else:
#                 with open('temp.csv', 'a', encoding='utf-8') as file:
#                     file.write(line)
#     shutil.copyfile('temp.csv','student.csv')
#     with open('temp.csv', 'w', encoding='utf-8') as i:
#         if count !=0:
#             print('Сотрудник удален!')
#     if count == 0:
#         print('Сотрудника с данной фамилией нет !')