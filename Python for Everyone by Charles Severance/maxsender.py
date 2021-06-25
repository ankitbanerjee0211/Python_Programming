name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    if line.startswith('From:'):
        email = words[1]
        counts[email] = counts.get(email,0) + 1

maxcount = None
maxsender = None
for email,count in counts.items():
    if maxcount is None or count > maxcount:
        maxcount = count
        maxsender = email

print(maxsender, maxcount)
