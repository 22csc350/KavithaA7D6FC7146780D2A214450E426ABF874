class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):

  sorted_student = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_student


student = [Student("sivasankari","A123",7.8), Student ("ramya","A124",8.9),Student("midhuna","A125",9.1),Student("meera","A126",9.9),]

sorted_student= sort_students(student)

for student in sorted_student:
  print ("Name: {}, CGPA: {}".format(student.name,student.roll_number, student.cgpa))