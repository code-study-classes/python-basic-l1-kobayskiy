load = [10, 50, 20, 80, 30, 90, 40, 60, 10, 20]

smoothed_load = []

for i in range(len(load) - 2):
    window = load[i:i+3]
    average = sum(window) // len(window)
    smoothed_load.append(average)

print(f"Исходная нагрузка: {load}")
print(f"Сглаженный тренд: {smoothed_load}")