number = int(input())
words=[]

for i in range(number):
    word = input()
    length = len(word)
    if not ([length,word] in words):
        words.append([length,word])

words.sort()

words = [j for [i,j] in words]

for i in range(len(words)):
    print(words[i])