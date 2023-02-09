# light = True #-->ПРАВДА
# night = False #-->ЛОЖЬ



# print(light == night)
# print(light)
# print(light == night) #True False


# and, or, not

# age = 21
# car = False
# print(age>=16 and car == True) #False

# print(age>=16 or car == True) #False

# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()

# pos = mc.player.getTilePos()
# x = pos.x
# y = pos.y
# z = pos.z

# block_legs = mc.getBlock(x,y,z) #НОГИ
# block_head = mc.getBlock(x, y+1, z) #ГОЛОВА
# water = 9
# mc.postToChat('Игрок в воде: ' + str(block_legs == water or block_head == water))

# print(True or False)

# color_cat = input('Цвет кошки: ') #РЫЖИЙ ЧЕРНЫЙ БЕЛЫЙ СЕРЫЙ
# my_cat = color_cat == 'белая' or color_cat == 'черная'
# print('Я заведу кошку: ' + str(my_cat))
# int ---> integer
# count_of_cats = int(input('Сколько кошек хочешь? '))
# count_of_cats = 4
# count_of_cats = input('Сколько кошек хочешь? ')
# count_of_cats = '4'
# print(type(count_of_cats))
# print(str(block_legs == water))

# and or
# True or False

# True and False

# print(True and True and True and False)
# print(False and False and False and True)
# and or
# print(False or True or True or False)
# and ---> False
# print(True and True and True and False)   


# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()

# pos = mc.player.getTilePos() 
# x = pos.x
# y = pos.y
# z = pos.z


# block_right = mc.getBlock(x, y, z+2)
# block_left = mc.getBlock(x-2, y, z)
# block_up = mc.getBlock(x+2, y, z)
# block_down = mc.getBlock(x, y, z-2)
# mc.postToChat('игрок в тесноте: ' + str(block_right != 0 and block_left != 0 and block_up != 0 and block_down != 0))
# mc.postToChat('игрок в тесноте: ' + str(block_right != 0 and block_left != 0 and block_up != 0 and block_down != 0))
# str(block_right != 0 and block_left != 0 and block_up != 0 and block_down != 0)
# str(True and True and False and True)
# and ---> False
# str(block_right != 0 and block_left != 0 and block_up != 0 and block_down != 0)
# str(True and True and True and False)
# and ----> False

# mc.postToChat('игрок в тесноте: ' + str(block_right != 0 and block_left != 0 and block_up != 0 and block_down != 0))

# block_up = mc.getBlock(x, y+2, z)
# block_down = mc.getBlock(x, y-1, z)
# mc.postToChat('игрок в туннеле: ' + str(block_up != 0 and block_down != 0))


# seats = [1,2,3,5,4]
# students = [7,6,5,4]

# def solution(s, st):
#     s = sorted(s)
#     st = sorted(st)
#     res = 0
#     for seat,students in zip(s,st):
#         res = abs(seat - students)
#     return res



# solution(seats, students)


# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# import time

# pos = mc.player.getTilePos()
# floorX = pos.x - 2
# floorY = pos.y - 1
# floorZ = pos.z - 2

# width = 5
# length = 5
# block = 41

# mc.setBlocks(floorX, floorY, floorZ, floorX + width, floorY, floorZ + length, block)
# while floorX <= pos.x <= floorX + width and floorZ <= pos.z <= floorZ + length:
# 	if block == 41:
# 		block = 57
# 	else:
# 		block = 41
# 	mc.setBlocks(floorX, floorY, floorZ, floorX + width, floorY, floorZ + length, block)
# 	pos = mc.player.getTilePos()
# 	time.sleep(0.5)


# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# pos = mc.player.getTilePos()
# x = pos.x
# y = pos.y
# z = pos.z

# import random

# # mc.player.setTilePos(x + random.randint(-100, 100), y, z + random.randint(-100, 100))
# import random
# import keyboard

# def randomBlockLocations(blockType, repeats):
#     x, y, z = mc.player.getTilePos()

#     count = 0
#     while count <= repeats:
#         count += 1
#         x += random.randint(-127, 127)
#         z += random.randint(-127, 127)
#         y = mc.getHeight(x, z)
#         mc.setBlock(x, y, z, blockType)

# if __name__ == "__main__":
#     while not keyboard.is_pressed('q'):
#         randomBlockLocations(blockType=150, repeats=200)


# print(2)

# print(2)
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# pos = mc.player.getTilePos()
# posx = pos.x
# posy = pos.y
# posz = pos.z
# print(0==False)
# print(x)
# import math
# def CreatePyramid(posx,posy,posz,width,mybase,mywalls,mytopblock):
#   # Function to create a pyramid at x,y,z
#   # with specified width using the specified
#   # block materials for the base, walls and top.
 
#   mc.postToChat("About to create pyramid!")
 
#   # May sure width is odd number so pyramid ends
#   # with a single block
#   if width%2==0:
#     width=width+1
 
#   height = (width+1)/2
#   halfsize = int(math.floor(width/2))
 
#   print("Player : {} {} {}".format(posx,posy,posz))
#

# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# import keyboard
#
# def func():
#     block = 24
#     height = 75
#
#     pos = mc.player.getTilePos()
#     x, y, z = pos.x + height, pos.y, pos.z
#     for level in reversed(range(height)):
#         mc.setBlocks(x - level, y, z - level, x + level, y, z + level, block)
#         y += 1
#
# while True:
#     if keyboard.is_pressed('q'):
#         func()
# --------------------Пароль----------------------
# password = 'asd'
# count = 0
# limit = 5
# while count<limit:
#     attempt = input('Введите пароль: ')
#     count += 1
#     if attempt == password:
#         print('Верный пароль')
#         break
#     elif count == 4:
#         print('Пароль неверный, осталась последняя попытка')
#     elif attempt != password and count  == 5:
#         print('Количество попыток истекло, ты амогус')
#     else:
#         print('Пароль неверный, осталось ' + str(5-count) + ' попыток(-ки)')
# --------------------Пароль----------------------

# while True:
#     # бесконечно печатает инфинити
#     print("Infinity")

# никогда не выведется
# print("Это сообщения никогда не выведется")

password = 'asd'
login = 'DSA'

count = 0 + 1 + 1
# while count < 5:
#     count = count + 1
#     attempt_password = input('Enter password: ')
#     if attempt_password == password:
#         print('Пароль верен')
#         break
#     elif attempt_password != password:
#         print('Неверный пароль, у вас осталось ' + str(5-count) + 'попыток')
# print('end')


# True = 1
# False = 0
# while 1:
#     print(2)



# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# import random
import time
#Получили наши позиции и координаты
#СЧЁТЧИК
# count = 0
# x, y, z = mc.player.getTilePos()
# pos = mc.player.getTilePos()
# x, y, z = mc.player.getTilePos()
# mc.setBlock(x, y, z, 38, 1)
# mc.setBlock(x + 1, y, z, 38, 2)
# mc.setBlock(x, y, z + 1, 38, 4)
# while count <= 30:
#     pos = mc.player.getTilePos()
#     x = pos.x
#     y = pos.y
#     z = pos.z
#     mc.setBlock(x,y,z,38, 1)
#     mc.setBlock(x+1, y, z, 38, 1)
#     mc.setBlock(x - 1, y, z, 38, 2)
#     mc.setBlock(x, y, z + 1, 38, 3)
#     mc.setBlock(x,y,z-1,38,4)
#     mc.setBlock(x+1,y,z+1,38,5)
#     mc.setBlock(x-1,y,z-1,38,6)
#     mc.setBlock(x+1,y,z-1,38,7)
#     mc.setBlock(x-1,y,z+1,38,8)
#     count += 1
#     time.sleep(0.1)

# while count <= 5:
#     x += random.randint(-200, 200)
#     y += random.randint(-10, 10)
#     z += random.randint(-200, 200)
#     mc.player.setTilePos(x, y, z)
#     count = count + 1
#     time.sleep(2)
# mc.postToChat('Конец телепортаций')



# while 3>2:
#     print('Бесконечный цикл')




# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# import random
# x,y,z = mc.player.getTilePos()
# x_door = -365
# y_door = 78
# z_door = -68
#
# x_block = -371
# y_block = 81
# z_block = -68
#
# air = 0
# stone = 1
# almaz = 57
# # mc.player.setTilePos(-366,78,-70)
# key = mc.getBlock(x_block, y_block, z_block)
# while True:
#     # mc.setBlock(x,y+1,z,100)
#     while key != almaz:
#         key = mc.getBlock(x_block, y_block, z_block)
#         mc.setBlocks(x_door, y_door, z_door, x_door - 4, y_door + 2, z_door + 2, stone)
#     while key == almaz:
#         key = mc.getBlock(x_block, y_block, z_block)
#         mc.setBlocks(x_door, y_door, z_door, x_door - 4, y_door + 2, z_door + 2, air)


# number = 10
# print(humburger)01
# number = int(input())
# login = 'asd'
# password = 'asdasd'
# login_input = input('enter login')
# password_input = input('enter password')
# if


# if 2>3:
#     print('Я дурак')
# elif 4>3:
#     print('Я точно дурак')
# else:
#     print('Я математик')







# from mcpi.minecraft import Minecraft
#
# mc = Minecraft.create()
# import random
#
# pos = mc.player.getTilePos()
# x = pos.x
# y = pos.y
# z = pos.z
# width = 5
# height = 5
# length = 5
# block = 4
# air = 0
# x += random.randint(-5,5)
# y += random.randint(-20,20)
# z += random.randint(-80,80)
# mc.player.setTilePos(x, y, z)
# mc.setBlocks(x, y, z, x + width, y + height, z + length, 0)
# mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height - 1, z + length - 1, 0)
'''
x += random.randint(10)
y += random.randint(40)
z += random.randint(-160)
mc.player.setTilePos(x, y, z)
mc.setBlocks(x, y, z, x + width, y + height, z + length, 4)
mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height - 1, z + length - 1, 0)

x += random.randint(15)
y += random.randint(60)
z += random.randint(-240)
mc.player.setTilePos(x, y, z)
mc.setBlocks(x, y, z, x + width, y + height, z + length, 4)
mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height - 1, z + length - 1, 0)

x += random.randint(20)
y += random.randint(80)
z += random.randint(-320)
mc.player.setTilePos(x, y, z)
mc.setBlocks(x, y, z, x + width, y + height, z + length, 4)
mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height - 1, z + length - 1, 0)

x += random.randint(25)
y += random.randint(100)
z += random.randint(-400)
mc.player.setTilePos(x, y, z)
mc.setBlocks(x, y, z, x + width, y + height, z + length, 4)
mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height - 1, z + length - 1, 0)
'''

# from mcpi.minecraft import Minecraft
# import time
# mc = Minecraft.create()
# import random
# x, y, z = mc.player.getTilePos()
# width = 5
# height = 5
# length = 5
# block = 4
# air = 0
# count = 0
# if a == a:
#!= == <= >= < >
# while count != 5:
#     count += 1
#     x += random.randint(-5, 5)
#     y += random.randint(0, 20)
#     z += random.randint(-80, 80)
#     mc.player.setTilePos(x, y, z)
#     mc.setBlocks(x, y, z, x + width, y + height, z + length, 4)
#     mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height - 1, z + length - 1, 0)
#     time.sleep(2)
#
# mc.postToChat('Конец программы')


# money = 10
# continueInput = input('Хотите продолжить? Да/Нет ')
#
# while continueInput == 'Да':
#     continueInput = input('Хотите продолжить? Да/Нет ')
#     money += 1
#     print('Текущий баланс: ' + str(money))
#
# print('Итоговый счёт: ' + str(money))

'''
x += random.randint(10)
y += random.randint(40)
z += random.randint(-160)
mc.player.setTilePos(x, y, z)
mc.setBlocks(x, y, z, x + width, y + height, z + length, 4)
mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height - 1, z + length - 1, 0)

x += random.randint(15)
y += random.randint(60)
z += random.randint(-240)
mc.player.setTilePos(x, y, z)
mc.setBlocks(x, y, z, x + width, y + height, z + length, 4)
mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height - 1, z + length - 1, 0)

x += random.randint(20)
y += random.randint(80)
z += random.randint(-320)
mc.player.setTilePos(x, y, z)
mc.setBlocks(x, y, z, x + width, y + height, z + length, 4)
mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height - 1, z + length - 1, 0)

x += random.randint(25)
y += random.randint(100)
z += random.randint(-400)
mc.player.setTilePos(x, y, z)
mc.setBlocks(x, y, z, x + width, y + height, z + length, 4)
mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height - 1, z + length - 1, 0)
'''

# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
#
# x, y, z = mc.player.getTilePos()
#
# water = 8
# flow_water = 9
# count = 0
# blockHead = mc.getBlock(x, y+2, z)
# while blockHead == water or blockHead == flow_water:
#     x, y, z = mc.player.getTilePos()
#     blockHead = mc.getBlock(x, y + 2, z)
#     count += 1
#     mc.postToChat('Вы находитесь в воде ' + str(count))
#
# if count > 6:
#     mc.setBlock(x,y,z+1,38)
#     mc.setBlock(x+1,y,z,38)


# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
#
# x,y,z = mc.player.getTilePos()
#
# while True:
#     mc.setBlocks(x,y,z,x+1,y+1,z+1, 57)



# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# import time
# pos = mc.player.getTilePos()
# width = 5
# length = 5
# block = 41
#
# floor_x, floor_y, floor_z = pos.x-2, pos.y-1, pos.z-2
#
# mc.setBlocks(floor_x, floor_y, floor_z, floor_x + width, floor_y, floor_z + length, block)
# while floor_x <= pos.x <= floor_x+width and floor_z<=pos.z<=floor_z+length:
#     if block == 41:
#         block = 57
#     else:
#         block = 41
#     mc.setBlocks(floor_x, floor_y, floor_z, floor_x + width, floor_y, floor_z + length, block)
#     pos = mc.player.getTilePos()
#     time.sleep(0.5)


# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
#
# x,y,z = -444, 74, -131
# width=10
# length=10
# height=10


# mc.setBlocks(x1,y1,z1,x1+5,y1+5,z1+5, 1)
# mc.setBlocks(x1+1,y1+1,z1+1,x+4,y1+4,z1+4, 0)

# mc.setBlocks(x, y, z, x + width, y + height, z + length, 1)
# mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height - 1, z + length - 1, 0)
# while True:
#     x,y,z = -444, 74, -131
#     mc.setBlocks(x, y, z, x + width, y + height, z + length, 1)
#     mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height - 1, z + length - 1, 0)



# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# import time
#
# x,y,z = mc.player.getTilePos()
#
# floor_x = x-3
# floor_y = y-1
# floor_z = z-3
#
# width = 6
# length = 6
#
# mc.setBlocks(floor_x, floor_y, floor_z, floor_x+width, floor_y, floor_z+length, 95,1)
#
# color_glass = 1
# while True:
#     x, y, z = mc.player.getTilePos()
#     while floor_x <= x <= floor_x+width and floor_y == y-1 and floor_z <= z <= floor_z+length:
#         if color_glass == 15:
#             color_glass = 1
#         mc.setBlocks(floor_x, floor_y, floor_z, floor_x + width, floor_y, floor_z + length, 95, color_glass)
#         color_glass += 1
#         time.sleep(0.2)
#         x, y, z = mc.player.getTilePos()



# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
#
# x, y, z = mc.player.getTilePos()
#
# sveto_kamen = 89 #светокамень
#
# x_block = -409
# y_block = 71
# z_block = -129
#
# while True:
#     mc.setBlocks(x_block, y_block, z_block, x_block+5, y_block+5, z_block+5, 1)
#     mc.setBlocks(x_block+1, y_block+1, z_block+1, x_block+4, y_block+4, z_block+4, 0)
#     mc.setBlock(x_block+1, y_block+1, z_block+1,89)
#     mc.setBlock(x_block + 4, y_block + 4, z_block + 4, 89)
#     time.sleep(0.1)
#     x_block = -409
#     y_block = 71
#     z_block = -129


from mcpi.minecraft import Minecraft
mc = Minecraft.create()




