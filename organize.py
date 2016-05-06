import os
from shutil import copyfile, rmtree

if os.path.exists('data'):
    rmtree('data')

os.makedirs('data/train/spam')
os.makedirs('data/train/ham')
os.makedirs('data/test/spam')
os.makedirs('data/test/ham')

files = os.listdir('bare/part1')
spam = [f for f in files if 'spmsg' in f]
ham = [f for f in files if 'spmsg' not in f]

s = 1
h = 1
for j in range(1,11):

    if j is not 10:
        t = 'train'
    else:
        t = 'test'
        s, h = 1, 1

    d = 'bare/part' + str(j) + '/'
    files = os.listdir(d)
    spam = [f for f in files if 'spmsg' in f]
    ham = [f for f in files if 'spmsg' not in f]
    for i in spam:
        copyfile(d + str(i), 'data/'+t+'/spam/'+str(s))
        s+=1
    for i in ham:
        copyfile(d + str(i), 'data/'+t+'/ham/'+str(h))
        h+=1
