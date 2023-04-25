from wordinator import Wordinator

var1 = input("str 1: ")
var2 = input("str 2: ")

words = Wordinator(var1, var2)

print("first word")
words.firstWord()
print("big word")
words.bigWord()
print("middle word")
words.middleWords()
print("switch case")
words.switchCase()
print("slice back words")
words.backWordsSlice()
print("manual back words")
words.backWordsManual()




