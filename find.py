def find_student(id_student: int)-> str:
    """поиcк по id ученика возвращет строку [айди имя фамилия класс литера]"""
    
    with open('student.txt', "r", encoding='UTF-8') as data_file:
        for line in data_file.readlines():
            if str(id_student) in line:
                return line


def find_id_student(surname: str)-> int:
    """поиcк по фамилии возвращет id ученика"""
    with open('student.txt', "r", encoding='UTF-8') as data_file:
        for line in data_file.readlines():
            if surname in line:
                i = 0
                id_student = ''
                while line[i] != "|":
                    id_student = id_student + line[i]
                    i += 1
    return int(id_student) 

