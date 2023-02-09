# soldiers = int(input('сколько солдатов в деревне: '))
# zombies = int(input('сколько зомби атакуют нашу деревню: '))
# # if - если
# # если зомби больше чем солдат, тогда выведи
# if zombies > soldiers:
#     print('Деревня погибла')

# login = 'Kanysh'
# password = 'КанышБот'

# attempt = input('Введите пароль: ')
# if password == attempt:
#     print('Вы вошли в аккаунт')


# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()

# pos = mc.player.getTilePos()
# x = pos.x
# y = pos.y
# z = pos.z

# snow = 80

# head = 6
# body = 8
# foot = 10

# mc.setBlocks(x, y, z, x+foot, y+foot, z+foot, snow)
# mc.setBlocks(x+1, y+foot+1, z+1, x+body+1, y+body+foot+1, z+body+1, snow)
# # mc.setBlocks(x, y, z, x+foot, y+foot, z+foot, snow)
# mc.setBlocks(x+1, y+1, z+1, x+foot-1, y+foot-1, z+foot-1, 0)


# from mcpi.minecraft import Minecraft
# mc=Minecraft.create()

# pos = mc.player.getTilePos()
# x = pos.x
# y = pos.y
# z = pos.z
# snow=80
# height=10

# baseheight = 8
# sideHeight = height
# mc.setBlocks(x+1, y+sideHeight+1, z+1, x+baseheight+1, y+baseheight+sideHeight+1, z+baseheight+1, snow)

# # pointHeight = height * 2
# mc.setBlocks(x+1, y, z+1, x+2, y+pointHeight, z+2,snow)


# baseheight = height // 2
# mc.setBlocks(x, y, z, x+sideHeight, y+sideHeight, z+sideHeight, snow)
# # mc.setBlocks(x, y, z, x+foot, y+foot, z+foot, snow)
# # mc.setBlocks(x+1 ,y+foot+1 ,z+1, x+body+1, y+foot+body+1, z+body+1, snow)
# mc.setBlocks(x+2 ,y+sideHeight+baseheight+2 ,z+2, x+6+2, y+sideHeight+baseheight+2, z+6+2, snow)
# # for i in range(100):
# #     print(i)
# while x<100:
#     x = x+1
# x = {asd: 'asd'}
# x = [1,2,3, 'asd', 46]
# from mcpi.minecraft import Minecraft
# mc=Minecraft.create()

# pos = mc.player.getTilePos()
# x = pos.x
# y = pos.y
# z = pos.z
# width=10
# length=10
# height=10

# mc.setBlocks(x, y, z, x+width, y+height, z+length, 4)
# mc.setBlocks(x+1, y+1, z+1, x+width-1, y+height-1, z+length-1, 0)










# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# # print(2)
# pos = mc.player.getTilePos()
# mc.setBlocks(pos.x-5, pos.y, pos.z-5, pos.x+5, pos.y-5, pos.z+5, 0)








# from mcpi.minecraft import Minecraft
# import keyboard

# mc = Minecraft.create()


# def setPillar(x, y, z, height):
#     stairBlock = 156
#     block = 155
#     # Вершина колонны
#     mc.setBlocks(x - 1, y + height, z - 1, x + 1, y + height, z + 1,
#                  block, 1)
#     mc.setBlock(x - 1, y + height - 1, z, stairBlock, 12)
#     mc.setBlock(x + 1, y + height - 1, z, stairBlock, 13)
#     mc.setBlock(x, y + height - 1, z + 1, stairBlock, 15)
#     mc.setBlock(x, y + height - 1, z - 1, stairBlock, 14)
#     # Основание колонны
#     mc.setBlocks(x - 1, y, z - 1, x + 1, y, z + 1, block, 1)
#     mc.setBlock(x - 1, y + 1, z, stairBlock, 0)
#     mc.setBlock(x + 1, y + 1, z, stairBlock, 1)
#     mc.setBlock(x, y + 1, z + 1, stairBlock, 3)
#     mc.setBlock(x, y + 1, z - 1, stairBlock, 2)
#     # Ствол колонны
#     mc.setBlocks(x, y, z, x, y + height, z, block, 2)


# def func():
#     pos = mc.player.getTilePos()
#     x, y, z = pos.x + 2, pos.y, pos.z

#     for i in range(0, 100, 5):
#         setPillar(x + i, y, z, 8)
#         setPillar(x - i, y, z, 8)
#         for j in range(0, 100, 5):
#             setPillar(x, y, z+j, 8)
#             setPillar(x, y, z-j, 8)

# while True:
#     if keyboard.is_pressed('q'):
        # func()


# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()

# answer = 'замок'
# attempt = input('Введите слово: ')

# mc.player.setPos()





# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# import time

# pos = mc.player.getTilePos()

# x = pos.x 
# y = pos.y 
# z = pos.z 


# start_x = 284
# start_y = 87
# start_z = -195
# time.sleep(3)
# mc.player.setTilePos(start_x, start_y+1, start_z)
# time.sleep(0.5)
# mc.player.setTilePos(start_x-1, start_y+2, start_z)
# time.sleep(0.5)
# mc.player.setTilePos(start_x-2, start_y+3, start_z)
# time.sleep(0.5)
# mc.player.setTilePos(start_x-3, start_y+4, start_z)
# time.sleep(0.5)
# mc.player.setTilePos(start_x-4, start_y+5, start_z)
# time.sleep(0.5)
# mc.player.setTilePos(start_x-5, start_y+6, start_z)





# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# import time

# pos = mc.player.getTilePos()
# x = -367
# y = 78
# z = -71


# key_word = 'door'
# attempt = input('Вставьте ключевое слово: ')
# if attempt == key_word:
#         mc.player.setTilePos(x,y,z)
# else:
#         mc.postToChat('wrong answer')

# x = -354
# y = 71 
# z = -106

# gift = mc.getBlock(x, y, z)
# if gift == 41 or gift == 57:
#         mc.setBlock(x,y,z,0)
#         mc.postToChat('HAHAHAHAHA')
# else:
#         mc.setBlock(x,y,z,116)
# x_block = -371
# y_block = 81
# z_block = -68



# x_door = -367
# y_door = 78
# z_door = -67

# # mc.player.setTilePos(x_door, y_door, z_door)

# air = 0

# key = mc.getBlock(x_block, y_block, z_block)

# if key != air:
#         if key == 57:
#                 mc.setBlocks(x_door,y_door,z_door, x_door-2,y_door+2,z_door+2, air)
#         else:
#                 mc.postToChat('Неправильный блок')



print(2)

# gift = mc.getBlock(x_block, y_block, z_block)
# if gift == 57:
#         mc.setBlocks(x_door, y_door, z_door, x_door - 2, y_door + 2, z_door+2, air)
# else:
#         mc.setBlocks(x_door, y_door, z_door, x_door - 2, y_door + 2, z_door+2, 1)
		


# zombies = int(input('Сколько зомби на горизонте: '))
# # zombies = 0 - 10
# if zombies > 30: #more than 30 zombies 
#         print('Нам кирдык, вызывайте северную Корею')
# elif zombies > 10: #10 - 30 zombies
#         print('Дети и старики успеют убежать')
# elif zombies == 0: 
#         print('Ура, можно будет спокойно дома поиграть майнкрафт')
# else: #
#         print('Сейчас разберёмся')


# zombies = int(input('Сколько зомби на горизонте: ')) 
# # zombies = 0 - 10
# if zombies > 10: #False
#         print('Дети и старики успеют убежать') #End
# elif zombies > 30: #more than 30 zombies 
#         print('Нам кирдык, вызывайте северную Корею')
# elif zombies == 0: 
#         print('Ура, можно будет спокойно дома поиграть майнкрафт')
# else: #
#         print('Сейчас разберёмся')


# pigman = 15
# print(pigman>20)
# > == >= < <= != True False



# hasCake = input('У тебя есть торт? Да/Нет ')
# wouldShare = input('Поделишься? Да/Нет ')

# if hasCake == 'Да' and wouldShare == 'Да':
#         print('Ура, покушаем вместе')
# elif hasCake == 'Да' and wouldShare == 'Нет':
#         print('Жадина говядина')
# elif hasCake == 'Нет' and wouldShare == 'Да':
#         print('Спасибо, я был бы рад покушать с тобой, но кушать нечего')
# else:
#         print('Печально')
# if True/False and True/False:
#         print('Ура, покушаем вместе')
# and ---> True
# or ---> False



# hasCake = input('Есть торт? д/н ') 
# hasSamsa = input('Есть самса? д/н ') 
# if hasCake=='д' or hasSamsa=='д':
#         print('Хоть что-то покушаем')

