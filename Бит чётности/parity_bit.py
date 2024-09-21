def count_of_ones(byte):
    count = 0
    for bit in byte:
        if bit == "1":
            count += 1
    return count

byte = list()
i = 0
while i < 8:
    byte.append(input("Введите 0 или 1: "))
    i += 1
 
if count_of_ones(byte) % 2 == 0:
    byte.append("0")
else:
    byte.append("1")

print(byte)
