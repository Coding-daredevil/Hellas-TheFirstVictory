###[Buildings]###

source = [
          'C:/Users/DaredevilGR/Documents/Paradox Interactive/Hearts of Iron IV/mod/Hellas/map/',
          'D:/Modding/git/Hellas-TheFirstVictory/map/'
         ]

f = open(source[1]+'buildings.txt', "r")
new_file = []
for x in f:
    try:
        if int(x[:3])>=835:
            new_file.append(x)
    except:
        continue





f.close()
   
f = open(source[1]+"nbuild.txt", "w")
f.write(('').join(new_file))
f.close()

###[Unitstacks]###

source = [
          'C:/Users/DaredevilGR/Documents/Paradox Interactive/Hearts of Iron IV/mod/Hellas/map/',
          'D:/Modding/git/Hellas-TheFirstVictory/map/'
         ]
provid = "841 849 863 895 922 936 966 976 1106 1109 1173 1205 3526 3844 3864 3879 3893 3914 3936 3973 3980 3988 4078 4109 4178 4193 6895 6930 6990 7096 7127 7211 9791 9805 9833 9837 9916 9930 10163 10203 11774 11786 11818 11829 11842 11895 11905 11965 12001 13257 13258 13259 13260 13261 13262 13263 13264 13265 13266 13267 13268 13269 13270 13271 13272 13273 13274 13275"
f = open(source[1]+'unitstacks.txt', "r")
new_file = []
for x in f:
    try:
        if x.split(';')[0] in provid.split(' '):
            new_file.append(x)
    except:
        continue





f.close()
   
f = open(source[1]+"nstacks.txt", "w")
f.write(('').join(new_file))
f.close()


###[Update Unitstacks]###

source1 = 'C:/Users/DaredevilGR/Documents/Paradox Interactive/Hearts of Iron IV/mod/Hellas/map/'
source2 = 'D:/Modding/git/Hellas-TheFirstVictory/map/'
f1 = open(source1+'unitstacks.txt', "r")
f2 = open(source2+'nstacks.txt', "r")
f3 = open(source1+'fstacks.txt', "w")
new_file, dfile = [], {}
for line in f2:
    t = line.split(';')[:2]
    dfile[(';').join(t)] = line


for line in f1:
    t = line.split(';')[:2]
    new_file.append(dfile[(';').join(t)]) if dfile.get((';').join(t), 0) else new_file.append(line)


f3.write(('').join(new_file))
f1.close()
f2.close()
f3.close()

###[Update Buildings]###

source1 = 'C:/Users/DaredevilGR/Documents/Paradox Interactive/Hearts of Iron IV/mod/Hellas/map/'
source2 = 'D:/Modding/git/Hellas-TheFirstVictory/map/'
f1 = open(source1+'buildings.txt', "r")
f2 = open(source2+'buildings.txt', "r")
f3 = open(source1+'fbuildings.txt', "w")
new_file, dfile = [], {}
for line in f2:
    try:
        if int(line.split(';')[0])>=835: 
            dfile[line[:3]] = str(int(line[:3])+74) + line[3:]
            #print(str(int(line[:3])+74) + line[3:])
    except:
        continue


for line in f1:
    new_file.append(dfile[line[:3]]) if dfile.get(line[:3], 0) else new_file.append(line)


f3.write(('').join(new_file))
f1.close()
f2.close()
f3.close()

###[Update Supply Nodes]###

source1 = 'C:/Users/DaredevilGR/Documents/Paradox Interactive/Hearts of Iron IV/mod/Hellas/map/'
source2 = 'D:/Games/Hearts of Iron IV/map/'
f1 = open(source1+'supply_nodes.txt', "r")
f2 = open(source2+'supply_nodes.txt', "r")
f3 = open(source1+'fsupply_nodes.txt', "w")
new_file, dfile = [], {}
for line in f2:
    dfile[line.split(' ')[1]] = 1
    new_file.append(line)


for line in f1:
    if not dfile.get(line.split(' ')[1], 0): new_file.append(line)


f3.write(('').join(new_file))
f1.close()
f2.close()
f3.close()

###[Update Victory Points]###

source1 = 'C:/Users/DaredevilGR/Documents/Paradox Interactive/Hearts of Iron IV/mod/Hellas/map/'
source2 = 'D:/Games/Hearts of Iron IV/map/'
f1 = open(source1+'victory_points_l_english.yml', "r")
f2 = open(source2+'victory_points_l_english.yml', "r")
f3 = open(source1+'fvictory_points_l_english.yml', "w")
new_file, dfile = [], {}
for line in f2:
    dfile[line.split(' ')[1]] = 1
    new_file.append(line)


for line in f1:
    if not dfile.get(line.split(' ')[1], 0): new_file.append(line)


f3.write(('').join(new_file))
f1.close()
f2.close()
f3.close()