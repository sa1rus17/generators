students = [
    {'id': 1, 'full_name': 'Муллакаев Андрей Евгеньевич'},
    {'id': 2, 'full_name': 'Левин Максим Максимович'},
    {'id': 3, 'full_name': 'Клишин Даниил Денисович'},
]

full_names = [student['full_name']
              for student
              in students
              if len(student['full_name'].split()[1]) > 6]
print(full_names)
   
