from typing import List
import csv
import interface as ie
import check as ch

def read_from_csv(path_file) -> List[str]:
    """
    Считывает csv файл и возвращает список
    Args:
    path_file - путь до файла,
    Returns:
    List[str] - список
    """
    list_file = []
    with open(path_file, 'r', encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = '|')
        for row in file_reader:
            if row != []:
                list_file.append(row)
    return list_file

def student_id_filter():
    student_list = read_from_csv('student.csv')
    # print(student_list) # проверка УДАЛИТЬ!!!
    subject_list = read_from_csv('school_subject.csv')
    # print(subject_list) # проверка УДАЛИТЬ!!!
    grades_list = read_from_csv('grades.csv')
    # print(grades_list) # проверка УДАЛИТЬ!!!
    id_filter_criterion = ie.get_id_student() # работает только если в модуле find файлы csv                
    new_grades_list = []
    for row in grades_list:
        if row[0] == id_filter_criterion:
            new_grades_list.append(row)
    # print(new_grades_list) # проверка УДАЛИТЬ!!!

    for row in student_list:
        if row[0] == id_filter_criterion:
            student_name = row[1] + ' ' + row[2]
    # print(student_name) # проверка УДАЛИТЬ!!!

    for i in range(0, len(new_grades_list)):
        count = 0
        new_grades_list[i][0] = student_name
        # new_grades_list[i][1] = subject_name # как-то надо вытащить из списка предметов название по id в новом списке оценок
        count +=1
    # print(new_grades_list) # проверка УДАЛИТЬ!!!

    ie.top_line1()
    count = 0
    for row in new_grades_list:
        print(f' {row[0]}|\t\t{row[1]}      |\t  {row[2]} |\t     {row[3]} |\t{row[4]} |\t   {row[5]}')
    count += 1


def class_filter() -> List[str]:
    """
    Запрашивает у пользователя класс и литеру, выдаёт список учеников в данном классе
    Returns:
    List[str] - список
    """
    student_list = read_from_csv('student.csv') 
    class_filter_criterion = ie.get_class_number()
    ch.check_class(class_filter_criterion)
    letter_filter_criterion = ie.get_class_name()
    new_class_list = []
    for row in student_list:
        if row[3] == class_filter_criterion and row[4] == letter_filter_criterion.lower():
            new_class_list.append(row)
    ie.top_line()
    count = 0
    for row in new_class_list:
        print(f' {row[0]}   |\t{row[1]}|\t{row[2]}|\t   {row[3]} |\t   {row[4]}')
    count += 1




# student_id_filter()
# class_filter() # проверено, работает
