def nolga_ushlash(x):
    try:
        return 1 / x
    except ZeroDivisionError:
        return "Xatolik: Nolga bo'lish xatosi"

print(nolga_ushlash(5))  # 0.2
print(nolga_ushlash(0))  # Xatolik: Nolga bo'lish xatosi
