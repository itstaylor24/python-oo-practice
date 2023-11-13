"""Word Finder: finds random words from a dictionary."""

class  Wordfinder:
file = open("words.txt", "r")
my_list = []
for line in file:
    my_list.append(line)
print(my_list)
# file.close()
