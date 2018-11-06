import csv
from collections import defaultdict
import pprint
import matplotlib.pyplot as plt

def main():
   
    filename = "data/thads2011.txt"
    headers_idx = defaultdict(str)

    neg = defaultdict(int)
    pos = defaultdict(int)

    with open(filename, 'rt') as csvfile:
        HADS_reader = csv.reader(csvfile, delimiter=',')

        headers = next(HADS_reader)
        for i, header in enumerate(headers):
            headers_idx[header] = i

        for row in HADS_reader:
            burd = float(row[headers_idx['BURDEN']])
            loc = row[headers_idx['METRO3']]
            loc = int(loc.strip("\'"))
            if burd < 0:
                neg[loc] += 1
            else:
                pos[loc] += 1

    neg = dict(neg)
    pos = dict(pos)
    
    METRO = list(sorted(neg.keys()))
    Y = [[],[]]

    for m in METRO:
        Y[0].append(neg[m])
        Y[1].append(pos[m])
    
    width = 0.35
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    negs = ax.bar([location for location in METRO], Y[0], width, color='blue')
    poss = ax.bar([location+width for location in METRO], Y[1], width, color='green')

    plt.show()


if __name__ == "__main__":
    main()
