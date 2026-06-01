### Вспомогательная либа. Импортируется и вызывается. Просто так не запускается ###
## Либа для прохождения лабиринта. Использует правло правой или левой руки, адаптивно меняет руку

# Установка напрвления движения и руки, по умолчанию
up = North 
hand = East

def right_rod():
	### Фунциия (redefinition of directions) переопределяет напрвления движения и просмотра руки ###
	global up
	global hand
	if up == North:
		up = hand # East
		hand = South
	elif up == East:
		up = hand # South
		hand = West
	elif up == South:
		up = hand # West
		hand = North
	else:
		up = hand # North
		hand = East

def left_rod():
	### Как right_rod только поворачиваемся в другую сторону ###
	global up
	global hand
	if up == North:
		hand = up # North
		up = West 
	elif up == West:
		hand = up # West
		up = South 
	elif up == South:
		hand = up # South
		up = East
	else:
		hand = up # East
		up = North

def go_move():
	# по умолчанию рука = стена справа
	if can_move(up) and not can_move(hand):
		# Если можем двигаться вперед и по руке есть стена, то двигаемся вперед
		move(up)
		return get_pos_x(), get_pos_y()
	elif not can_move(up) and not can_move(hand):
		# Если впереди стена и по руке стена, то поворачиваемся влево (переопределям напрвление движения)
		left_rod()
		move(up)
		return get_pos_x(), get_pos_y()
	else:
		# Иначе, если впереди тупик и по руке нет стены, то вертимся вправо (переопределям напрвление движения)
		right_rod()
		move(up)
		return get_pos_x(), get_pos_y()
	return 1

def run():
	## Функция для пробега лабиринта и сбора сокровища
	go = 1 # флаг для пробега. Нужен был для тестов. Сейчас бесполезен, но особо не занимает память и не мешает, поэтому оставил. Можете убрать, а внутри while поменять на True
	while go: # бежим пока флаг поднят
		go_move() # собственно движение, возвращает координаты, или 1 (нужно было при тестах). Но нам ничего из этого не нужно, поэтому просто вызов
		if get_entity_type() == Entities.Treasure:
			# Если под дроном сокровище - собираем
			harvest()
			go = 0 # снимаем флаг, чтоб не бажть дальше
			return 1

def re_sinding(sh, max):
	# Функция для переиспользования лабиринта. Принимает текущий счетчик кол-ва переиспользований и максимум переиспользований.
	# Если максимум переиспользований еще не достигнут, то пересоздает лабиринт, при нахождении сокровища. Иначе собирает сокровище
	# В остальном, такая же, как run()
	go = 1
	while go:
		one = go_move()
		if get_entity_type() == Entities.Treasure and sh <= max:
			# Если под дроном сокровище и счетчик меньше максимального- собираем
			use_item(Items.Weird_Substance, get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1))
			return 1 # вернуть 1 для счетчика
		elif get_entity_type() == Entities.Treasure and sh > max:
			harvest()
			go = 0
			return 1 # вернуть 1 для счетчика