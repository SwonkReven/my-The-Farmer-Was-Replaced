### Скрипт для создания и прохождения лабиринта ###
## Для одного дрона
## Протестирован на поле 32х32, 16х16, 8x8 и 3х3
## по умолчанию дрон создает лабиринт, ищет сокровище, собирает, создает лабиринт снова

import sapport
import lft_v2 # Либа для прохождения лабиринта

clear() # Очистить все поле
# sapport.return_to_home()

# Определяем исходные направления
direction_y = North
direction_x = East

# set_world_size(8)

while True:
	# Бегать лабиринт будем ВЕЧНО
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			## Пробегаем поле вдоль и поперек
			
			# Блок с действиями ->
			# # Если созрело - собираем урожай
			if can_harvest():
				harvest()
			# а тут сажаем:
			plant(Entities.Bush)

			# Блок с перемещением -> 
			# Меняем направление, если дошли до конца поля (по Y)
			if y+1 == get_world_size() and direction_y == North:
				direction_y = South
			elif y+1 == get_world_size():
				direction_y = North
			# шагаем только если не выходим за пределы поля
			if y+1 < get_world_size():
			# if can_move(direction_y): # так правильнее, но мой вариант пока работает лучше
				move(direction_y)
		if x == get_world_size()-1:
					break
		move(direction_x)
	
	sapport.return_to_home() # Возвращаемся в ячейку 0:0
	
	if get_entity_type() != Entities.Hedge: # Если под дроном не лабиринт (там будет куст), то создаем его
		use_item(Items.Weird_Substance, get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1))

	lft_v2.run() # Пробегаем лабиринт, собираем сокровище
	sapport.return_to_home() # Возвращаемся в ячейку 0:0
	# break