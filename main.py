file_path = 'save.dat'

with open(file_path, 'r') as file:
    data = file.readlines()

data = [line.strip() for line in data]

print(data[4])