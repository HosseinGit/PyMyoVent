
import threading

def testThread(num):
    print (num)

"""if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=testThread, args=(i,))
        t.start()"""
import multiprocessing
def spawn(num):
  print(num)

if __name__ == '__main__':
  for i in range(25):
    ## right here
    p = multiprocessing.Process(target=spawn, args=(i,))
    p.start()
    #p.join()