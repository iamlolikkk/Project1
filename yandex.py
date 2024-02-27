#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def koordinate(self):
#         print("Точка по оси x: ", self.x)
#         print("Точка по оси y: ", self.y)
#
#
# x = input("Введите значение x:\n")
# y = input("Введите значение y:\n")
#
# tochka = Point(x, y)
# tochka.koordinate()
#
#
#
# class Point:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
#
#     def move(self, new_x, new_y):
#         self.x += new_x
#         self.y += new_y
#
#     def length(self, point2):
#         result = ((point2.x - self.x) ** 2 + (point2.y - self.y) ** 2) ** 0.5
#         return round(result, 2)
#
#
# point = Point(3, 5)
# print(point.x, point.y)
# point.move(2, -3)
# print(point.x, point.y)
#
#
#
#
# class RedButton:
#     def __init__(self) -> None:
#         self.counter = 0
#
#     def click(self):
#         self.counter += 1
#         print('Тревога!')
#
#     def count(self):
#         return self.counter
#
#
# first_button = RedButton()
# second_button = RedButton()
# for time in range(5):
#     if time % 2 == 0:
#         second_button.click()
#     else:
#         first_button.click()
# print(first_button.count(), second_button.count())
#
#
#
#
# class Programmer:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#         self.hours_worked = 0
#         self.salary = 0
#     def work(self, time):
#         self.hours_worked += time
#         self.salary += time * self.get_hourly_salary()
#     def rise(self):
#         if self.position == "Senior":
#             self.salary += 1
#         else:
#             self.position = "Senior"
#             self.salary += 20
#     def get_hourly_salary(self):
#         if self.position == "Junior":
#             return 10
#         elif self.position == "Middle":
#             return 15
#         else:
#             return 20
#     def info(self):
#         return f"{self.name} {self.hours_worked}ч. {self.salary}тгр."
# programmer = Programmer("John", "Junior")
# programmer.work(40)
# programmer.rise()
# print(programmer.info())
#
#
#
#
# class Rectangle:
#     def __init__(self, *coords):
#         self.coords = coords
#         self.width = abs(self.coords[0][0] - self.coords[1][0])
#         self.height = abs(self.coords[0][1] - self.coords[1][1])
#
#     def perimeter(self):
#         return round(2 * (self.width + self.height), 2)
#
#     def area(self):
#         return round(self.width * self.height, 2)
#
#
# rect = Rectangle((3.2, -4.3), (7.52, 3.14))
# print(rect.perimeter())
#
#
#
#
# class Rectangle:
#     def __init__(self, corner1, corner2) -> None:
#         self.left_down = [min(corner1[0], corner2[0]),
#                           min(corner1[1], corner2[1])]
#         self.up_right = [max(corner1[0], corner2[0]),
#                          max(corner1[1], corner2[1])]
#
#     def perimeter(self):
#         return round((self.up_right[0] - self.left_down[0]) * 2 +
#                      (self.up_right[1] - self.left_down[1]) * 2, 2)
#
#     def area(self):
#         return round((self.up_right[0] - self.left_down[0]) *
#                      (self.up_right[1] - self.left_down[1]), 2)
#
#     def get_pos(self):
#         return round(self.left_down[0], 2), round(self.up_right[1], 2)
#
#     def get_size(self):
#         return round(self.up_right[0] - self.left_down[0], 2), \
#             round(self.up_right[1] - self.left_down[1], 2)
#
#     def move(self, dx, dy):
#         self.left_down[0] += dx
#         self.left_down[1] += dy
#         self.up_right[0] += dx
#         self.up_right[1] += dy
#
#     def resize(self, width, height):
#         self.up_right[0] = self.left_down[0] + width
#         self.left_down[1] = self.up_right[1] - height
#
# rect = Rectangle((3.2, -4.3), (7.52, 3.14))
# print(rect.get_pos(), rect.get_size())
# rect.move(1.32, -5)
# print(rect.get_pos(), rect.get_size())
#
#
#
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def turn(self):
#         center_x = self.width / 2
#         center_y = self.height / 2
#
#         new_width = self.height
#         new_height = self.width
#
#         self.width = round(new_width, 2)
#         self.height = round(new_height, 2)
#
#     def scale(self, factor):
#         center_x = self.width / 2
#         center_y = self.height / 2
#
#         new_width = self.width * factor
#         new_height = self.height * factor
#
#         self.width = round(new_width, 2)
#         self.height = round(new_height, 2)
#
#     def display(self):
#         print(f"Width: {self.width}")
#         print(f"Height: {self.height}")
#
#
# # Example usage
# rectangle = Rectangle(4, 6)
# rectangle.display()  # Output: Width: 4, Height: 6
# rectangle.turn()
# rectangle.display()  # Output: Width: 6, Height: 4
# rectangle.scale(1.5)
# rectangle.display()  # Output: Width: 9, Height: 6