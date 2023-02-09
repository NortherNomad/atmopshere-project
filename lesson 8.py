from mcpi.minecraft import Minecraft
mc=Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
width=100
length=100
height=100

mc.postToChat('Началось')
# mc.setBlocks(x, y, z, x+width, y+height, z+length, 4)
# mc.setBlocks(x+1, y+1, z+1, x+width-1, y+height-1, z+length-1, 0)



# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()

# pos = mc.player.getTilePos()
# x = pos.x
# y = pos.y
# z = pos.z

# length = 100
# #Создаём куб
# # mc.setBlocks(x, y, z, x+length, y+length, z+length, 57)
# #опустошаем куб
# mc.setBlocks(x, y, z, x+3, y+3, z+3, 57)
# mc.setBlocks(x+1, y+1, z+1, x+2, y+2, z+2, 0)

# number1 = 10
# number2 = 20
# if number1 < number2:
#     print('второе число больше')

# login = 'KanyshBot'
# password = 'DavidBot'

# attempt_login = input('Введите логин: ')
# attempt_password = input('Введите пароль: ')

# if attempt_login == login and attempt_password == password:
#     print('Вы вошли в аккаунт')
# elif attempt_login == login and attempt_password != password:
#     print('Неправильный пароль')
# else:
#     print('Неверный логин и/или пароль')


# snegovik = False
# chocolate = False
# nostalgia = False #ЛЮБИМОЕ МОРОЖЕНОЕ
# day_night = False
# if nostalgia:
#     print('возьму настольгию')
# elif chocolate:
#     print('возьму шоколадное')
# elif snegovik:
#     print('возьму snegovik')
# elif day_night:
#     print('возьму day_night')
# else:
#     print('Мороженого нет, в стране кризис')
# print('Конец')

# print(attempt_password == paswword)




# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()

# x = 349
# y = 70
# z = -177
# block = mc.getBlock(x,y,z)
# gold = 41
# diamond = 57
# earth = 3
# plant = 6
# if block == 41 or block == 57:
#     mc.postToChat('Хороший подарок, давай побольше таких')
# elif block == earth or block == plant:
#     mc.postToChat('Плохой подарок, давай другой')
# elif block == 0:
#     mc.setBlock(x, y, z, 80)

# balance = 10000
# snyatiye_deneg = int(input('Сколько хочешь снять: '))
# if snyatiye_deneg <= balance:
#     answer = input('Уверен? Да/Нет')
#     if answer == 'Да':
#         print('успешное снятие денег')
#     else:
#         print('отмена')
# elif snyatiye_deneg > balance:
#     print('Недостаточно денег, иди работай, чёрт')
# balance = 12000
# snyatiye_deneg = int(input('Сколько хочешь снять: ')) # <----- 6000
# # print(snyatiye_deneg)
# if snyatiye_deneg <= balance:
#     answer = input('Уверен? Да/Нет ') #Да
#     if answer == 'Да':
#         print('успешное снятие денег')
#         balance -= snyatiye_deneg
# print(balance)



# x = False
# y = 5.0
# print(type(x))
# print(type(y))

# from multiprocessing.connection import answer_challenge


# try:
#     balance = 0
#     answer = int(input('Сколько денег хочешь закинуть на кошелёк? ')) # <---- пять тысяч
#     balance += answer
#     print('На балансе: ' + str(balance))
# except ValueError:
#     print('Введи число, чёрт')
# mc.postToChat()

# x = 2
# if False:
#     print(x)


# from __future__ import annotations
# from abc import ABC, abstractmethod
# from typing import Any, Optional


# class Handler(ABC):
#     """
#     The Handler interface declares a method for building the chain of handlers.
#     It also declares a method for executing a request.
#     """

#     @abstractmethod
#     def set_next(self, handler: Handler) -> Handler:
#         pass

#     @abstractmethod
#     def handle(self, request) -> Optional[str]:
#         pass


# class AbstractHandler(Handler):
#     """
#     The default chaining behavior can be implemented inside a base handler
#     class.
#     """

#     _next_handler: Handler = None

#     def set_next(self, handler: Handler) -> Handler:
#         self._next_handler = handler
#         # Returning a handler from here will let us link handlers in a
#         # convenient way like this:
#         # monkey.set_next(squirrel).set_next(dog)
#         return handler

#     @abstractmethod
#     def handle(self, request: Any) -> str:
#         if self._next_handler:
#             return self._next_handler.handle(request)

#         return None


# """
# All Concrete Handlers either handle a request or pass it to the next handler in
# the chain.
# """


# class MonkeyHandler(AbstractHandler):
#     def handle(self, request: Any) -> str:
#         if request == "Banana":
#             return f"Monkey: I'll eat the {request}"
#         else:
#             return super().handle(request)


# class SquirrelHandler(AbstractHandler):
#     def handle(self, request: Any) -> str:
#         if request == "Nut":
#             return f"Squirrel: I'll eat the {request}"
#         else:
#             return super().handle(request)


# class DogHandler(AbstractHandler):
#     def handle(self, request: Any) -> str:
#         if request == "MeatBall":
#             return f"Dog: I'll eat the {request}"
#         else:
#             return super().handle(request)


# def client_code(handler: Handler) -> None:
#     """
#     The client code is usually suited to work with a single handler. In most
#     cases, it is not even aware that the handler is part of a chain.
#     """

#     for food in ["Nut", "Banana", "Cup of coffee"]:
#         print(f"\nClient: Who wants a {food}?")
#         result = handler.handle(food)
#         if result:
#             print(f"  {result}", end="")
#         else:
#             print(f"  {food} was left untouched.", end="")


# if __name__ == "__main__":
#     monkey = MonkeyHandler()
#     squirrel = SquirrelHandler()
#     dog = DogHandler()

#     monkey.set_next(squirrel).set_next(dog)

#     # The client should be able to send a request to any handler, not just the
#     # first one in the chain.
#     print("Chain: Monkey > Squirrel > Dog")
#     client_code(monkey)
#     print("\n")

#     print("Subchain: Squirrel > Dog")
#     client_code(squirrel)