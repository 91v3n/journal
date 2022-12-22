import check
def get_class_name():
    '''Запрашивает у пользовтеля литеру класса, проверяет верность введенных данных'''
    class_name = ''
    while not check.check_class_name(class_name): 
        class_name = input('Введите литеру класса: ')
    return class_name
def get_class_number():
    '''Запрашивает у пользовтеля номер класса, проверяет верность введенных данных'''
    class_number = 0
    while not check.check_class(class_number): 
        class_number = input('Введите номер класса: ')
    return class_number
def get_id_student():
    '''Запрашивает у пользовтеля номер приказа о зачислении ученика в школу (6 цифр), проверяет верность введенных данных'''
    id_student = ''
    while not check.student_id(id_student): 
        id_student = input('Введите номер приказа о зачислении ученика в школу: ')
    return id_student

def get_surname():
    '''Запрашивает у пользовтеля фамилию, проверяет верность введенных данных'''
    surname = ''
    while not check.cheсk_second_name(surname): 
        surname = input('Введите фамилию: ')
    return surname

def get_name():
    '''Запрашивает у пользовтеля имя, проверяет верность введенных данных'''
    name = ''
    while not check.check_name(name):
        name = input('Введите имя: ')
    return name












# функция для отображения списка учеников при фильтрации по классу и литере
def top_line():
    '''Печатает шапку'''
    print("---"*19)
    print('ID ученика|\tимя|\tфамилия|\tкласс|\tлитера')
    print("---"*19)

# функция для отображения списка оценок при фильтрации по ученику
def top_line1():
    '''Печатает шапку'''
    print("---"*27)
    print('           ФИО|\tназвание предмета|1 четверть|2 четверть|3 четверть|4 четверть')
    print("---"*27)