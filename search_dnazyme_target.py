import json
from Bio.Seq import Seq

with open("merged_backsplice_sequences15bp.json") as handle:
    data = json.load(handle)

def locus_find():
    locus = {}
    locusgu = {}
    for cid in data:
        #for x in range(10,20):
            #if data[cid][x] == "A":
                #if data[cid][x+1] == "G":
                    #locus[cid] = x
        for y in range(10,20):
            if data[cid][y] == "G":
                if data[cid][y+1] == "T":
                    locusgu[cid] = y
    return locusgu
    #split_seq(locus)

#def split_seq(locus):
    #seq_rc = ""
    #for cid in locus:
        #n = locus[cid]
        #left = str(data[cid][n-8:n])
        #right = str(data[cid][n:n+8])
        #print "Loci of AG is %d" % n
        #print left, len(left)
        #print right, len(right)
        #print left+ "*" + right
        #print Seq(left).complement() + "*" + Seq(right).complement()
        #print data[cid]
        #break


def dnazyme_creater(locus):
    dnazyme = {}
    for cid in locus:
        n = locus[cid]
        catcore = "GGCTAGCTACAACGA"
        left = str(data[cid][n-8:n])
        right = str(data[cid][n+1:n+9])
        #print data[cid]
        #print Seq(data[cid]).complement()
        dzyme = Seq(left).complement() + catcore + Seq(right).complement()
        dnazyme[cid] = str(dzyme)
    return dnazyme


if __name__ == '__main__':
    #loci_lib,
    locigu = locus_find()
    #dnazyme_lib = dnazyme_creater(loci_lib)
    dzyme_gu = dnazyme_creater(locigu)
    #print len(dzyme_gu)
    print len(dzyme_gu)
    with open ('dnazyme_sequences_GU.json','w') as handle:
        json.dump(dzyme_gu, handle, indent=2)



