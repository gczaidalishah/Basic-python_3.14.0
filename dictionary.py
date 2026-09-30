# info={
#  "name": "zaid ali",
#  "subjects": ["calculus", "linear algebra", "signals and systems", "electromagnetics"],
#  "topics_of_today": ("vectors", "matrices"),
#  "department": "electrical engineering",
#  "section": "b",
#  "semester" : 4,
# }
# print(info["subjects"])
# print(info["topics_of_today"])
# student={
#     "name": "zaid ali",
#     "subjects": {
#         "CA" : 3,
#         "DLD" : 2.5,
#         "EE" : 3,
#         "DIFFERENTIAL EQUATIONS" : 2.2,
#     }
    
# }
# pairs= list(student.items())
# # print(student["subjects"]["DLD"])
# # print(list(student.items()))
# # print(student.items())
# print(pairs[1])
# student.update({"city": "charsadda"})
# print(student)
dict= {}
input_key = input("Enter subject name: ")
input_value = 3
dict.update({input_key: input_value})
input_key = input("Enter subject name: ")
input_value = 4
dict.update({input_key: input_value})
input_key = input("Enter subject name: ")
input_value = 5
dict.update({input_key: input_value})
print(dict)