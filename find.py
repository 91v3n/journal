
def find_student(id_student: int)-> str:
    """поиcк по id ученика возвращет строку [айди имя фамилия класс литера]"""
    
    with open('students.txt', "r", encoding='UTF-8') as data_file:
        for line in data_file.readlines():
            if str(id_student) in line:
                i = 0
                id_data = ''
                while line[i] != "|":
                    id_data = id_data + line[i]
                    i += 1
                if id_student == int(id_data):
                    return line
        return -1


def find_id_student(surname: str)-> int:
    """поиcк по фамилии возвращет id ученика"""
    with open('students.txt', "r", encoding='UTF-8') as data_file:
        for line in data_file.readlines():
            if surname in line:
                i = 0
                id_student = ''
                while line[i] != "|":
                    id_student = id_student + line[i]
                    i += 1
                return int(id_student)
        else:
            return -1

