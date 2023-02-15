number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_number = [x for x in number if x % 2 == 0]

# print(new_number)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

weather_f = {x: y * 9/5 + 32 for (x, y) in weather_c.items()}

# print(weather_f)



import pandas

student_dic = {
    "students": ["a", "b", "c"],
    "scores": [1, 2, 3]
}

# for (x, y) in student_dic.items():
    # print(y)
    # print(x, y)

student_df = pandas.DataFrame(student_dic)
# print(student_df)

# for (x, y) in student_df.iterrows():
#     print(x)
#     print(y)
#     print(y.students)
#     print(y.scores)
#     if y.students == "a":
#         print(y.scores)

new_dict = {x: y for x, y in student_df.iterrows()}
# print(new_dict)
print(new_dict[0])
print(type(new_dict[0]))
print(new_dict[0].index)
print(new_dict[0].values)