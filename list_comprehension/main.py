import random

# ---------- List Comprehension --------

# ========= with list ======
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)
#
# # ======= with string ==========
# letters = "Nosheen"
# letters_list = [letter for letter in letters]
# print(letters_list)
#
# # =========== with range ===========
# range_number = range(1, 5)
# range_list = [n * 2 for n in range_number]
# print(range_list)
#
# # -------------- Conditional List Comprehension -------------
# # ========= with String ==========
# my_list = ["Nosh", "Mina", "Jann", "Zima", "Fajar", "Aqsa", "Ayza"]
# string_list = [name.upper() for name in my_list if len(name) < 5]
# # string_list1 = [name for name in my_list if len(name) < 6]
# print(string_list)

# -------------- Dictionary Comprehension ----------------
# Syntax is: new_dict = {new_key:new_value for item in list}
names = ["Nosheen", "Minahil", "Jannat", "Zimal", "Fajar", "Aqsa", "Ayeza"]

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)
