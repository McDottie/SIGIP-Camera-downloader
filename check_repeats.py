import filecmp
import os

filecount = 0
curID = 0

curName1 = None
curName2 = None
curFileName1 = None
curFileName2 = None

paths = os.walk('.')

email = 'Bom dia,\n as cameras '
print(email)
for child in paths:
    # print(child)
    if not child[1] and child[2]:
        if curName1 in child[0] or curName2 in child[0]:
            filecount += 1
            if filecount == 1:
                curFileName1 = child[0] + '\\' + child[2][0]
            else:
                curFileName2 = child[0] + '\\' + child[2][0]

    if filecount == 2:
        filecount = 0
        if filecmp.cmp(curFileName1, curFileName2, shallow=False):       
            #print(curID + '(' + curFileName1 + '),', end =" ")
            print(curID.replace('.\\','') + curFileName1 + ':' + curFileName2)
            #email = email.join(curID + '(' + curFileName1 + '), ')

    if child[1] and not child[2]:
        curID = child[0]
        curName1 = child[1][-1]
        curName2 = child[1][-2]

print('encontram-se sem atualizar imagem.')
#print(filecmp.cmp('1671028212000/N6__9090D_TV00231671028212000.mp4',
#'1671027971000/N6__9090D_TV00231671027971000.mp4', shallow=False))