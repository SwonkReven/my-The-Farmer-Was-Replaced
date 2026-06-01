### Скрипт для высаживания и сортироваки кактусов ###
# испольуюет мульти-дронов х32, на поле 32х32

import sapport

# Создаем матрицу всего поля
all_world = {}

def preparation():
	### Функция создает массив содержащий координаты каждой ячейки и текущее значение зрелости растения (0) ###
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			all_world[0+x, 0+y] = 0

def drone_example_sorting_east():
	# Функция drone_example_sorting_east выполняется рекурсивно, для каждого дрона
	def sorting_cactuses():
		# Основная фнкция сорировки выполняемая дроном
		for y in range(get_world_size()-1):
			## Новоиспеченный дрон пробегает по своей линии вправо 
			# и записывает значения каждого кактуса, для дальнейшей сортировки
			all_world[get_pos_x(), get_pos_y()] = measure()
			move(East)
		run = True # флаг пробега
		while run:
			run = False # снимаем флаг, чтоб дрон остановился после текущей проверки линии
			for x in range(get_world_size()-1):
				## пробегаем линию вправо, смотрим на текущее значение кактуса и на значение кактуса из ячейки слева
				move(East)
				cactus = measure()
				if x > 0 and get_pos_x() > 0: # Если дрон не у границы (значит впереди и сзади есть ячейки)
					if cactus < all_world[get_pos_x()-1, get_pos_y()]: # если в ячейке слева что-то есть
						# Если текущее значение меньше, чем прошлое - меняем местами
						swap(West)
						run = True # поднимаем флаг, чтоб перепроверить линию
						# записываем изменения в мировой словарь
						all_world[get_pos_x(), get_pos_y()] = measure()
						all_world[get_pos_x()-1, get_pos_y()] = cactus

	change_hat(Hats.Gray_Hat) # надеть шляпу
	id = num_drones()
	if id != 1 and get_pos_x() != get_world_size()-1:
		# move(East)
		move(North)
	if id != max_drones() and get_pos_x() != get_world_size()-1:
		spawn_drone(drone_example_sorting_east)
	sorting_cactuses()

def drone_example_sorting_north():
	# Функция drone_example_sorting_north выполняется рекурсивно, для каждого дрона
	def sorting_cactuses():
		for y in range(get_world_size()-1):
			## Новоиспеченный дрон пробегает по своей линии вверх 
			# и записывает значения каждого кактуса, для дальнейшей сортировки
			all_world[get_pos_x(), get_pos_y()] = measure()
			move(North)
		run = True # флаг пробега
		while run:
			run = False # снимаем флаг, чтоб дрон остановился
			# после после текущей проверки линии
			for y in range(get_world_size()-1):
				## пробегаем линию вверх, смотрим на текущее значение кактуса
				# и на значение кактуса из ячейки ниже
				move(North)
				cactus = measure()
				if y > 0 and get_pos_y() > 0: # Если дрон не у границы (значит впереди и сзади есть ячейки)
					if cactus < all_world[get_pos_x(), get_pos_y()-1]: # если в ячейке ниже что-то есть
						# Если текущее значение меньше, чем прошлое - меняем местами
						swap(South)
						run = True # поднимаем флаг, чтоб перепроверить линию
						# записываем изменения в мировой словарь
						all_world[get_pos_x(), get_pos_y()] = measure()
						all_world[get_pos_x(), get_pos_y()-1] = cactus
		
	change_hat(Hats.Gray_Hat) # надеть шляпу
	id = num_drones()
	if id != 1 and get_pos_x() != get_world_size()-1:
		move(East)
		# move(North)
	if id != max_drones() and get_pos_x() != get_world_size()-1:
		spawn_drone(drone_example_sorting_north)
	sorting_cactuses()

def drone_example_harvest():
	def main():
		for i in range(get_world_size()):
			y = get_pos_y()
			if get_water() < 0.75: # Поливаем, если нужно
				use_item(Items.Water)
			if get_ground_type()!=Grounds.Soil: # Удобряем, если надо
				till()
			if can_harvest(): # Если возможно - собираем урожай
				harvest()
			move(North)

	change_hat(Hats.Purple_Hat) # надеть шляпу
	id = num_drones()
	if id != 1 and get_pos_x() != get_world_size()-1:
		move(East)
		# move(North)
	if id != max_drones() and get_pos_x() != get_world_size()-1:
		spawn_drone(drone_example_harvest)
	main()

def drone_example_plants():
	def main():
		for i in range(get_world_size()):
			y = get_pos_y()
			if get_water() < 0.75: # Поливаем, если нужно
				use_item(Items.Water)
			if get_ground_type()!=Grounds.Soil: # Удобряем, если надо
				till()
			# if can_harvest(): # Если возможно - собираем урожай
			# 	harvest()
			plant(Entities.Cactus)
			move(North)

	change_hat(Hats.Green_Hat) # надеть шляпу
	id = num_drones()
	if id != 1 and get_pos_x() != get_world_size()-1:
		move(East)
		# move(North)
	if id != max_drones() and get_pos_x() != get_world_size()-1:
		spawn_drone(drone_example_plants)
	main()

if __name__ == "__main__":
	while True:
		preparation() # Создаем массив "координаты:значение"
		sapport.return_to_home() # возвращаемся в ячейку 0:0
		drone_example_harvest() # множество дронов пробегают все поле и собирают урожай
		# Ждем, пока все дроны не закончат, иначе следующие не заспавнятся в нужном кол-ве
		while num_drones() > 1:
			pass
		drone_example_plants() # множество дронов пробегают все поле и сажают кактусы
		while num_drones() > 1:
			pass
		sapport.return_to_home() # возвращаемся в ячейку 0:0
		drone_example_sorting_east() # множество дронов пробегают поле (каждый по своей строке) и сортируют кактысы на линии в порядке возрастания слева направо
		while num_drones() > 1:
			pass
		sapport.return_to_home() # возвращаемся в ячейку 0:0
		drone_example_sorting_north() # множество дронов пробегают поле (каждый по своему столбцу) и сортируют кактысы на линии в порядке возрастания снизу вверх
		while num_drones() > 1:
			pass