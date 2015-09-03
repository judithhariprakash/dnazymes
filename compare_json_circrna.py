import json

with open("dnazyme_sequences_GU.json") as handle:
    datagt = json.load(handle)

with open("dnazyme_sequences.json") as hand:
    agdata = json.load(hand)
common_cid_dnazyme = {}
unique_ag={}
unique_gt = {}
for cid in agdata:
    if cid in datagt:
       common_cid_dnazyme[cid] = (agdata[cid],datagt[cid])
    else:
        unique_ag[cid] = agdata[cid]

for cid in datagt:
    if cid not in agdata:
        unique_gt[cid] = datagt[cid]


print "Unique CIDs in AG: " + str(len(unique_ag))
print "Common CIDs: " + str(len(common_cid_dnazyme))
print "Unique CIDs in Gt: " +str(len(unique_gt))
print "Total CIDs covered:",
print len(unique_ag) + len(common_cid_dnazyme) + len(unique_gt)
with open ('cid_ag_gt_dnazyme.json','w') as handle:
        json.dump(common_cid_dnazyme, handle, indent=2)
with open ('unique_ag_dnazyme.json', 'w') as ha1:
        json.dump(unique_ag, ha1, indent = 2)
with open ('unique_gt_dnazyme.json', 'w') as ha2:
        json.dump(unique_gt, ha2, indent = 2)
