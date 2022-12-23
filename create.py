from interface import get_surname, get_name, get_id_student,get_class_number,get_class_name,create_success

def create_student():
   """
     Функция запрашивает и записывает данные об ученики в текстовый файл с данными об учениках, и создает запись
     об ученике и его оценках в файле оценок в соответсвии с номером класса
          
   """
   with open('student.csv', 'a', encoding='utf-8') as file:
      id_student = get_id_student()  
      surname = get_surname()
      name = get_name()
      class_number = get_class_number()
      class_name = get_class_name()      
      data = id_student + '|' + name + '|' + surname + '|' + class_number + '|' + class_name
      file.write('\n' + data)      
      create_grades(id_student,class_number)
      create_success()
      return data

def create_grades(id_student,class_number):
    """Функция создает запись в журнале оценок. В зависимости от номера класса добавляет предметы и ставит заглушку "0" 
    в каждой четверти для дальнейшего выставления оценок
    Arg:
    (int) id_student
    (int) class_number
    """
    #ищем в файле все предметы соотвествующие номеру класса и возвращаем список
    #ВАЖНО! список предметов должен заканчиваться знаком '|', иначе последний будет в виде 00Х\n и поиск работает плохо для него
    #файл class-sub.csv содержит в [0] элементе строки номер класса , а далее все предметы в этом классе
    #файл class-sub.csv содержит предметы для примера, возможны отличия от существующих школьных программ :)
    with open('class-sub.csv', 'r', encoding='utf-8') as file_sub_class:
        list_of_sub_by_class =[]
        for line in file_sub_class:
            class_number_from_file = line.split('|')[0]
            if class_number_from_file == class_number:
                list_of_sub_by_class=line.split('|')    
    #открываем файл с предметами, если предмет есть в списке предметов для номера класса ученика - добавляем запись о нем в журнал
    #используем заглушку "0" - оценка еще не выставлена за эту четверть 
    with open('school_subject.csv', 'r', encoding='utf-8') as file_sub:
        sub_list=[]
        for line in file_sub:
            sub_list=line.split('|')[0]
            if sub_list in list_of_sub_by_class:
              with open('grades.csv', 'a', encoding='utf-8') as file_grades:                 
                  data_student_grades =id_student+'|' + sub_list + '|' +'0' + '|' +'0' + '|' +'0' + '|' +'0'
                  file_grades.write('\n' + data_student_grades)

