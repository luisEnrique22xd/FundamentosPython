students = []

def show_students():
    for student in students:
        print (student)
        print ("Alumno->", student)

def add_student(student): 
    students.append(student)
    
def remove_student(student):
       try:
            students.remove(student)
       except Exception:
        print ("No existe")
choice_text = """
Elige una opcion:
1- Insertar
2- Mostrar
3- Eliminar
4- Salir
"""
while True:
        choice = int(input(choice_text))
        if choice ==1:
                student = input("ingresa Student: ")
                add_student(student)
        elif choice == 2:
                show_students()
        elif choice == 3:
              student = input("ingresa student a eliminar: ")
              remove_student(student)

        elif choice ==4:
                break
        else:
                print ("Incorrect option")
