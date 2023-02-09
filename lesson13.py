# from mcpi.minecraft import Minecraft
# # импортим нужные библиотеки
# import random
# import math
# import time
# mc = Minecraft.create()
#
# # получаем корды игрока
# x, y, z = mc.player.getTilePos()
#
# # дублируем их в корды блока
# block_x, block_y, block_z = x, y, z
#
# # изменяем x и z случайным образом, чтобы спавнить блок
# block_x += random.randint(-200, 200)
# block_z += random.randint(-200, 200)
# # для y используем getHeight - блок заспавнился на поверхности
# block_y = mc.getHeight(block_x, block_z)
#
# # записываем идентификатор блока
# block = 89
#
# # флаг для проверки создан блок или нет
# block_create = False
#
# # пока блок не создан
# while not block_create:
#     # делаем проверку чтобы блок не мог спавнится на воде
#     if block_y - 1 != 8 or block_y - 1 != 9:
#         # спавним блок
#         mc.setBlock(block_x, block_y, block_z, block)
#         # меняем флаг на true
#         block_create = True
#         # блок создан
#         mc.postToChat("Блок создан")
#
#
# # запускаем бесконечный цикл
# while True:
#     # получаем корды игрока
#     x, y, z = mc.player.getTilePos()
#     # считаем до него дистанцию по теореме пифагора
#     distance = math.sqrt((x - block_x)**2 + (z - block_z)**2)
#     # выводит ее в консоль
#     print(distance)
#
#     # если дистанция больше 300 - Антарктида
#     if distance >= 300:
#         mc.postToChat("Антарктида")
#     # остальные части запускаем с помощью elif
#     elif distance >= 200:
#         mc.postToChat("Замерзаешь")
#     elif distance >= 150:
#         mc.postToChat("Очень холодно")
#     elif distance >= 100:
#         mc.postToChat("Холодно")
#     elif distance >= 50:
#         mc.postToChat("Тепло")
#     elif distance >= 25:
#         mc.postToChat("Горячо")
#     elif distance >= 10:
#         mc.postToChat("Обожжешься")
#     elif distance <= 1:
#         # если мы в одном блоке от искомого - нужно остановить бесконечный цикл
#         mc.postToChat("Блок найден")
#         # используем брейк чтобы остановить
#         break
#     # добавляем задержку в секунду
#     time.sleep(1)



#
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# import time
# import random
# x, y, z = mc.player.getTilePos()
#
# sveto_kamen = 89 #светокамень
#
# x_block = -409
# y_block = 71
# z_block = -129
# mc.player.setTilePos(-400, 65, -129)
# x_key = -403
# y_key = 77
# z_key = -123
#
# while True:
#     while mc.getBlock(x_key,y_key,z_key) != 57:
#         mc.setBlocks(x_block, y_block, z_block, x_block+5, y_block+5, z_block+5, 1)
#         mc.setBlocks(x_block+1, y_block+1, z_block+1, x_block+4, y_block+4, z_block+4, 0)
#         mc.setBlock(x_block+1, y_block+1, z_block+1,89)
#         mc.setBlock(x_block + 4, y_block + 4, z_block + 4, 89)
#
#     time.sleep(0.1)
#     x_block = -409
#     y_block = 71
#     z_block = -129



#конструкция while-else
# message = input('Введите сообщение:') #прервать
# while message != 'стоп':
#     print(message)
#     message = input('Введите сообщение:') #прервать
#     if message == 'прервать':
#         print('Пользователь прервал чат')
#         break
# else:
#     print('Бот покинул чат')



from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import math
import time


x,y,z = mc.player.getTilePos()

block_x, block_y, block_z = x,y,z

block_x += random.randint(-100, 100)
block_z += random.randint(-100, 100)
block_y = mc.getHeight(block_x, block_z)

block = 57

mc.setBlock(block_x, block_y, block_z, block)

block_create = False

while not block_create:
    if block_y-1 != 8 or block_y-1 != 9:
        mc.setBlock(block_x, block_y, block_z, block)
        block_create = True
        mc.postToChat('Блок создан')

while True:
    x,y,z = mc.player.getTilePos()
    distance = math.sqrt((x - block_x)**2 + (z - block_z)**2)
    print(distance)
    if distance >= 150:
        mc.postToChat('Antarctida')
    elif distance >= 100:
        mc.postToChat('Very cold')
    elif distance >= 50:
        mc.postToChat('cold')
    elif distance >= 30:
        mc.postToChat('Warm')
    elif distance >= 20:
        mc.postToChat('Hot')
    elif distance >= 10:
        mc.postToChat('FIRE')
    elif distance <= 1:
        mc.postToChat('Блок найден')
        count = 0
        while count < 30:
            count += 1
            mc.setBlock(x+random.randint(qq), y+random.randint(-5,5), z+random.randint(-5,5), 57)
        # mc.setBlock(x,y,z,random.randint(57, 57))
        break
    time.sleep(1)








