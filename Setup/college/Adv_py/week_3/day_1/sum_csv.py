import csv
with open('sum.csv') as fin:
    headerline = fin.next()
    total = 0
    for row in csv.reader(fin):
        total += int(row[1])
    print (total)

'''
with open('sum.csv') as fin :
    next(fin)
    total = sum(int(r[1]) for r in csv.reader(fin))
'''    