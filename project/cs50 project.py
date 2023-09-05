import os
#os.remove("student.txt")
#os.remove("teacher.txt")
#os.remove("lessons.txt")

students_list = []
class person :
    def __init__ (self,first_name,last_name,code_melli):
        self.firstname = first_name
        self.lastname = last_name
        self.codemelli = code_melli

class term :
    def __init__(self, nomre, name_dars, code_dars,) :
      self.nomre = nomre
      self.name_dars = name_dars
      self.code_dars = code_dars

    def lessons() :
      

      print( """
    1. FARSI 1, TIME: 8:00 TO 10:00, OSTAD: KARIMI
    2. FARSI 2, TIME: 16:00 TO 18:00, OSTAD: AMIRI
    3. MATH 1, TIME: 8:00 TO 10:00, OSTAD: NASERI
    4. FIZIK 1, TIME: 14:00 TO 16:00, OSTAD: ABBASI
    5. BACK""")


      F1 = "FARSI 1, TIME: 8:00 TO 10:00, OSTAD: KARIMI" 
      F2 = "FARSI 2, TIME: 16:00 TO 18:00, OSTAD: AMIRI"
      M1 = "MATH 1, TIME: 8:00 TO 10:00, OSTAD: NASERI"
      FZ1 = "FIZIK 1, TIME: 14:00 TO 16:00, OSTAD: ABBASI"

      choise5 = int(input("choose your lessons: "))
      if choise5 == 1:
       file = open('student.txt' , 'a+')
       file.write("LESSONS : ")
       file.write(F1)
       file.write("\n")
       file.close()
       print("\n")
       print("FARSI 1 ADDED !")
       term.lessons()
      elif choise5 == 2:
       file = open('student.txt' , 'a+')
       file.write(F2)
       file.write("\n")
       file.close()
       print("\n")
       print("FARSI 2 ADDED !")
       term.lessons()
      elif choise5 == 3:
       file = open('student.txt' , 'a+')
       file.write(M1)
       file.write("\n")
       file.close()
       print("\n")
       print("MATH 1 ADDED !")
       term.lessons()
      elif choise5 == 4:
       file = open('student.txt' , 'a+')
       file.write(FZ1)
       file.write("\n")
       file.close()
       print("\n")
       print("FIZIK 1 ADDED !")
       term.lessons()
      elif choise5 == 5:
        student.student_menu()    
      else :
        print("invalid")
        term.lessons()
       
    def nomre() :


  

      pass






class student (person) :
    def __init__(self, first_name, last_name, code_melli, id, field, year):
        super().__init__(self, first_name, last_name, code_melli)
        self.id = id
        self.field = field
        self.year = year




        
   
    students_list = []    
    def register_student ():
      os.system("cls")
      first_name = input('first name: ')
      last_name = input('last name: ')
      id = (input('id: '))
      field = input('field: ')
      year = (input('year: '))
      code_melli = (input('codemelli: '))
      st = student(id, first_name , last_name, code_melli, field, year )
      students_list.append(st)
      file = open('student.txt' , 'a+')
      file.write("\n")
      file.write(f"NAME : {first_name}")
      file.write("\n")
      file.write(f"LASTNAME : {last_name}")
      file.write("\n")
      file.write(f"ID : {id}")
      file.write("\n")
      file.write(f"FIELD : {field}")
      file.write("\n")
      file.write(f"YEAR : {year}")
      file.write("\n")
      file.write(f"CODEMELLI : {code_melli}")
      file.write("\n")
      file.write("\n")
      file.close()
      print("\n")
      print(f"WELLCOME SOTOONE GANG , {first_name} , {last_name}")
      print("\n")
      student.student_menu()
   

    def show_profile_student():

      id = input("enter your id: ")
      for student in students_list:
        if student.id == id :
          print(student.id , student.first_name, student.last_name)

      
 

    def student_menu():
      
    
      print("""                             WELLCOME DEAR STUDENT \U0001F480


\U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      


    ____________
   |            |
1. |  register  |
   |____________|
    __________________
   |                  |
2. |  choose lessons  |
   |__________________|
    ________________
   |                |
3. |  show profile  |
   |________________|
    ________
   |        |
4. |  BACK  |
   |________|   



\U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744

                    """)

      choise2 = int(input("Please choose \U0001F5FF : "))

      if choise2 == 1:
         student.register_student()
      elif choise2 == 2:
         term.lessons()
      elif choise2 == 3:
         student.show_profile_student()
      elif choise2 == 4:
         os.system("cls")
         mainmenu()
      else :
         print ("\U00002757 \U00002757 \U00002757 \U00002757 \U00002757   INVALID   \U00002757 \U00002757 \U00002757 \U00002757 \U00002757")
      student.student_menu()




class teacher (person) :
    def __init__(self, first_name, last_name, code_melli, role, code):
        super().__init__(first_name, last_name, code_melli)
        self.code = code
        self.role = role


    def register_teacher ():
      os.system("cls")
      print("\n")
      firstname = input('first name: ')
      lastname = input('last name: ')
      code = (input('code: '))
      role = input('role: ')
      codemelli = (input('codemelli: '))
      file = open('teacher.txt' , 'a+')
      file.write(f"NAME : {firstname}")
      file.write("\n")
      file.write(f"LASTNAME : {lastname}")
      file.write("\n")
      file.write(f"CODE : {code}")
      file.write("\n")
      file.write(f"ROLE : {role}")
      file.write("\n")
      file.write(f"CODEMELLI : {codemelli}")
      file.write("\n")
      file.write("\n")
      file.write("\n")
      file.close()
      print("\n")
      print(f"WELLCOME DEAR  {firstname} , {lastname}")
      print("\n")
      teacher.teacher_menu()
     

    def show_lessons() :
      
      print( """
    1. FARSI 1, TIME: 8:00 TO 10:00, OSTAD: KARIMI
    2. FARSI 2, TIME: 16:00 TO 18:00, OSTAD: AMIRI
    3. MATH 1, TIME: 8:00 TO 10:00, OSTAD: NASERI
    4. FIZIK 1, TIME: 14:00 TO 16:00, OSTAD: ABBASI
    5. BACK""")
      choise6 = int(input("choose: ")) 
      if choise6 == 5:
         teacher.teacher_menu()
      else :
        print("invalid")
        teacher.show_lessons()     
    

    def list_students():
      
      file = open("student.txt", "r")
      print(file.read())
      teacher.teacher_menu()


    def show_profile_teacher() :
      
      file = open("teacher.txt", "r")
      print(file.read())
       

    def teacher_menu():
    
      print("""                             WELLCOME DEAR TEACHER \U0001F4BC


\U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      


    ____________
   |            |
1. |  register  |
   |____________|
    ________________
   |                |
2. |  show lessons  |
   |________________|
    _________________
   |                 |
3. |  list students  |
   |_________________|
    ________________
   |                |
4. |  show profile  |
   |________________|
    ________
   |        |
5. |  BACK  |
   |________|   



\U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744

                    """)
      choise3 = int(input("Please choose \U0001F5FF : "))
      if choise3 == 1:
        teacher.register_teacher()
      elif choise3 == 2:
        teacher.show_lessons()
      elif choise3 == 3:
        teacher.list_students()
      elif choise3 == 4:
        teacher.show_profile_teacher()
      elif choise3 == 5:
        os.system("cls")
        mainmenu()
      else :    
        print ("\U00002757 \U00002757 \U00002757 \U00002757 \U00002757   INVALID   \U00002757 \U00002757 \U00002757 \U00002757 \U00002757")
        teacher.teacher_menu()




class employee (person) :
    def __init__(self, first_name, last_name, code_melli,code,role):
        super().__init__(first_name, last_name, code_melli)
        self.code = code
        self.role = role


    def register_students ():
      os.system("cls")
      print("\n")
      firstname = input('first name: ')
      lastname = input('last name: ')
      id = (input('id: '))
      field = input('field: ')
      year = (input('year: '))
      codemelli = (input('codemelli: '))
      file = open('student.txt' , 'a+')
      file.write(f"NAME : {firstname}")
      file.write("\n")
      file.write(f"LASTNAME : {lastname}")
      file.write("\n")
      file.write(f"ID : {id}")
      file.write("\n")
      file.write(f"FIELD : {field}")
      file.write("\n")
      file.write(f"YEAR : {year}")
      file.write("\n")
      file.write(f"CODEMELLI : {codemelli}")
      file.write("\n")
      file.write("\n")
      file.close()
      print("\n")
      print(f" {firstname} , {lastname} added")
      employee.employee_menu()
        
  
    def list_students() : 
      os.system("cls") 
      f = open("student.txt", "r")
      print(f.read())
      employee.employee_menu()


    def register_teachers ():
        os.system("cls")
        print("\n")
        firstname = input('first name: ')
        lastname = input('last name: ')
        code = (input('code: '))
        role = input('role: ')
        codemelli = (input('codemelli: '))
        file = open('teacher.txt' , 'a+')
        file.write(f"NAME : {firstname}")
        file.write("\n")
        file.write(f"LASTNAME : {lastname}")
        file.write("\n")
        file.write(f"CODE : {code}")
        file.write("\n")
        file.write(f"ROLE : {role}")
        file.write("\n")
        file.write(f"CODEMELLI : {codemelli}")
        file.write("\n")
        file.write("\n")
        file.close()
        print("\n")
        print(f"{firstname} , {lastname} added! ")
        employee.employee_menu()
        
  
    def list_teachers() :
      os.system("cls")
      file = open("teacher.txt", "r")
      print(file.read())
      employee.employee_menu()
  

    def list_lessons() :
      

      print( """
    1. FARSI 1, TIME: 8:00 TO 10:00, OSTAD: KARIMI
    2. FARSI 2, TIME: 16:00 TO 18:00, OSTAD: AMIRI
    3. MATH 1, TIME: 8:00 TO 10:00, OSTAD: NASERI
    4. FIZIK 1, TIME: 14:00 TO 16:00, OSTAD: ABBASI
    5. BACK""")


      F1 = "1. FARSI 1, TIME: 8:00 TO 10:00, OSTAD: KARIMI" 
      F2 = "2. FARSI 2, TIME: 16:00 TO 18:00, OSTAD: AMIRI"
      M1 = "3. MATH 1, TIME: 8:00 TO 10:00, OSTAD: NASERI"
      FZ1 = "4. FIZIK 1, TIME: 14:00 TO 16:00, OSTAD: ABBASI"

      file = open("lessons.txt" , "a+")
      file.write(F1)
      file.write("\n")
      file.write(F2)
      file.write("\n")
      file.write(M1)
      file.write("\n")
      file.write(FZ1)
      file.close()
      
      choise6 = int(input("choose: ")) 
      if choise6 == 5:
         employee.employee_menu()
      else :
        print("invalid")
        employee.list_lessons()


    def employee_menu():
        
       
        print(""" 
                                                        WELLCOME DEAR EMPLOYEE \U0001F4BB

\U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744     
               
    _________________________
   |                         |
1. |    register students    |
   |_________________________|
    _____________________     
   |                     |
2. |    list students    |
   |_____________________| 
    ________________________     
   |                        |
3. |    register teacher    |
   |________________________| 
    _____________________     
   |                     |
4. |    list teachers    |
   |_____________________| 
    ______________________     
   |                      |
5. |     list lessons     |
   |______________________|
    ______________    
   |              |
6. |     BACK     |
   |______________|                  


\U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744
                     
                      """)
        choise4 = int(input("Please choose \U0001F5FF : "))
        if choise4 == 1:
          employee.register_students()
        elif choise4 == 2:
          employee.list_students()
        elif choise4 == 3:
          employee.register_teachers()
        elif choise4 == 4:
          employee.list_teachers()
        elif choise4 == 5:
          employee.list_lessons()
        elif choise4 == 6:
          os.system("cls")
          mainmenu()
        else :            
          print ("\U00002757 \U00002757 \U00002757 \U00002757 \U00002757   INVALID   \U00002757 \U00002757 \U00002757 \U00002757 \U00002757")
        employee.employee_menu()  



                
def login_student() :
  os.system("cls")
  print("""                                                    
                                        \U00002744  \U00002744  \U00002744  \U00002744    
                                        \U00002744  LOGIN \U00002744
                                        \U00002744  \U00002744  \U00002744  \U00002744    
                                                                               
                                                                               """       )
  username = input("\U0001F512 USERNAME : ")
  print("""
.
.
.
""")
  password = int(input("\U0001F511 PASSWORD : "))

  username_student = "mehdi"
  password_studen = 1710

  if username == username_student and password == password_studen :
        student.student_menu()     
  else :
      print("\U00002757 \U00002757 \U00002757 \U00002757 \U00002757   INCORRECT   \U00002757 \U00002757 \U00002757 \U00002757 \U00002757")
      mainmenu()

def login_teacher() :
  os.system("cls")
  print("""                                                    
                                        \U00002744  \U00002744  \U00002744  \U00002744    
                                        \U00002744  LOGIN \U00002744
                                        \U00002744  \U00002744  \U00002744  \U00002744    
                                                                               
                                                                               """       )
  
  username = input("\U0001F512 USERNAME : ")
  print("""
.
.
.
""")
  password = int(input("\U0001F511 PASSWORD : "))

  username_teacher = "yousof"
  password_teacher =1212

  if username == username_teacher and password == password_teacher :
      teacher.teacher_menu()
  else :
      print("\U00002757 \U00002757 \U00002757 \U00002757 \U00002757   INCORRECT   \U00002757 \U00002757 \U00002757 \U00002757 \U00002757")
      mainmenu()    

def login_employee() :
  os.system("cls")

  username_employee = "amin"
  password_employee = 1234

  print("""                                                    
                                        \U00002744  \U00002744  \U00002744  \U00002744    
                                        \U00002744  LOGIN \U00002744
                                        \U00002744  \U00002744  \U00002744  \U00002744    
                                                                               
                                                                               """       )
  
  username = input("\U0001F512 USERNAME : ")
  print("""
.
.
.
""")
  password = int(input("\U0001F511 PASSWORD : "))
  if username  == username_employee and password == password_employee :
     employee.employee_menu()
 
  else :
       print("\U00002757 \U00002757 \U00002757 \U00002757 \U00002757   INCORRECT   \U00002757 \U00002757 \U00002757 \U00002757 \U00002757")
       mainmenu()  









def mainmenu():
   
  print("""                                     
                                                    \U000026A1 \U000026A1 \U000026A1
                                            
                                         \U0001F4A5 \U0001F4A5 \U0001F4A5   WELLCOME   \U0001F4A5 \U0001F4A5 \U0001F4A5
                                           
                                                    \U000026A1 \U000026A1 \U000026A1



\U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744                                           
            
    ____________________                    ____________________                     _____________________
   |                    |                  |                    |                   |                     |
1. |    AS A STUDENT    |               2. |    AS A TEACHER    |                3. |    AS A EMPLOYEE    |         
   |____________________|                  |____________________|                   |_____________________|
                                          
 
\U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744      \U00002744 


                       """)
  choise = int(input("Please choose \U0001F5FF : "))
  if choise == 1:
        login_student()
        student.student_menu()
  elif choise == 2:
        login_teacher()
        teacher.teacher_menu()
  elif choise == 3:
        #login_employee()
        employee.employee_menu()    
  else :  
        print ("\U00002757 \U00002757 \U00002757 \U00002757 \U00002757   INVALID   \U00002757 \U00002757 \U00002757 \U00002757 \U00002757")
        
        mainmenu()
   


mainmenu()
