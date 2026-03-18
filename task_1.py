import random

rannums = [random.randint(1, 100) for i in range(random.randint(7,10))]
print(f'Исходные баллы: {rannums}')

min_score = min(rannums)
max_score = max(rannums)
print(f'Удаляем минимум ({min_score}) и максимум ({max_score})')

rannums_copy = rannums.copy()

rannums_copy.remove(min_score)
rannums_copy.remove(max_score)
print(f'Оставшиеся баллы: {rannums_copy}')

average = sum(rannums_copy) / len(rannums_copy)
print(f'Средний рейтинг: {average}')