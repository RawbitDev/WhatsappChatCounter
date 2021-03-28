import codecs

counter = {}
with codecs.open('chat.txt', encoding='utf-8') as f:
    for line in f:
        if line.count(':') >= 2:
            line = line.split(':', 2)[2]
        line = line.strip()
        if not (line.startswith("<") and line.endswith(">")):
            for c in line:
                counter[c] = counter.get(c, 0) + 1

counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
for entry in counter:
    print("'" + entry[0] + "' -> " + str(entry[1]))
