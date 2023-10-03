with open('day_5.txt','r+') as fd :
    print("reading in r+")
    print(fd.read())

with open('day_5.txt','w+') as fd :
    print("reading in w+")
    fd.seek(0)
    print(fd.read())

with open('day_5.txt','r+'):
    print('writing in r+')
    fd.write('new theory')
    fd.seek(0)
    print(fd.read())

with open('sampling_day_5.txt','w+'):
    print('writing in w+')
    fd.write('new theory')
    fd.seek(0)
    print(fd.read())

with open('a.text','r+') as fd:
    pass

with open('b.text','w+') as fd:
    pass