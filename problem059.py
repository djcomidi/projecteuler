from string import ascii_lowercase

with open('problem059_cipher1.txt') as in_file:
    # encdata = map(int, in_file.readline()[:-1].split(','))
    encdata = [int(t) for t in in_file.readline()[:-1].split(",")]

# change to 3 to determine key chars
ubound = 0
for i in range(ubound):
    for letter in ascii_lowercase:
        msg = ""
        for c in encdata[i::3]:
            msg += chr(c ^ ord(letter))
        output = "%s, %s" % (letter, msg[:100])
        print(output)

key, decdata = "god", ""
ascii_sum = 0
for i, c in enumerate(encdata):
    decdata += chr(c ^ ord(key[i % len(key)]))
    ascii_sum += ord(decdata[-1])
print(decdata)
print(ascii_sum)
