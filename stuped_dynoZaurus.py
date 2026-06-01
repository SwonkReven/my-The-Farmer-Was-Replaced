### Тупой динозавр! Тупая змея! 100% прохождение! Занимеат все поле!
### ... Если у вас есть несколько лишних часов...
### PыSы Скрипт работает с размером поля кратным 2 (4х4, 6х6, 8х8, ..., 32х32)
### PыPыSы Тупая змея оказалась не такой уж и тупой. Из-за разгона
# , при выполнении повторяющихся действий и скоращения поля для появления яблока
# , итоговое время прохождения, на карте 32х32
# , получается быстрее, нежели у конкурента - dynoZaurus.py: 
# на поле 16х16 - stuped_dinoZaur = 209.49 сек | dynoZaurus = 117.97 сек
# на поле 18х18 - stuped_dinoZaur = 335.23 сек | dynoZaurus = 149.58 сек
# симуляция на поле 32х32 - stuped_dinoZaur = 2112.66 сек (35.211 мин) | dynoZaurus = 1388.57 (23.143 мин)
# фактическое время на поле 32х32 - stuped_dinoZaur = 2231.5 сек (37.191 мин) | dynoZaurus = не финишировал после 1ч 20 мин, перепроверять не хочу

import sapport

def letsgo():
	# Определяем исходные направления
	direction_y = North
	direction_x = East
	# Пробегаем все поле вверх-вниз, оставляя нижнюю линию пустой, чтоб вернуться по ней
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			# Переопределяем движение 
			if y+1 == get_world_size() and direction_y == North:
				# Если дошли до края поля вверх, начинаем идти вниз
				direction_y = South
			elif get_pos_y() == 1 and direction_y == South:
				# Если дошли до 1 ячейки поля вниз (не 0, а 1), то идем вверх
				direction_y = North
			# шагаем только если не выходим за пределы поля
			if y+1 < get_world_size():
				move(direction_y)
		move(direction_x) # Идем вправо, перемещаясь на новую линию
	move(South) # Прошли поле, значит делаем шаг на короткий пйть домой
	sapport.return_to_home() # и идем домой
	return 1 # счетчик нужен 

if __name__ == "__main__":
	clear()
	# set_world_size(32) # Размеры поля
	sapport.return_to_home() # идем в клетку 0:0
	change_hat(Hats.Dinosaur_Hat) # Надеваем Дино-шляпу
	# start_time = get_time()
	snake_body = 0
	# Пока тело меньше поля - бежим и жрем яблоки
	while snake_body < get_world_size()**2-1:
		snake_body += letsgo()
		if not can_move(North) and not can_move(South) and not can_move(East) and not can_move(West):
			# Если бежать некуда, дино-змей в тупике, то прекращаем бегать
			break
	# change_hat(Hats.Gray_Hat) # Надеваем серую шляпу и собираем кости
	stop_time = get_time()
	# quick_print(start_time,stop_time, stop_time-start_time, get_tick_count())