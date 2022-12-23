import interface
import create
import filter
import find
import add_grade


def start():
    while True:
        interface.main_menu()
        i= interface.select_menu_item()
        if i == 1:
            create.create_student()
        elif i == 2:
            ##    
            create.create_student()
        elif i == 3:
            ## 
            id = int(interface.get_id_student())       
            find.find_student(id)   
        elif i == 4:
            filter.student_id_filter()
            ##        
        elif i == 5:
            filter.class_filter()
            ##    
    
