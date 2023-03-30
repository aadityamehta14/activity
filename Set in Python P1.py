problem 1
sentence = "Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drik"

# split sentence into list of words

sentence_list = []
words = sentence.split()
sentence_list.extend(words)
print(sentence_list,"\n")

# convert list to set to get unique words

sentence_set = set(sentence_list)
print(sentence_set,"\n")

# print the number of unique words

num_unique = len(sentence_set)
print(num_unique)
