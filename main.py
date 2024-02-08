# 11111
# import random
# class MusicAlbum:
#     def __init__(self, title, artist, release_year, genre, tracklist):
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#         self.genre = genre
#         self.tracklist = tracklist
#
#     def play_random_track(self):
#         import random
#         random_track = random.choice(self.tracklist)
#         print("Название:", self.title)
#         print("Исполнитель:", self.artist)
#         print("Год:", self.release_year)
#         print("Жанр:", self.genre)
#         print("Треки:", self.tracklist)
#         print("Воспроизводится трек:", random_track)

#использования класса MusicAlbum
# album = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
# ["Deutschland", "Badio", "Zeigdich", "Ausländer", "sex",
# "Puppe", "Wasichliebe", "Diamant", "Weitweg", "Tattoo",
# "Hallomann"])
#
# album.play_random_track()

# 222222
# class Student:
#     def __init__(self, name, age, grade, scores):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.scores = scores
#
#     def average_score(self):
#         return sum(self.scores) / len(self.scores)
#
# # Пример использования
# student2 = Student("Егор Данилов", 12, "5В", [5, 4, 4, 5])
# print("Имя:", student2.name)
# print("Возраст:", student2.age)
# print("Класс:", student2.grade)
# print("Оценки:", *student2.scores)
# print("Средний балл:", student2.average_score())

# 33333
# class Recipe:
#     def __init__(self, name, ingredients):
#         self.name = name
#         self.ingredients = ingredients
#
#     def print_ingredients(self):
#         print(f"Ингредиенты для {self.name}:")
#         for ingredient in self.ingredients:
#             print(f"﻿﻿{ingredient}")
#
#     def cook(self):
#         print(f"Сегодня мы готовим {self.name}.")
#         print("Выполняем инструкцию по приготовлению блюда", self.name)
#         print(f"Блюдо {self.name} готово!")
#
# #создаем рецепт спагетти болоньезе
# spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
# #печатаем список продуктов для рецепта спагетти
# spaghetti.print_ingredients()
# #готовим спагетти
# spaghetti.cook()
#
# #создаем рецепт для кекса
# cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло"])
# #печатаем рецепт кекса
# cake.print_ingredients()