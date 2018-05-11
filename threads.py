import threading
from time import sleep,ctime

def music(func):
    for i in range(2):
        print("I was listening to %s %s" %(func,ctime()))
        print('-'*50)
        sleep(2)

def move(func):
    for i in range(2):
        print("I was at the %s %s" %(func,ctime()))
        print('-' * 50)
        sleep(5)

def player(name):
    r = name.split('.')[1]
    if r == 'mp3':
        music(name)
    elif r == 'mp4':
        move(name)
    else:
        print("文件格式不对")
threads = []

filename=['pendulum.mp3','Home.mp4','未来世界.mp4']
files = range(len(filename))
for i in files:
    t = threading.Thread(target=player,args=(filename[i],))
    threads.append(t)


if __name__=='__main__':
    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()

print("all end: %s" %ctime())