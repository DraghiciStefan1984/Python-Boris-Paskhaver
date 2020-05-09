# f=open('text.txt', 'r')
# f.close()

# if __name__=='__main__':
#     with open('text.txt', 'r') as f:
#         print('file has been opened')
#         content=f.read()
#         print(content)
#     print('file has been closed')

with open('text.txt', 'r') as f:
    print('file has been opened')
    for line in f:
        print(line)
print('file has been closed')