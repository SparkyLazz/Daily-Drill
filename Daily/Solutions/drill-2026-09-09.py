def puzzle(array):
  boundary = 0
  for i in range(len(array)):
    if array[i] != 0:
      temp = array[boundary]
      array[boundary] = array[i]
      array[i] = temp
      boundary += 1

data = [0, 0, 0, 1]
puzzle(data)
print(data)
