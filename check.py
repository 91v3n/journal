def check_name(student_name:str='петя')->bool:
    """возвращает true если строка из букв от 4 до 15 символов
    """   
    if not student_name.isalpha():
        return False
    if len(student_name)>15 or len(student_name)<4:
        return False
    else:
        return True


def cheсk_second_name(student_second_name:str='петров')->bool:
    """возвращает true если строка из букв от 3 до 15 символов
    """   
    if not student_second_name.isalpha():
        return False
    if len(student_second_name)>15 or len(student_second_name)<2:
        return False
    else:
        return True


def check_class(class_number:str)->bool:
    """возвращает true если строка из цирфы от 1 до 11 
    """   
    if class_number.isdigit() == False:
        return False	
    if int(class_number)>11 or int(class_number)<1:
        return False
    else:
        return True


def check_class_name(name_class:str='а')->bool:
    """возвращает true если строка из буквы в диапозоне алфавита от а до з включительно
    """   
    class_name_list=['а','б','в','г','д','е','ж','з']
    if class_name_list.count(name_class)==0:
        return False
    else:
        return True


def check_subject(subject : str='биология')->bool:	
    """возвращает true если строка из букв от 3 до 15 символов
    """   
    if not subject.isalpha():
        return False
    if len(subject)>15 or len(subject)<3:
        return False
    else:
        return True

def student_id(id:str)->bool:
    """возвращает true если строка из цифр от 4 до 6 символов
    """  
    if id.isdigit() == False:
        return False
    if len(str(id))>6 or len(str(id))<4:
        return False
    else:
        return True

def check_quarter(quarter:str)->bool:	
    """возвращает true если строка из цифры от 1 до 4 включительно
    """  
    if quarter.isdigit() == False:
        return False
    if int(quarter)>4 or int(quarter)<1:
        return False
    else:
        return True

def check_grade(grade:str)->bool:	
    """возвращает true если строка из цифры от 2 до 5 включительно
    """  
    if grade.isdigit() == False:
        return False
    if int(grade)>5 or int(grade)<2:
        return False
    else:
        return True



def check_item_menu(item_menu:str)->bool:
    """возвращает true если строка из цифры от 1 до 5 включительно
    """  
    if 	item_menu.isdigit() and int(item_menu)>0 and int(item_menu)<5:
        return True
    else:
        return False    
    
