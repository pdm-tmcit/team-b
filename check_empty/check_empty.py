recv=[]
buff=[]


f=open('village_g10_sample_1.csv')
i=1

while True:
	#1行読み取る
	read=f.readline()

	#読み込んで空なら
	#whileから抜ける
	if not read:
		break


	recv=read.split(',');
	#4列目が空か調べる
	if len(recv[3])==0:
		buff.append(i)
	i=i+1

print("空欄:")
print(buff)

f.close()