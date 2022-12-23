def find_student(id_student: int)-> str:
    """поиcк по id ученика возвращет строку [айди имя фамилия класс литера]"""
    
    with open('student.csv', "r", encoding='UTF-8') as data_file:
        import csv
        for line in data_file.readlines():
            if str(id_student) in line:
                i = 0
                id_data = ''
                while line[i] != "|":
                    id_data = id_data + line[i]
                    i += 1
                if id_student == int(id_data):
                    print_line = line.split('|')
                    print(f'Имя:{print_line[1]}\nФамилия: {print_line[2]} \nID:{print_line[0]}\nКласс: {print_line[3]}{print_line[4]}')                    
                    return line
        return -1
    
def find_id_student(surname: str)-> int:
    """поиcк по фамилии возвращет id ученика"""
    
    with open('student.csv', "r", encoding='UTF-8') as data_file:
        import csv
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