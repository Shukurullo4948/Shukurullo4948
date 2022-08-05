# 1 UPPER
# class string:
#     def init(self, txt):
#         self.text = txt
#
#     def Upper(self):
#         place = ''
#         for i in self.text:
#             if ord(i) > 91:
#                 place += chr(ord(i) - 32)
#             elif ord(i) < 91:
#                 place += i
#
#         return place
#
# a = string("PyTHon")
# print(a.Upper())
#
# # 2 lower
# class str:
#     def init(self, text):
#         self.t = text
#     def Lower(self):
#         place = ''
#         for i in self.t:
#             if ord(i) > 64 and ord(i) < 90:
#                 place+=chr(ord(i)+32)
#             else:
#                 place+=i
#         return place
# a = str('PYThoN')
# print(a.Lower())
#
# # 3 Replace
# class str:
#     def init(self, a, b):
#         self.txt = b
#     def Replace(self):
#         place = ''
#         for i in self.txt:
#             if i!=a:
#                 place+=i
#             else:
#                 continue
#         return place
# a = str('pytxon', 'python')
# print(a.Replace())

# class Parent:
#     def func1(self):
#         print('This is function in Parent class')
#
# class CHild1(Parent):
#     def func2(self):
#         print('This is function in CHild 1 class')
