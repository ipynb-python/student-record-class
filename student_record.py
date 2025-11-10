class StudentRecord:
    def __init__(self, name, student_num, degree):
        self.name = name
        self.student_num = student_num
        self.degree = degree
        self.grade_dict = {}
        return
    
    def enter_grade(self, module_code, grade):
        self.grade_dict[module_code] = grade

    def calculate_grade_average(self):
        total = 0
        keys = self.grade_dict.keys
        n = len(keys)
        for key in keys:
            total +=  self.grade_dict[key]
        

    
