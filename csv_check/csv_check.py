import random
import func

recv=[]
buff=[]
sen=[]
out_morph=[]


f=open('village_g10_sample_1.csv')
w=open('village_g10_sol.csv',mode='w')
i=1

while True:
	#1行読み取る
	read=f.readline()

	#読み込んで空なら
	#whileから抜ける
	if not read:
		break


	recv=read.split(',');
	out_morph=func.morph(recv[1],recv[2],recv[3])

	if(len(recv[3])==0):
		jud=random.randint(1,2)
		if jud==1:
			recv[3]=out_morph[0]+"は"+out_morph[1]+"かもしれない"
		else:
			recv[3]=out_morph[0]+"は"+out_morph[1]+"だと思う"

	sen.append(recv)


"""
for i in range(len(buff)):
	jud=random.randint(1,3)
	if jud==1:
		sen[buff[i]-1][3]="わかりました．"
	elif jud==2:
		sen[buff[i]-1][3]="そうですね．"
	else:
		sen[buff[i]-1][3]="どうでしょう..."
"""
for i in range(len(sen)):
	for j in range(len(sen[i])):
		w.write(sen[i][j])
		if sen[i][j]!='\n':
			w.write(',')
f.close()
w.close()