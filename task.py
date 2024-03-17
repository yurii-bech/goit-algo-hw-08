import heapq

def min_cost_to_connect_cables(cables):
    # Ініціалізуємо список кабелів
    heap = cables[:]
    heapq.heapify(heap)  # Перетворюємо список у піраміду

    total_cost = 0
    while len(heap) > 1:
        # Беремо два найменші кабелі
        shortest1 = heapq.heappop(heap)
        shortest2 = heapq.heappop(heap)

        # Об'єднуємо їх і додаємо витрати до загальної суми
        merged_cable = shortest1 + shortest2
        total_cost += merged_cable

        # Додаємо новий кабель до списку
        heapq.heappush(heap, merged_cable)

    return total_cost

# Приклад використання
cables = [8, 4, 6, 12, 13]
min_cost = min_cost_to_connect_cables(cables)
print(f"Мінімальні витрати на об'єднання кабелів: {min_cost}")