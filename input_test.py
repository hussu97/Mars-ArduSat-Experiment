import time
for i in range(1,10):
    time.sleep(1)
    f = open('data.csv','a')
    f.write('2,3,4,24,25,{}\n'.format(i*10))
    ## Python will convert \n to os.linesep
    f.close()
