key = [52, 87, 38, 73, 64, 98, 79, 66, 86, 80, 114, 106, 38, 98, 36, 121, 54, 117, 52, 94, 88, 33, 94, 38, 86, 70, 113,
       48, 115, 69, 98, 48, 73, 94, 107, 83]

enc = [62, 10, 50, 62, 81, 12, 62, 4, 1, 31, 34, 102, 81, 107, 126, 108, 14, 5, 6, 105, 77, 86, 81, 121, 95, 66, 15, 38,
       114, 56, 81, 50, 47, 83, 59, 73]

# reversing the key list
key = key[::-1]

result = []
for i in range(len(enc)):
    result.append(chr(enc[i] ^ key[i]))

print(''.join(result))
