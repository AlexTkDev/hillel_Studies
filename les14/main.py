from group import Group
from create_Student import Student
from ERROR_MaxAmountException import MaxAmountException



st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# st3 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# st4 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# st5 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# st6 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# st7 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# st8 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# st9 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# st10 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# st11= Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# st12= Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
try:
    gr.add_student(st1)
    gr.add_student(st2)
    # gr.add_student(st3)
    # gr.add_student(st4)
    # gr.add_student(st5)
    # gr.add_student(st6)
    # gr.add_student(st7)
    # gr.add_student(st8)
    # gr.add_student(st9)
    # gr.add_student(st10)
    # gr.add_student(st11)
    # gr.add_student(st12)
except MaxAmountException as err:
    print(f"[*] {err.get_exception_message()}!\n"
          f"[*] --> The student {err.first_name} {err.name} 11 on the list,"
          f" create a new group and add this student.")

print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr) # Only one student