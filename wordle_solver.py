import string 

file = open("words.txt")
word_list = file.readlines()
#print(len(word_list))

wordle_data = []

for x in range(5):
    wordle_data.append([])
    for char in string.ascii_lowercase:
        wordle_data[x].append(char)
        #print(len(wordle_data[x]))