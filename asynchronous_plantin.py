### Скрипт для высаживания и сбора произвольных растений ###
## Использует мульти-дронов # тестился на поле 32х32

import sapport

def drone_example():
	## Функция выполняется рекурсивно, для каждого дрона
	def main():
		## Дрон бесконечно бежит по своей линии, удобряет/поливает землю, собирает урожай и сажает нужные культуры
		while True:
			y = get_pos_y() # текущая позиция в столбце. Нужна далее, если сажаем кактусы, или деревья
			if get_water() < 0.75: # Поливаем
				use_item(Items.Water)
			if get_ground_type()!=Grounds.Soil: # Удобряем
				till()
			if can_harvest() or not get_entity_type() : # Если возможно - собираем урожай (или если ничего не растет)
				harvest()

				# Начинаем сажать всякое (да, внутри проверки на урожай, иначе сажать дрон будет поверх растения, которое еще не выросло)
				plant(Entities.Carrot) # морковка
				# # Дерево/куст - через одного
				# # Если выше что-то сажается, напрмиер, раскомментированная сейчас морковка, то эта посадка не сработает, надо закоммитить морковку
				# if y in range(0,get_world_size()):
				# 	if (y+id)%2==0:
				# 		plant(Entities.Tree)
				# 	else:
				# 		plant(Entities.Bush)

				# # что-то + Кактус через одного. В примере 4 растения: Подсолнух, тыква, морковка, кактус. 
				# # Если выше что-то сажается, напрмиер, раскомментированная сейчас морковка, то эта посадка не сработает, надо закоммитить морковку
				# if y in range(0,get_world_size()):
				# 	if (y+id)%4==0:
				# 		plant(Entities.Sunflower)
				# 	elif (y+id)%4==1:
				# 		plant(Entities.Pumpkin)
				# 	elif (y+id)%4==2:
				# 		plant(Entities.Carrot)
				# 	else:
				# 		plant(Entities.Cactus)

			move(North)

	change_hat(Hats.Purple_Hat) # надеть шляпупу
	id = num_drones() # Присвоить текущему дрону id
	if id != 1 and get_pos_x() != get_world_size()-1: # Если не дрон не оригинал, и не у края поля, то двигаемся вправо
		move(East)
		# move(North)
	if id != max_drones() and get_pos_x() != get_world_size()-1: # Если текущий дрон не макисмальный из возможных и не у края поля
		spawn_drone(drone_example) # спавним еще дронов
	main() # отправляем дрона выполнять основную функцию main
	
if __name__ == "__main__":
	clear() # Чистим поле
	# sapport.return_to_home()
	drone_example() # спавним дронов рекурсивно и выполняем действия
	while num_drones() != 1: # Ждем, пока все дроны не закончат работу
		pass