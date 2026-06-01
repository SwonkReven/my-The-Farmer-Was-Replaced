### Дино-змейка шарится к яблоку, а не просто по полю. Потом опишу ###
import sapport

def letsgo():
	target_x, target_y = measure()
	snake_length = 0

	maximum_collection_length = get_world_size()**2
	while snake_length < maximum_collection_length:
		# Используем проверки четности на основе позиции вместо переворачивания переменных
		is_x = get_pos_x() % 2 == 0
		is_y = get_pos_y() % 2 == 0

		if is_x:
			if is_y:
				if target_y < get_pos_y():
					if not move(South):
						move(East)
				else:
					if not move(East):
						move(South)
			else:
				if target_x < get_pos_x():
					if not move(West):
						move(South)
				else:
					if not move(South):
						move(West)
		else:
			if is_y:
				if target_x > get_pos_x():
					if not move(East):
						move(North)
				else:
					if not move(North):
						move(East)
			else:
				if target_y > get_pos_y():
					if not move(North):
						move(West)
				else:
					if not move(West):
						move(North)
		if not can_move(North) and not can_move(South) and not can_move(East) and not can_move(West):
			return 1

		# Обновляем записи о теле и длине змеи
		if measure():
			target_x, target_y = measure()
			snake_length += 1

if __name__ == "__main__":
	# clear()
	change_hat(Hats.Gray_Hat)
	sapport.return_to_home()
	set_world_size(32)
	change_hat(Hats.Dinosaur_Hat)
	# start_time = get_time()

	letsgo()
	# stop_time = get_time()
	# quick_print(start_time,stop_time, stop_time-start_time, get_tick_count())