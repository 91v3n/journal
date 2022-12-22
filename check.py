def check_name(student_name:str='петя')->bool:   
    if len(student_name)>15 or len(student_name)<4:
        return False
    else:
        return True


def cheсk_second_name(student_second_name:str='петров')->bool:
    if len(student_second_name)>15 or len(student_second_name)<2:
        return False
    else:
        return True


def check_class(class_number:int)->bool:	
    if int(class_number)>11 or int(class_number)<1:
        return False
    else:
        return True


def check_class_name(name_class:str='а')->bool:
    class_name_list=['а','б','в','г','д','е','ж','з']
    if class_name_list.count(name_class)==0:
        return False
    else:
        return True


def check_subject(subject : str='биология')->bool:	
    if len(subject)>15 or len(subject)<3:
        return False
    else:
        return True

def student_id(id:int=555555)->bool:
    if len(str(id))>6 or len(str(id))<4:
        return False
    else:
        return True

def check_quarter(quarter:int=4)->bool:	
    if int(quarter)>4 or int(quarter)<1:
        return False
    else:
        return True

def check_grade(grade:int=5)->bool:	
    if int(grade)>5 or int(grade)<2:
        return False
    else:
        return True
