### Скрипт для посадки/сбора укультур ###
## Для одного дрона
## Протестирован на всех размерах поля
import sapport

clear() # Очистить все поле
# sapport.return_to_home()
change_hat(Hats.Green_Hat) # надеть зеленую шляпу

# Список растений для посдаки 
# содержит тип растения и признак, надо ли пахать землю для данного растения 
# напрмер в [Entities.Carrot, 1] - указан тип растения "Морковь" и значение "вспахать поле" = 1 (да, нужно)
# Если сажать растение НЕ нужно, то закомментируйте лишние. Как сейчас закомментирована строка "[Entities.Grass, 0], # Трава"
entities = [
	# [Entities.Grass, 0], # Трава
	[Entities.Bush, 0], # Куст
	[Entities.Carrot, 1], # Морковь
	[Entities.Tree, 0], # Дерево
	[Entities.Pumpkin, 1], # Тыква
	[Entities.Sunflower, 1], # Подсолнух
	[Entities.Cactus, 1], # Кактус
	]

# Определяем исходные направления
direction_y = North
direction_x = East

def we_plant(x, y):
	## Функция вспахивает поле, если надо, сажает растение из списка, удобряет и поливает, если надо
	el = ((x+y) % (len(entities))) # x+y, а не просто x нужно для смещения строк на единицу для каждого столбца (Например, чтоб деревья или кактусы не росли рядом)
	# Если для растения нужна вспаханная земля, а её нет, то пашем
	if entities[el][1] == 1 and get_ground_type() != Grounds.Soil:
			till()			
	# Если для растения нужна НЕ вспаханная земля, а она вспахана, то пашем (меняем состояние)
	elif entities[el][1] == 0 and get_ground_type() == Grounds.Soil:
			till()
	# Сажаем растение, соответствующее текущей позиции
	plant(entities[el][0])
	# we_fertilizer() # !Внимание! Удобрение дает только половину урожая. Если надо удобрять поле, раскомментируёте строку
	we_water() # Поливаем

def we_water():
	## Функция для полива
	while True: # одна поливка не дает 100% влажности. Цикл для полива, чтобподнять влажность до нужного уровня
		if get_water() < 0.5 and num_items(Items.Water) > 100: # Если влажность меньше половины и единиц воды больше 100, то поливаем
			use_item(Items.Water)
		else: # иначе прекращаем поливать
			break

def we_fertilizer():
	## Функция удобрения. Под удобрением растение растет мгновенно, но дает половину урожая + вещество
	#Удобряем и тут же собираем, но только если удобрний больше 100
	if num_items(Items.Fertilizer) > 100:
		use_item(Items.Fertilizer)
		if can_harvest():
			harvest()

if __name__=="__main__":
	set_world_size(6)
	while True:
		## Выполняем ВЕЧЕО
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				## Пробегаем поле вдоль и поперек
				
				# Блок с действиями ->
				# # Если созрело - собираем урожай
				if can_harvest():
					harvest()
				# а тут сажаем:
				we_plant(get_pos_x(), get_pos_y())

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
			# !Временно отключил! Раскомментируйте строки ниже (и закомментируйте строку 92), если хотите красиво передивгаться внутри поля, не выходя за пределы
			# Меняем направление, если дошли до конца поля (по X)
			# if x+1 == get_world_size() and direction_x == East:
			# 	direction_x = West
			# elif x+1 == get_world_size():
			# 	direction_x = East
			# if x+1 < get_world_size():
			# # if can_move(direction_x): # так правильнее, но мой вариант пока работает лучше
			# 	move(direction_x)
			move(direction_x)