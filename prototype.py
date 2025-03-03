size = 10

# Печатаем заголовок
print("  ", end="" + "\n")
for i in range(1, size + 1):
    print("%2X" % i, end="")
print("\n" + "    " + "----" * size)

# Таблица сложения
print("Сложение:")
for i in range(1, size + 1):
    print("%2d |" % i, end="")
    for j in range(1, size + 1):
        print("%4X" % (i + j), end="")
    print()

print()  # Пустая строка для разделения

# Таблица умножения
print("Умножение:")
for i in range(1, size + 1):
    print("%2d |" % i, end="")
    for j in range(1, size + 1):
        print("%4X" % (i * j), end="")
    print()
