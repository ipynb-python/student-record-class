from student_record import StudentRecord

student1 = StudentRecord("Emmet Brown", 239, "BSc Physics")
student1.enter_grade("PHYS205", 55)
student1.enter_grade("MATH220", 55)
student1.enter_grade("PHYS205", 55)

print(student1.name)
