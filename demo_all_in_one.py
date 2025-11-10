class StudentRecord:
    def __init__(self, name, student_num, degree, grade_dict=None):
        self.name = name
        self.student_num = student_num
        self.degree = degree
        self.grade_dict = {}
        return
    
    def __str__(self):
        mystr = "*"*30+"\n"
        mystr += self.name+"\n"
        mystr += f"Student Number: {self.student_num}\n"
        mystr += f"Degree: {self.degree}\n"
        mystr += "Modules & Grades:\n"
        for key in self.grade_dict.keys():
            module = key
            grade = self.grade_dict[key]
            mystr += f"  {module}: {grade} \n"
        mystr += f"Average Grade: {self.calculate_grade_average()}\n"
        mystr += "*"*30
        return mystr

    def enter_grade(self, module_code, grade):
        self.grade_dict[module_code] = grade

    def calculate_grade_average(self):
        total = 0
        keys = self.grade_dict.keys()
        n = len(keys)
        for key in keys:
            total +=  self.grade_dict[key]
        av_grade = total/n
        return av_grade


student1 = StudentRecord("Emmet Brown", 239, "BSc Physics")
student1.enter_grade("PHYS205", 55)
student1.enter_grade("MATH220", 75)
student1.enter_grade("LANG201", 80)
student1.enter_grade("COMP101", 90)

print( student1 )
