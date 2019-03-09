# someone on reddit said since the values were in ASCII
# we could do:
arr = [104, 116, 116, 112, 115, 58, 47, 47, 103, 105, 115, 116,
      46, 103, 105, 116, 104, 117,98, 46, 99, 111, 109, 47, 112,
      121, 100, 97, 110, 110, 121, 47, 97, 56, 55, 100, 57, 54,
      49, 54, 102, 49, 50, 55, 52, 48, 48, 97, 57, 55, 97, 52]

solution = bytearray(arr).decode()

print(solution)