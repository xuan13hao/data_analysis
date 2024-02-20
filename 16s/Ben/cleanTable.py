import sys

if len(sys.argv)==2:
    intable = sys.argv[1]
else:
    print("call by ~ <table.tsv>")
    exit()


otu = {}
header = ""
with open(intable, 'r') as fin:
    for line in fin:
        if len(header) == 0:
            header = line
        else:
            context = line.split(',')
            if context[0] not in otu:
                otu[context[0]] = [0] * len(context[1:])
            for (i,it) in enumerate(context[1:]):
                otu[context[0]][i] += int(it)

with open(intable[:intable.rfind('.')]+'.clean.csv','w') as fout:
    fout.write(header)
    for tax in otu:
        fout.write(tax)
        for it in otu[tax]:
            fout.write(',')
            fout.write(str(it))
        fout.write('\n')
