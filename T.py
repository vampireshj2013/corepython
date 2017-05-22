# -*-coding:utf-8-*-
import os

tmp = r'C:\temp'
if not os.path.isdir(tmp):
    print 'no temp directory available'
    os.mkdir(tmp)

os.chdir(tmp)
print "current work dir :%s" % os.getcwd()

# os.mkdir("example1")
# os.mkdir("example2")
# os.mkdir("example3")

print os.listdir(os.getcwd())

f = open("test.txt", "w+")
f.write("hello world!\n")
f.write("你好!\n")
f.close()
print os.listdir(os.getcwd())

path = os.path.join(os.getcwd(), os.listdir(os.getcwd())[0])
print path
print os.path.split(path)

# os.rmdir(path)
# os.remove('test.txt')
print os.getcwd()
os.rename('test.txt','l.txt')


