import os

print("현재운영체제:",os.name)
# nt = 윈도우
# posix = 리눅스

print('현재폴더:',os.getcwd())
print('내부요소:',os.listdir())

'''
#os.mkdir('sample')
#os.rmdir('sample')
with open('original.txt','w') as file:
    file.write('hello python')
os.rename('original.txt', 'newfilename.txt')

os.remove('newfilename.txt')
'''
