import sys

print(sys.argv)
word_length=0
for arg in sys.argv[1:]:
    word_length+=len(arg)
print(word_length)