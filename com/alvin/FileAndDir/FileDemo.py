import os

print(os.getcwd())
print(os.listdir(os.getcwd()))

os.mkdir('E:\python\dir')
print(os.path.isdir('E:\python\dir'))
print(os.path.isfile('E:\python\dir'))
os.rmdir('E:\python\dir')
