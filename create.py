from interface import get_surname, get_name, get_id_student,get_class_number,get_class_name

def create_student():
   """
     Функция запрашивает и записывает данные об ученики в текстовый файл с данными об учениках, и создает запись
     об ученике и его оценках в файле оценок
          
   """
   with open('students.txt', 'a', encoding='utf-8') as file:
      id_student = get_id_student()  
      surname = get_surname()
      name = get_name()
      class_number = get_class_number()
      class_name = get_class_name()      
      data = id_student + '|' + name + '|' + surname + '|' + class_number + '|' + class_name
      file.write('\n' + data)      
      create_grades(id_student)
      return data

def create_grades(id_student):
    with open('sub.txt', 'r', encoding='utf-8') as file_sub:
        sub_list=[]
        for line in file_sub:
            sub_list=line.split('|')[0]
            with open('grades.txt', 'a', encoding='utf-8') as file_grades:                 
                data1 =sub_list+'|' + id_student + '|' +'0' + '|' +'0' + '|' +'0' + '|' +'0'
                file_grades.write('\n' + data1)

