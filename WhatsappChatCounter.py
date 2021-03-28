import codecs

messages = 0
chars = 0
counter = {}

with codecs.open('chat.txt', encoding='utf-8') as f:
    for line in f:
        if line.count(':') >= 2:
            line = line.split(':', 2)[2]
        line = line.strip()
        if not (line.startswith("<") and line.endswith(">")):
            messages += 1
            for c in line:
                chars += 1
                counter[c] = counter.get(c, 0) + 1

print(str(messages) + " messages were scanned.")
print(str(chars) + " chars were counted.")

counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
for entry in counter:
    print("'" + entry[0] + "' -> " + str(entry[1]) + " [" + str(round(entry[1]/chars*100, 2)) + "% of all chars]" + " [" + str(round(entry[1]/messages, 3)) + " per message]")
