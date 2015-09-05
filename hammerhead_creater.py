import json
from Bio.Seq import Seq

#opens the json file containing the target sequences 30bp from a window of 15bp
with open("merged_backsplice_sequences15bp.json") as handle:
    data = json.load(handle)

#finds the position of AG or GT and writes to a dictionary with the corresponding cid
def locus_find():
    locusag = {}
    for cid in data:
        for x in range(10,20):
            if data[cid][x] == "A":
                if data[cid][x+1] == "G":
                    locusag[cid] = x
    return locusag


#method to obtain the complement of the target sequence for performing a pairwise alignment to check the dnazyme
"""def split_seq(locus):
    seq_rc = {}
    for cid in locus:
        n = locus[cid]
        left = str(data[cid][n-8:n])
        right = str(data[cid][n:n+8])
        #print "Loci of AG is %d" % n
        #print left, len(left)
        #print right, len(right)
        #print left+ "*" + right
        seq_rc[cid] = Seq(left).complement() + "*" + Seq(right).complement()
        #print data[cid]
        #break"""

# based on the location of the AG or GU sequence, the catalytic core is added
# complement of the adjacent flanking region is obtained with 8bp on either side without complementary to A or the G at the centre

def dnazyme_creater(locus):
    dnazyme = {}
    for cid in locus:
        n = locus[cid]
        catcore = ""
        left = str(data[cid][n-8:n])
        right = str(data[cid][n+1:n+9])
        dzyme = Seq(left).complement() + catcore + Seq(right).complement()
        dnazyme[cid] = str(dzyme)
    return dnazyme

# main function calls the locus find method and saves the resulting dictionary to a variable

if __name__ == '__main__':
    lociat, locigt = locus_find()

# calls the dnazyme_creater method and saves the resulting dictionary to a variable

    dzyme_at = dnazyme_creater(lociat)
    print len(dzyme_gt)

# saves the dictionary of dnazymes into a json file

    with open ('dnazyme_sequences_GU.json','w') as handle:
        json.dump(dzyme_gt, handle, indent=2)


