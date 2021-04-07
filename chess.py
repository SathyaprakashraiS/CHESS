global check
global mate
global checkmatefunc
white=0

a=[
["BR","BH","BB","BQ","BK","BB","BH","BR"],      #[00,01,02,03,04,05,06,07]
["BP","BP","BP","BP","BP","BP","BP","BP"],		#[10,11,12,13,14,15,16,17]
["  ","  ","  ","  ","  ","  ","  ","  "],		#[20,21,22,23,24,25,26,27]
["  ","  ","  ","  ","  ","  ","  ","  "],		#[30,31,32,33,34,35,36,37]
["  ","  ","  ","  ","  ","  ","  ","  "],		#[40,41,42,43,44,45,46,47]
["  ","  ","  ","  ","  ","  ","  ","  "],		#[50,51,52,53,54,55,56,57]
["WP","WP","WP","WP","WP","WP","WP","WP"],		#[60,61,62,63,64,65,66,67]
["WR","WH","WB","WK","WQ","WB","WH","WR"]		#[70,71,72,73,74,75,76,77]
]

def player1():
	global a
	global white
	flag=0
	move=0
	valid=0
	while(flag!=2):
		flag=0
		while(move!=1):
			white=1
			checkmover=0
			checkmover=check()
			if(checkmover==1):
				#print("CHECK")
				matecheck()
				piecesmi=int(input("ENTER THE POSITION WHERE THE PIECE YOU WANT OT MOVE IS IN"))
				piecesmj=int(input("ENTER THE POSITION WHERE THE PIECE YOU WANT OT MOVE IS IN"))
				if(piecesmi>=0 and piecesmi<=7 and piecesmj>=0 and piecesmj<=7):
					pieces=a[piecesmi][piecesmj]
					#print(pieces)
					if(pieces==" " or pieces[0]=="B"):
						move=0
					else:
						move=1
						flag+=1
					#if(pieces!="WK"):
					#	move=0
					#else:
					#	move=1
					#	flag+=1
			else:
				piecesmi=int(input("ENTER THE POSITION WHERE THE PIECE YOU WANT OT MOVE IS IN"))
				piecesmj=int(input("ENTER THE POSITION WHERE THE PIECE YOU WANT OT MOVE IS IN"))
				if(piecesmi>=0 and piecesmi<=7 and piecesmj>=0 and piecesmj<=7):
					pieces=a[piecesmi][piecesmj]
					if(pieces=="  " or pieces[0]=="B"):
						move=0
					else:
						move=1
						flag+=1
		move=0
		while(move!=1):
			piecesi=int(input("WHAT IS THE POSITION I YOU WANT TO MOVE"))
			piecesj=int(input("WHAT IS THE POSITION J YOU WANT TO MOVE"))
			if(piecesi>=9 and piecesj>=9):
				'''move=0
				flag=0
				checkmover=0
				white=1
				valid=0'''
				return 3
			if(piecesi>=0 and piecesi<=7 and piecesj>=0 and piecesj<=7):
				#a[piecesi][piecesj]=pieces
				tomove=a[piecesi][piecesj]
				if(tomove=="  " or tomove[0]=="B"):
					#white=1
					valid=movetester(pieces,piecesmi,piecesmj,piecesi,piecesj)
					#print("valid value is ",valid)
					if(valid==1):
						temp=a[piecesi][piecesj]
						a[piecesi][piecesj]=pieces
						a[piecesmi][piecesmj]="  "
						checkmover=check()
						#print("check mover is ",checkmover)
						if(checkmover!=1):
							#print("white else nonve")
							valid=0
							move=1
							flag+=1
							return 1
						else:
							move=0
							a[piecesmi][piecesmj]=a[piecesi][piecesj]
							a[piecesi][piecesj]=temp
						#sda
						# valid=0
						#move=1
						#flag+=1
					if(valid>=2):
						#print("HERE2")
						valid=0
						move=1
						flag+=1
						return 1
					#else:
						#print("INVALID MOVE")
						#move=0
				if(tomove[0]=="W"):
					#print("HERE1")
					#print("INVLAID MOVE")
					move=0
			else:
				move=0

def  player2():
	global a
	global white
	flag=0
	move=0
	valid=0
	while(flag!=2):
		flag=0
		while(move!=1):
			white=0
			checkmover=0
			matecheck()
			checkmover=check()
			#print("sdfvihbvihbisibsibu check mover",checkmover)
			if(checkmover==1):
				#print("HALOOLLO")
				piecesmi=int(input("ENTER THE POSITION WHERE THE PIECE YOU WANT OT MOVE IS IN"))
				piecesmj=int(input("ENTER THE POSITION WHERE THE PIECE YOU WANT OT MOVE IS IN"))
				#print("piecesmi and piecesmj is ",piecesmi,piecesmj)
				if(piecesmi>=0 and piecesmi<=7 and piecesmj>=0 and piecesmj<=7):
					pieces=a[piecesmi][piecesmj]
					if(pieces==" " or pieces[0]=="W"):
						move=0
					else:
						move=1
						flag+=1

					#if(pieces=="BK"):
					#	move=1
					#else:
					#	move=0
			else:
				piecesmi=int(input("ENTER THE POSITION WHERE THE PIECE YOU WANT OT MOVE IS IN"))
				piecesmj=int(input("ENTER THE POSITION WHERE THE PIECE YOU WANT OT MOVE IS IN"))
				if(piecesmi>=0 and piecesmi<=7 and piecesmj>=0 and piecesmj<=7):
					pieces=a[piecesmi][piecesmj]
					if(pieces=="  " or pieces[0]=="W"):
						move=0
					else:
						move=1
						flag+=1
		move=0
		while(move!=1):
			piecesi=int(input("WHAT IS THE POSITION I YOU WANT TO MOVE"))
			piecesj=int(input("WHAT IS THE POSITION J YOU WANT TO MOVE"))
			if(piecesi>=9 and piecesj>=9):
				#move=0
				#player2()
				return 3
			if(piecesi>=0 and piecesi<=7 and piecesj>=0 and piecesj<=7):
				#a[piecesi][piecesj]=pieces
				tomove=a[piecesi][piecesj]
				if(tomove=="  " or tomove[0]=="W"):
					white=0
					valid=movetester(pieces,piecesmi,piecesmj,piecesi,piecesj)
					if(valid==1):
						temp=a[piecesi][piecesj]	
						a[piecesi][piecesj]=pieces
						a[piecesmi][piecesmj]="  "
						checkmover=check()
						#print(checkmover)
						if(checkmover!=1):
							#print("test0")
							valid=0
							move=1
							flag+=1
							return 1
						else:
							#print("test1")
							move=0
							a[piecesmi][piecesmj]=a[piecesi][piecesj]
							a[piecesi][piecesj]=temp
					if(valid==2):
						valid=0
						move=1
						flag+=1
						return 1
				if(tomove[0]=="B"):
					print("INVLAID MOVE")
					move=0
			else:
				move=0

def movetester(pieces,piecesmi,piecesmj,piecesi,piecesj):
	global a
	if(pieces=="WR"):
		i=0
		if(piecesi==piecesmi or piecesj==piecesmj):
			if(piecesj==piecesmj):
				flag=0
				if(piecesi>piecesmi):
					i=piecesi
					while(i>piecesmi):
						holder=a[i][piecesmj]
						if(i!=piecesmi):
							if(a[i][piecesmj]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i-=1
					if(flag==0):
						return 1
					else:
						return 0
				if(piecesi<piecesmi):
					i=piecesi
					while(i<piecesmi):
						holder=a[i][piecesmj]
						if(i!=piecesmi):
							if(a[i][piecesmj]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i+=1
					if(flag==0):
						return 1
					else:
						return 0
			if(piecesi==piecesmi):
				flag=0
				if(piecesj>piecesmj):
					i=piecesj
					while(i>piecesmj):
						holder=a[piecesmi][i]
						if(i!=piecesmj):
							if(a[piecesmi][i]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i-=1
					if(flag==0):
						return 1
					else:
						return 0
				if(piecesj<piecesmj):
					i=piecesj
					while(i<piecesmj):
						holder=a[piecesmi][i]
						if(i!=piecesmj):
							if(a[piecesmi][i]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i+=1
					if(flag==0):
						return 1
					else:
						return 0
		else:
			return 0
	if(pieces=="BR"):
		i=0
		if(piecesi==piecesmi or piecesj==piecesmj):
			if(piecesj==piecesmj):
				flag=0
				if(piecesi>piecesmi):
					i=piecesi-1
					while(i>piecesmi):
						holder=a[i][piecesmj]
						if(i!=piecesmi):
							if(a[i][piecesmj]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i-=1
					if(flag==0):
						return 1
				if(piecesi<piecesmi):
					i=piecesi
					while(i<piecesmi):
						holder=a[i][piecesmj]
						if(i!=piecesmi):
							if(a[i][piecesmj]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i+=1
					if(flag==0):
						return 1
			if(piecesi==piecesmi):
				flag=0
				if(piecesj>piecesmj):
					i=piecesj
					while(i>piecesmj):
						holder=a[piecesmi][i]
						if(i!=piecesmj):
							if(a[piecesmi][i]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i-=1
					if(flag==0):
						return 1
				if(piecesj<piecesmj):
					i=piecesj
					while(i<piecesmj):
						holder=a[piecesmi][i]
						if(i!=piecesmj):
							if(a[piecesmi][i]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i+=1
					if(flag==0):
						return 1
		else:
			return 0
	if(pieces=="WH"):
		flag=0
		if(piecesi>piecesmi):
			if(piecesj<piecesmj):
				if((piecesi==piecesmi+2) and (piecesmj==piecesj+1)):
					b=a[piecesi][piecesj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
				if((piecesi==piecesmi+1) and (piecesmj==piecesj+2)):
					b=a[piecesi][piecesj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
			if(piecesj>piecesmj):
				if((piecesi==piecesmi+2) and (piecesj==piecesmj+1)):
					b=a[piecesi][piecesmj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
				if((piecesi==piecesmi+1) and (piecesj==piecesmj+2)):
					b=a[piecesi][piecesj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
		if(piecesi<piecesmi):
			if(piecesj<piecesmj):
				if((piecesmi==piecesi+2) and (piecesmj==piecesj+1)):
					b=a[piecesi][piecesj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
				if((piecesmi==piecesi+1) and (piecesmj==piecesj+2)):
					b=a[piecesi][piecesj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
			if(piecesj>piecesmj):
				if((piecesmi==piecesi+2) and (piecesj==piecesmj+1)):
					b=a[piecesi][piecesj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
				if((piecesmi==piecesi+1) and (piecesj==piecesmj+2)):
					b=a[piecesi][piecesj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
		else:
			return 0
	if(pieces=="BH"):#TO DO TODAY
		flag=0
		if(piecesi>piecesmi):
			if(piecesj<piecesmj):
				if((piecesi==piecesmi+2) and (piecesmj==piecesj+1)):
					b=a[piecesi][piecesj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
				if((piecesi==piecesmi+1) and (piecesmj==piecesj+2)):
					b=a[piecesi][piecesj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
			if(piecesj>piecesmj):
				if((piecesi==piecesmi+2) and (piecesj==piecesmj+1)):
					b=a[piecesi][piecesmj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
				if((piecesi==piecesmi+1) and (piecesj==piecesmj+2)):
					b=a[piecesi][piecesj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
		if(piecesi<piecesmi):
			if(piecesj<piecesmj):
				if((piecesmi==piecesi+2) and (piecesmj==piecesj+1)):
					b=a[piecesi][piecesj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
				if((piecesmi==piecesi+1) and (piecesmj==piecesj+2)):
					b=a[piecesi][piecesj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
			if(piecesj>piecesmj):
				if((piecesmi==piecesi+2) and (piecesj==piecesmj+1)):
					b=a[piecesi][piecesj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
				if((piecesmi==piecesi+1) and (piecesj==piecesmj+2)):
					b=a[piecesi][piecesj]
					if(b[0]=="W"):
						flag+=1
						return 0
					else:
						return 1
		else:
			return 0
	if(pieces=="WB"):
		flag=0
		if(piecesi>piecesmi):
			if(piecesj<piecesmj):
				if((piecesi-piecesmi)==(piecesmj-piecesj)):
					i=piecesmi-1
					j=piecesmj-1
					if( ((piecesi==piecesmi+1) and  (piecesj==piecesmj-1)) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1))  ):
						return 1
					else:
						#for i in range(piecesi):
						while(i<piecesi):
							#for j in range(piecesj,-1):
							while(j>piecesj):
								b=a[i][j]
								if(a[i][j]!=a[piecesi][piecesj]):
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="W"):
										flag+=1
										return 0
								j-=1
							i+=1
							j=piecesmj-1
						if(flag==0):
							return 1
				
		if(piecesi<piecesmi):
			if(piecesj>piecesmj):
				if((piecesmi-piecesi)==(piecesj-piecesmj)):
					i=piecesmi-1
					j=piecesmj+1
					if( ((piecesi==piecesmi+1) and  (piecesj==piecesmj-1)) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1))  ):
						return 1
					else:
					#for i in range(piecesi,-1):
						while(i>piecesi):
							#for j in range(piecesj):
							while(j<piecesj):
								b=a[i][j]
								if(a[i][j]!=a[piecesi][piecesj]):
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="W"):
										flag+=1
										return 0
								j+=1
							i-=1
							j=piecesmj+1
						if(flag==0):
							return 1
				
		if(piecesmi>piecesi):
			if(piecesmj>piecesj):
				if((piecesmi-piecesi)==(piecesmj-piecesj)):
					if(piecesmj!=0 and piecesmi!=0):
						i=piecesmi-1
						j=piecesmj-1
					else:
						if(piecesmi==0):
							i=piecesmi+1
							j=piecesmj-1
						if(piecesmj==0):
							j=piecesmj+1
							i=piecesmi-1
					if( (((piecesi==piecesmi+1) and  (piecesj==piecesmj-1))) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1))  ):
						return 1
					else:
						while(i<piecesi):
							while(j<piecesj):
								b=a[i][j]
								#print(i)
								#print(j)
								if(a[i][j]!=a[piecesi][piecesj]):
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="W"):
										flag+=1
										return 0
								j+=1
								i+=1
							j=piecesmj
						if(flag==0):
							return 1

		if(piecesmi<piecesi):
			if(piecesmj<piecesj):
				if((piecesmi-piecesi)==(piecesmj-piecesj)):
					if(piecesmj!=0 and piecesmi!=0):
						i=piecesmi-1
						j=piecesmj-1
					else:
						if(piecesmi==0):
							i=piecesmi+1
							j=piecesmj-1
						if(piecesmj==0):
							j=piecesmj+1
							i=piecesmi-1
					if( (((piecesi==piecesmi+1) and  (piecesj==piecesmj-1))) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1))  ):
						return 1
					else:
						while(i>piecesi):
							while(j>piecesj):
								b=a[i][j]
								#print(i)
								#print(j)
								if(a[i][j]!=a[piecesi][piecesj]):
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="W"):
										flag+=1
										return 0
								j-=1
								i-=1
							j=piecesmj
						if(flag==0):
							return 1


		else:
			return 0
	if(pieces=="BB"):
		flag=0
		if(piecesi>piecesmi):
			if(piecesj<piecesmj):
				if((piecesi-piecesmi)==(piecesmj-piecesj)):
					if(piecesmj!=0 and piecesmi!=0):
						i=piecesmi-1
						j=piecesmj-1
					else:
						if(piecesmi==0):
							i=piecesmi+1
							j=piecesmj-1
						if(piecesmj==0):
							j=piecesmj+1
							i=piecesmi-1
					if( (((piecesi==piecesmi+1) and  (piecesj==piecesmj-1))) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1))  ):
						return 1
					else:
						#for i in range(piecesi):
						while(i<piecesi):
							#for j in range(piecesj,-1):
							while(j>piecesj):
								b=a[i][j]
								if(a[i][j]!=a[piecesi][piecesj]):
									#print(i)
									#print(j)
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="B"):
										flag+=1
										return 0
								j-=1
								i+=1
							j=piecesmj
						if(flag==0):
							return 1
				
		if(piecesi<piecesmi):
			if(piecesj>piecesmj):
				if((piecesmi-piecesi)==(piecesj-piecesmj)):
					#i=piecesmi
					#j=piecesmj
					if(piecesmj!=0 and piecesmi!=0):
						i=piecesmi-1
						j=piecesmj-1
					else:
						if(piecesmi==0):
							i=piecesmi-1
							j=piecesmj+1
						if(piecesmj==0):
							j=piecesmj-1
							i=piecesmi+1
					if( ((piecesi==piecesmi+1) and  (piecesj==piecesmj-1)) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1))  ):
						return 1
					else:
					#for i in range(piecesi,-1):
						while(i>piecesi):
							#for j in range(piecesj):
							while(j<piecesj):
								b=a[i][j]
								if(a[i][j]!=a[piecesi][piecesj]):
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="B"):
										flag+=1
										return 0
								j+=1
								i-=1
							j=piecesmj
						if(flag==0):
							return 1
#BLACK TOPLEFT RIGHT BOTTOM CODE TO CHECK
		if(piecesmi>piecesi):
			if(piecesmj>piecesj):
				if((piecesmi-piecesi)==(piecesmj-piecesj)):
					if(piecesmj!=0 and piecesmi!=0):
						i=piecesmi-1
						j=piecesmj-1
					else:
						if(piecesmi==0):
							i=piecesmi+1
							j=piecesmj-1
						if(piecesmj==0):
							j=piecesmj+1
							i=piecesmi-1
					if( (((piecesi==piecesmi+1) and  (piecesj==piecesmj-1))) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1))  ):
						return 1
					else:
						while(i<piecesi):
							while(j<piecesj):
								b=a[i][j]
								if(a[i][j]!=a[piecesi][piecesj]):
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="W"):
										flag+=1
										return 0
								j+=1
								i+=1
							j=piecesmj
						if(flag==0):
							return 1

		if(piecesmi<piecesi):
			if(piecesmj<piecesj):
				if((piecesmi-piecesi)==(piecesmj-piecesj)):
					if(piecesmj!=0 and piecesmi!=0):
						i=piecesmi-1
						j=piecesmj-1
					else:
						if(piecesmi==0):
							i=piecesmi+1
							j=piecesmj-1
						if(piecesmj==0):
							j=piecesmj+1
							i=piecesmi-1
					if( (((piecesi==piecesmi+1) and  (piecesj==piecesmj-1))) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1))  ):
						return 1
					else:
						while(i>piecesi):
							while(j>piecesj):
								b=a[i][j]
								if(a[i][j]!=a[piecesi][piecesj]):
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="W"):
										flag+=1
										return 0
								j-=1
								i-=1
							j=piecesmj
						if(flag==0):
							return 1
				
		else:
			return 0
	if(pieces=="WK"):
		holder=a[piecesi][piecesj]
		if(piecesi==piecesmi):
			if(piecesj>piecesmj and ((piecesj-piecesmj)==1)):
				'''if((a[piecesi-1][piecesj]!="BK") and (a[piecesi+1][piecesj]!="BK") and (a[piecesi][piecesj-1]!="BK") and (a[piecesi][piecesj+1]!="BK") and (a[piecesi-1][piecesj+1]!="BK") and (a[piecesi-1][piecesj-1]!="BK") and (a[piecesi+1][piecesj-1]!="BK") and (a[piecesi+1][piecesj+1]!="BK")):
					if((holder=="  " or holder[0]=="B") and holder!="BK"):
						#mate==0
						return 1
					else:
						return 0 '''

				if(piecesi-1>=0 and piecesj-1>=0 and piecesi+1<=7 and piecesj+1<=7):
					#print("testing0")
					if((a[piecesi-1][piecesj]!="BK") and (a[piecesi+1][piecesj]!="BK") and (a[piecesi][piecesj-1]!="BK") and (a[piecesi][piecesj+1]!="BK") and (a[piecesi-1][piecesj+1]!="BK") and (a[piecesi-1][piecesj-1]!="BK") and (a[piecesi+1][piecesj-1]!="BK") and (a[piecesi+1][piecesj+1]!="BK")):
						#print("testing1")
						if((holder=="  " or holder[0]=="B") and holder!="BK"):
							#mate==0
							return 1
						else:
							return 0
				if(piecesi-1>=0 and piecesi+1<=7 and piecesj-1>=0):
					if((a[piecesi-1][piecesj]!="BK") and (a[piecesi+1][piecesj]!="BK") and (a[piecesi][piecesj-1]!="BK") and (a[piecesi-1][piecesj-1]!="BK") and (a[piecesi+1][piecesj-1]!="BK")):
						return 1
					else:
						return 0
				if(piecesi-1>=0 and piecesi+1<=7 and piecesj+1<=7):
					if((a[piecesi-1][piecesj]!="BK") and (a[piecesi+1][piecesj]!="BK") and (a[piecesi][piecesj+1]!="BK") and (a[piecesi-1][piecesj+1]!="BK") and (a[piecesi+1][piecesj+1]!="BK")):
						return 1
					else:
						return 0

				if(piecesj-1>=0 and piecesj+1<=7 and piecesi-1>=0):
					if((a[piecesi-1][piecesj]!="BK") and (a[piecesi-1][piecesj+1]!="BK") and (a[piecesi-1][piecesj-1]!="BK")):
						return 1
					else:
						return 0

				if(piecesj-1>=0 and piecesj+1<=7 and piecesi+1<=7):
					if((a[piecesi+1][piecesj]!="BK") and (a[piecesi+1][piecesj-1]!="BK") and (a[piecesi+1][piecesj+1]!="BK")):
						return 1
					else:
						return 0

			if(piecesmj>piecesj and ((piecesmj-piecesj)==1)):
				if(piecesi-1>=0 and piecesj-1>=0 and piecesi+1<=7 and piecesj+1<=7):
					#print("testing0")
					if((a[piecesi-1][piecesj]!="BK") and (a[piecesi+1][piecesj]!="BK") and (a[piecesi][piecesj-1]!="BK") and (a[piecesi][piecesj+1]!="BK") and (a[piecesi-1][piecesj+1]!="BK") and (a[piecesi-1][piecesj-1]!="BK") and (a[piecesi+1][piecesj-1]!="BK") and (a[piecesi+1][piecesj+1]!="BK")):
						#print("testing1")
						if((holder=="  " or holder[0]=="B") and holder!="BK"):
							#mate==0
							return 1
						else:
							return 0
				if(piecesi-1>=0 and piecesi+1<=7 and piecesj-1>=0):
					if((a[piecesi-1][piecesj]!="BK") and (a[piecesi+1][piecesj]!="BK") and (a[piecesi][piecesj-1]!="BK") and (a[piecesi-1][piecesj-1]!="BK") and (a[piecesi+1][piecesj-1]!="BK")):
						return 1
					else:
						return 0
				if(piecesi-1>=0 and piecesi+1<=7 and piecesj+1<=7):
					if((a[piecesi-1][piecesj]!="BK") and (a[piecesi+1][piecesj]!="BK") and (a[piecesi][piecesj+1]!="BK") and (a[piecesi-1][piecesj+1]!="BK") and (a[piecesi+1][piecesj+1]!="BK")):
						return 1
					else:
						return 0

				if(piecesj-1>=0 and piecesj+1<=7 and piecesi-1>=0):
					if((a[piecesi-1][piecesj]!="BK") and (a[piecesi-1][piecesj+1]!="BK") and (a[piecesi-1][piecesj-1]!="BK")):
						return 1
					else:
						return 0

				if(piecesj-1>=0 and piecesj+1<=7 and piecesi+1<=7):
					if((a[piecesi+1][piecesj]!="BK") and (a[piecesi+1][piecesj-1]!="BK") and (a[piecesi+1][piecesj+1]!="BK")):
						return 1
					else:
						return 0				

		if(piecesj==piecesmj):
			if(piecesi>piecesmi and ((piecesi-piecesmi)==1)):
				if((a[piecesi-1][piecesj]!="BK") and (a[piecesi+1][piecesj]!="BK") and (a[piecesi][piecesj-1]!="BK") and (a[piecesi][piecesj+1]!="BK") and (a[piecesi-1][piecesj+1]!="BK") and (a[piecesi-1][piecesj-1]!="BK") and (a[piecesi+1][piecesj-1]!="BK") and (a[piecesi+1][piecesj+1]!="BK")):
					if((holder=="  " or holder[0]=="B") and holder!="BK"):
						#mate==0
						return 1
					else:
						return 0
			if(piecesmi>piecesi and ((piecesmi-piecesi)==1)):
				if((a[piecesi-1][piecesj]!="BK") and (a[piecesi+1][piecesj]!="BK") and (a[piecesi][piecesj-1]!="BK") and (a[piecesi][piecesj+1]!="BK") and (a[piecesi-1][piecesj+1]!="BK") and (a[piecesi-1][piecesj-1]!="BK") and (a[piecesi+1][piecesj-1]!="BK") and (a[piecesi+1][piecesj+1]!="BK")):
					if((holder=="  " or holder[0]=="B") and holder!="BK"):
						#mate==0
						return 1
					else:
						return 0
		if((piecesi==piecesmi-1) and (piecesj==piecesmj+1)):
			if((a[piecesi-1][piecesj]!="BK") and (a[piecesi+1][piecesj]!="BK") and (a[piecesi][piecesj-1]!="BK") and (a[piecesi][piecesj+1]!="BK") and (a[piecesi-1][piecesj+1]!="BK") and (a[piecesi-1][piecesj-1]!="BK") and (a[piecesi+1][piecesj-1]!="BK") and (a[piecesi+1][piecesj+1]!="BK")):
				if((holder=="  " or holder[0]=="B") and holder!="BK"):
					#mate==0
					return 1
				else:
					return 0
		if((piecesi==piecesmi-1) and (piecesj==piecesmj-1)):
			if((a[piecesi-1][piecesj]!="BK") and (a[piecesi+1][piecesj]!="BK") and (a[piecesi][piecesj-1]!="BK") and (a[piecesi][piecesj+1]!="BK") and (a[piecesi-1][piecesj+1]!="BK") and (a[piecesi-1][piecesj-1]!="BK") and (a[piecesi+1][piecesj-1]!="BK") and (a[piecesi+1][piecesj+1]!="BK")):
				if((holder=="  " or holder[0]=="B") and holder!="BK"):
					#mate==0
					return 1
				else:
					return 0
		if((piecesi==piecesmi+1) and (piecesj==piecesmj-1)):
			if((a[piecesi-1][piecesj]!="BK") and (a[piecesi+1][piecesj]!="BK") and (a[piecesi][piecesj-1]!="BK") and (a[piecesi][piecesj+1]!="BK") and (a[piecesi-1][piecesj+1]!="BK") and (a[piecesi-1][piecesj-1]!="BK") and (a[piecesi+1][piecesj-1]!="BK") and (a[piecesi+1][piecesj+1]!="BK")):
				if((holder=="  " or holder[0]=="B") and holder!="BK"):
					#mate==0
					return 1
				else:
					return 0
		if((piecesi==piecesmi+1) and (piecesj==piecesmj+1)):
			if((a[piecesi-1][piecesj]!="BK") and (a[piecesi+1][piecesj]!="BK") and (a[piecesi][piecesj-1]!="BK") and (a[piecesi][piecesj+1]!="BK") and (a[piecesi-1][piecesj+1]!="WK") and (a[piecesi-1][piecesj-1]!="BK") and (a[piecesi+1][piecesj-1]!="BK") and (a[piecesi+1][piecesj+1]!="BK")):
				if((holder=="  " or holder[0]=="B") and holder!="BK"):
					#mate==0
					return 1
				else:
					return 0
		else:
			return 0
	if(pieces=="BK"):
		holder=a[piecesi][piecesj]
		if(piecesi==piecesmi):
			if(piecesj>piecesmj and ((piecesj-piecesmj)==1)):
				if((a[piecesi-1][piecesj]!="WK") and (a[piecesi+1][piecesj]!="WK") and (a[piecesi][piecesj-1]!="WK") and (a[piecesi][piecesj+1]!="WK") and (a[piecesi-1][piecesj+1]!="WK") and (a[piecesi-1][piecesj-1]!="WK") and (a[piecesi+1][piecesj-1]!="WK") and (a[piecesi+1][piecesj+1]!="WK")):
					if(holder=="  " or holder[0]=="W"):
						#mate==0
						return 1
					else:
						return 0
			if(piecesmj>piecesj and ((piecesmj-piecesj)==1)):
				if((a[piecesi-1][piecesj]!="WK") and (a[piecesi+1][piecesj]!="WK") and (a[piecesi][piecesj-1]!="WK") and (a[piecesi][piecesj+1]!="WK") and (a[piecesi-1][piecesj+1]!="WK") and (a[piecesi-1][piecesj-1]!="WK") and (a[piecesi+1][piecesj-1]!="WK") and (a[piecesi+1][piecesj+1]!="WK")):
					if(holder=="  " or holder[0]=="W"):
						#mate==0
						return 1
					else:
						return 0
		if(piecesj==piecesmj):
			if(piecesi>piecesmi and ((piecesi-piecesmi)==1)):
				if((a[piecesi-1][piecesj]!="WK") and (a[piecesi+1][piecesj]!="WK") and (a[piecesi][piecesj-1]!="WK") and (a[piecesi][piecesj+1]!="WK") and (a[piecesi-1][piecesj+1]!="WK") and (a[piecesi-1][piecesj-1]!="WK") and (a[piecesi+1][piecesj-1]!="WK") and (a[piecesi+1][piecesj+1]!="WK")):
					if(holder=="  " or holder[0]=="W"):
						#mate==0
						return 1
					else:
						return 0
			if(piecesmi>piecesi and ((piecesmi-piecesi)==1)):
				if((a[piecesi-1][piecesj]!="WK") and (a[piecesi+1][piecesj]!="WK") and (a[piecesi][piecesj-1]!="WK") and (a[piecesi][piecesj+1]!="WK") and (a[piecesi-1][piecesj+1]!="WK") and (a[piecesi-1][piecesj-1]!="WK") and (a[piecesi+1][piecesj-1]!="WK") and (a[piecesi+1][piecesj+1]!="WK")):
					if(holder=="  " or holder[0]=="W"):
						#mate==0
						return 1
					else:
						return 0
		if((piecesi==piecesmi-1) and (piecesj==piecesmj+1)):
			if((a[piecesi-1][piecesj]!="WK") and (a[piecesi+1][piecesj]!="WK") and (a[piecesi][piecesj-1]!="WK") and (a[piecesi][piecesj+1]!="WK") and (a[piecesi-1][piecesj+1]!="WK") and (a[piecesi-1][piecesj-1]!="WK") and (a[piecesi+1][piecesj-1]!="WK") and (a[piecesi+1][piecesj+1]!="WK")):
				if(holder=="  " or holder[0]=="W"):
					#mate==0
					return 1
				else:
					return 0
		if((piecesi==piecesmi-1) and (piecesj==piecesmj-1)):
			if((a[piecesi-1][piecesj]!="WK") and (a[piecesi+1][piecesj]!="WK") and (a[piecesi][piecesj-1]!="WK") and (a[piecesi][piecesj+1]!="WK") and (a[piecesi-1][piecesj+1]!="WK") and (a[piecesi-1][piecesj-1]!="WK") and (a[piecesi+1][piecesj-1]!="WK") and (a[piecesi+1][piecesj+1]!="WK")):
				if(holder=="  " or holder[0]=="W"):
					#mate==0
					return 1
				else:
					return 0
		if((piecesi==piecesmi+1) and (piecesj==piecesmj-1)):
			if((a[piecesi-1][piecesj]!="WK") and (a[piecesi+1][piecesj]!="WK") and (a[piecesi][piecesj-1]!="WK") and (a[piecesi][piecesj+1]!="WK") and (a[piecesi-1][piecesj+1]!="WK") and (a[piecesi-1][piecesj-1]!="WK") and (a[piecesi+1][piecesj-1]!="WK") and (a[piecesi+1][piecesj+1]!="WK")):
				if(holder=="  " or holder[0]=="W"):
					#mate==0
					return 1
				else:
					return 0
		if((piecesi==piecesmi+1) and (piecesj==piecesmj+1)):
			if((a[piecesi-1][piecesj]!="WK") and (a[piecesi+1][piecesj]!="WK") and (a[piecesi][piecesj-1]!="WK") and (a[piecesi][piecesj+1]!="WK") and (a[piecesi-1][piecesj+1]!="WK") and (a[piecesi-1][piecesj-1]!="WK") and (a[piecesi+1][piecesj-1]!="WK") and (a[piecesi+1][piecesj+1]!="WK")):
				if(holder=="  " or holder[0]=="W"):
					#mate==0
					return 1
				else:
					return 0
		else:
			return 0
	if(pieces=="WQ"):
		i=0
		flag=0
		if(piecesi==piecesmi or piecesj==piecesmj):
			if(piecesj==piecesmj):
				flag=0
				if(piecesi>piecesmi):
					i=piecesi
					while(i>piecesmi):
						holder=a[i][piecesmj]
						if(i!=piecesmi):
							if(a[i][piecesmj]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i-=1
					if(flag==0):
						return 1
					else:
						return 0
				if(piecesi<piecesmi):
					i=piecesi
					while(i<piecesmi):
						holder=a[i][piecesmj]
						if(i!=piecesmi):
							if(a[i][piecesmj]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i+=1
					if(flag==0):
						return 1
					else:
						return 0
			if(piecesi==piecesmi):
				flag=0
				if(piecesj>piecesmj):
					i=piecesj
					while(i>piecesmj):
						holder=a[piecesmi][i]
						if(i!=piecesmj):
							if(a[piecesmi][i]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i-=1
					if(flag==0):
						return 1
					else:
						return 0
				if(piecesj<piecesmj):
					i=piecesj
					while(i<piecesmj):
						holder=a[piecesmi][i]
						if(i!=piecesmj):
							if(a[piecesmi][i]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i+=1
					if(flag==0):
						return 1
					else:
						return 0

		if(piecesi>piecesmi):
			if(piecesj<piecesmj):
				if((piecesi-piecesmi)==(piecesmj-piecesj)):
					i=piecesmi-1
					j=piecesmj-1
					if( ((piecesi==piecesmi+1) and  (piecesj==piecesmj-1)) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1))  ):
						return 1
					else:
						#for i in range(piecesi):
						while(i<piecesi):
							#for j in range(piecesj,-1):
							while(j>piecesj):
								b=a[i][j]
								if(a[i][j]!=a[piecesi][piecesj]):
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="W"):
										flag+=1
										return 0
								j-=1
							i+=1
							j=piecesmj-1
						if(flag==0):
							return 1
				
		if(piecesi<piecesmi):
			if(piecesj>piecesmj):
				if((piecesmi-piecesi)==(piecesj-piecesmj)):
					i=piecesmi-1
					j=piecesmj+1
					if( ((piecesi==piecesmi+1) and  (piecesj==piecesmj-1)) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1)) ):
						return 1
					else:
					#for i in range(piecesi,-1):
						while(i>piecesi):
							#for j in range(piecesj):
							while(j<piecesj):
								b=a[i][j]
								if(a[i][j]!=a[piecesi][piecesj]):
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="W"):
										flag+=1
										return 0
								j+=1
							i-=1
							j=piecesmj+1
						if(flag==0):
							return 1
				
		if(piecesmi>piecesi):
			if(piecesmj>piecesj):
				#print("ithuva")
				if((piecesmi-piecesi)==(piecesmj-piecesj)):
					if(piecesmj!=0 and piecesmi!=0):
						i=piecesmi-1
						j=piecesmj-1
					else:
						if(piecesmi==0):
							i=piecesmi+1
							j=piecesmj-1
						if(piecesmj==0):
							j=piecesmj+1
							i=piecesmi-1
					if( (((piecesi==piecesmi+1) and  (piecesj==piecesmj-1))) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1))  ):
						return 1
					else:
						while(i<piecesi):
							while(j<piecesj):
								b=a[i][j]
								#print(i)
								#print(j)
								if(a[i][j]!=a[piecesi][piecesj]):
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="W"):
										flag+=1
										return 0
								j+=1
								i+=1
							j=piecesmj
						if(flag==0):
							return 1

		if(piecesmi<piecesi):
			if(piecesmj<piecesj):
				if((piecesmi-piecesi)==(piecesmj-piecesj)):
					if(piecesmj!=0 and piecesmi!=0):
						i=piecesmi-1
						j=piecesmj-1
					else:
						if(piecesmi==0):
							i=piecesmi+1
							j=piecesmj-1
						if(piecesmj==0):
							j=piecesmj+1
							i=piecesmi-1
					if( (((piecesi==piecesmi+1) and  (piecesj==piecesmj-1))) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1))  ):
						return 1
					else:
						while(i>piecesi):
							while(j>piecesj):
								b=a[i][j]
								#print(i)
								#print(j)
								if(a[i][j]!=a[piecesi][piecesj]):
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="W"):
										flag+=1
										return 0
								j-=1
								i-=1
							j=piecesmj
						if(flag==0):
							return 1

		else:
			return 0
	if(pieces=="BQ"):
		i=0
		if(piecesi==piecesmi or piecesj==piecesmj):
			if(piecesj==piecesmj):
				flag=0
				if(piecesi>piecesmi):
					i=piecesi-1
					while(i>piecesmi):
						holder=a[i][piecesmj]
						if(i!=piecesmi):
							if(a[i][piecesmj]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i-=1
					if(flag==0):
						return 1
				if(piecesi<piecesmi):
					i=piecesi
					while(i<piecesmi):
						holder=a[i][piecesmj]
						if(i!=piecesmi):
							if(a[i][piecesmj]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i+=1
					if(flag==0):
						return 1
			if(piecesi==piecesmi):
				flag=0
				if(piecesj>piecesmj):
					i=piecesj
					while(i>piecesmj):
						holder=a[piecesmi][i]
						if(i!=piecesmj):
							if(a[piecesmi][i]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i-=1
					if(flag==0):
						return 1
				if(piecesj<piecesmj):
					i=piecesj
					while(i<piecesmj):
						holder=a[piecesmi][i]
						if(i!=piecesmj):
							if(a[piecesmi][i]!=a[piecesi][piecesj]):
								if(holder[0]=="W" or holder[0]=="B"):
									flag+=1
									return 0
						i+=1
					if(flag==0):
						return 1

		flag=0
		if(piecesi>piecesmi):
			if(piecesj<piecesmj):
				if((piecesi-piecesmi)==(piecesmj-piecesj)):
					if(piecesmj!=0 and piecesmi!=0):
						i=piecesmi-1
						j=piecesmj-1
					else:
						if(piecesmi==0):
							i=piecesmi+1
							j=piecesmj-1
						if(piecesmj==0):
							j=piecesmj+1
							i=piecesmi-1
					if( (((piecesi==piecesmi+1) and  (piecesj==piecesmj-1))) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1))  ):
						return 1
					else:
						#for i in range(piecesi):
						while(i<piecesi):
							#for j in range(piecesj,-1):
							while(j>piecesj):
								b=a[i][j]
								if(a[i][j]!=a[piecesi][piecesj]):
									#print(i)
									#print(j)
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="B"):
										flag+=1
										return 0
								j-=1
								i+=1
							j=piecesmj
						if(flag==0):
							return 1
				
		if(piecesi<piecesmi):
			if(piecesj>piecesmj):
				if((piecesmi-piecesi)==(piecesj-piecesmj)):
					#i=piecesmi
					#j=piecesmj
					if(piecesmj!=0 and piecesmi!=0):
						i=piecesmi-1
						j=piecesmj-1
					else:
						if(piecesmi==0):
							i=piecesmi-1
							j=piecesmj+1
						if(piecesmj==0):
							j=piecesmj-1
							i=piecesmi+1
					if( ((piecesi==piecesmi+1) and  (piecesj==piecesmj-1)) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1))  ):
						return 1
					else:
					#for i in range(piecesi,-1):
						while(i>piecesi):
							#for j in range(piecesj):
							while(j<piecesj):
								b=a[i][j]
								if(a[i][j]!=a[piecesi][piecesj]):
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="B"):
										flag+=1
										return 0
								j+=1
								i-=1
							j=piecesmj
						if(flag==0):
							return 1
#BLACK TOPLEFT RIGHT BOTTOM CODE TO CHECK
		if(piecesmi>piecesi):
			if(piecesmj>piecesj):
				if((piecesmi-piecesi)==(piecesmj-piecesj)):
					if(piecesmj!=0 and piecesmi!=0):
						i=piecesmi-1
						j=piecesmj-1
					else:
						if(piecesmi==0):
							i=piecesmi+1
							j=piecesmj-1
						if(piecesmj==0):
							j=piecesmj+1
							i=piecesmi-1
					if( (((piecesi==piecesmi+1) and  (piecesj==piecesmj-1))) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1))  ):
						return 1
					else:
						while(i<piecesi):
							while(j<piecesj):
								b=a[i][j]
								if(a[i][j]!=a[piecesi][piecesj]):
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="B"):
										flag+=1
										return 0
								j+=1
								i+=1
							j=piecesmj
						if(flag==0):
							return 1

		if(piecesmi<piecesi):
			if(piecesmj<piecesj):
				if((piecesmi-piecesi)==(piecesmj-piecesj)):
					if(piecesmj!=0 and piecesmi!=0):
						i=piecesmi-1
						j=piecesmj-1
					else:
						if(piecesmi==0):
							i=piecesmi+1
							j=piecesmj-1
						if(piecesmj==0):
							j=piecesmj+1
							i=piecesmi-1
					if( (((piecesi==piecesmi+1) and  (piecesj==piecesmj-1))) or ((piecesi==piecesmi-1) and  (piecesj==piecesmj+1))  ):
						return 1
					else:
						while(i>piecesi):
							while(j>piecesj):
								b=a[i][j]
								if(a[i][j]!=a[piecesi][piecesj]):
									if(b[0]=="W" or b[0]=="B"):
										flag+=1
										return 0
								else:
									if(b[0]=="B"):
										flag+=1
										return 0
								j-=1
								i-=1
							j=piecesmj
						if(flag==0):
							return 1

		else:
			return 0
	if(pieces=="WP"):
		#print("HELO")
		holder=a[piecesi][piecesj]
		between=a[piecesmi-1][piecesmj]
		if(piecesj==piecesmj):
			if(piecesmi == (piecesi+1)):
				if(a[piecesi][piecesj]=="  "):
					return 1
				else:
					return 0

			if(piecesmi==(piecesi+2)):
				if(a[piecesi-1][piecesj]=="  " and a[piecesi][piecesj]=="  "):
					return 1
				else:
					return 0
				
		if((piecesmi==(piecesi+1)) and (piecesmj==(piecesj+1))):
			if(holder[0]=="B"):
				return 1
			else:
				return 0
		if((piecesmi==(piecesi+1)) and (piecesmj==(piecesj-1))):
			if(holder[0]=="B"):
				return 1
			else:
				return 0
		#NOT CONFIRMED
		#elif(piecesi==0):
		#	if(a[piecesi][piecesj]=="  "):
		#		a[piecesi][piecesj]="WQ"
		#		a[piecesmi][piecesmj]="  "
		#		return 2
		else:
			return 0

	if(pieces=="BP"):
		holder=a[piecesi][piecesj]
		between=a[piecesmi-1][piecesmj]
		if(piecesj==piecesmj):
			if(piecesmi == (piecesi-1)):
				if(a[piecesi][piecesj]=="  "):
					return 1
				else:
					return 0

			if(piecesmi==(piecesi-2)):
				if(a[piecesi-1][piecesj]=="  " and a[piecesi][piecesj]=="  "):
					return 1
				else:
					return 0
				
		if((piecesmi==(piecesi-1)) and (piecesmj==(piecesj+1))):
			if(holder[0]=="W"):
				return 1
			else:
				return 0
		if((piecesmi==(piecesi-1)) and (piecesmj==(piecesj-1))):
			if(holder[0]=="W"):
				return 1
			else:
				return 0

		#NOT CONFIRED
		#elif(piecesi==7):
		#	a[piecesi][piecesj]="BQ"
		#	a[piecesmi][piecesmj]="  "
		#	return 2

		else:
			if((piecesmi-piecesi)==-1 and holder[0]=="W"):
				if((piecesmj==(piecesj-1)) or (piecesmj==(piecesmj+1))):
					return 1
				else:
					return 0
			else:
				return 0
def check():
	global white
	whitecheck=0
	blackcheck=0
	global checkmatefunc
	
	for i in range(8):
		for j in range(8):
			if(white==1):
				if(a[i][j]=="WK"):
					herei=i
					herej=j
					#print("king at",herei,herej)
					#display()
					break
			if(white==0):
				if(a[i][j]=="BK"):
					#print("black king @")
					herei=i
					herej=j
					#print(herei,herej)
					break
	#CHECK CHECK FOR WHITE
	if(white==1):
		flag=0
		if((a[herei-2][herej+1]=="BH") or (a[herei-1][herej+2]=="BH") or (a[herei-2][herej-1]=="BH") or (a[herei-1][herej-2]=="BH") or (a[herei-1][herej+1]=="BP") or (a[herei-1][herej-1]=="BP")):
			#display()
			#print("horse found and the king was at ",herei,herej)
			return 1
		else:
			whitecheck+=0
		i=herei-1
		while(i<herei and i>=0):
			holder=a[i][herej]
			if(a[i][herej]=="BR" or a[i][herej]=="BQ"):
				#return 1
				whitecheck+=1
			if(a[i][herej]!="BR" and a[i][herej]!="BQ" and a[i][herej]!="  "):
				break
			if(holder[0]=="W"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			#flag+=1
			i-=1
		#if(flag!=0):
		#if(inbetween!=0):
		#	return 0
		if(whitecheck!=0):
			return 1
		i=herei+1
		while(i<=7):
			holder=a[i][herej]
			if(a[i][herej]=="BR" or a[i][herej]=="BQ"):
				#return 1
				whitecheck+=1
			if(a[i][herej]!="BR" and a[i][herej]!="BQ" and a[i][herej]!="  "):
				break
			if(holder[0]=="W"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			flag+=1
			i+=1
		#if(flag!=0):
		if(whitecheck!=0):
			return 1
		j=herej-1
		while(i<herej and i>=0):
			holder=a[herei][j]
			if(a[herei][j]=="BR" or a[herei][j]=="BQ"):
				#return 1
				whitecheck+=1
			if(a[herei][j]!="BR" and a[herei][j]!="BQ" and a[herei][j]!="  "):
				break
			if(holder[0]=="W"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			flag+=1
			i-=1
		#if(flag!=0):
		if(whitecheck!=0):
			return 1
		j=herej+1
		while(j<=7 and j>herej):
			holder=a[herei][j]
			if(a[herei][j]=="BR" or a[herei][j]=="BQ"):
				#return 1
				whitecheck+=1
			if(a[herei][j]!="BR" and a[herei][j]!="BQ" and a[herei][j]!="  "):
				break
			if(holder[0]=="W"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			flag+=1
			j+=1
		#if(flag!=0):
		if(whitecheck!=0):
			return 1
		i=herei-1
		j=herej-1
		while(i<herei and j<herej and i>=0 and j>=0):
			holder=a[i][j]
			if(a[i][j]=="BQ" or a[i][j]=="BB"):
				#return 1
				whitecheck+=1
			if(a[i][j]!="BQ" and a[i][j]!="BB" and a[i][j]!="  "):
				break
			if(holder[0]=="W"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			flag+=1
			i-=1
			j-=1
		#if(flag!=0):
		if(whitecheck!=0):
			return 1
		i=herei+1
		j=herej+1
		while(i<=7 and j<=7 and i>herei and j>herej):
			holder=a[i][j]
			if(a[i][j]=="BQ" or a[i][j]=="BB"):
				#return 1
				whitecheck+=1
			if(a[i][j]!="BQ" and a[i][j]!="BB" and a[i][j]!="  "):
				break
			if(holder[0]=="W"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			flag+=1
			i+=1
			j+=1
		#if(flag!=0):
		if(whitecheck!=0):
			return 1
		i=herei-1
		j=herej+1
		while(i<herei and i>=0 and j>herej and j<=7):
			holder=a[i][j]
			if(a[i][j]=="BQ" or a[i][j]=="BB"):
				#return 1
				whitecheck+=1
			if(a[i][j]!="BQ" and a[i][j]!="BB" and a[i][j]!="  "):
				break
			if(holder[0]=="W"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			flag+=1
			i-=1
			j+=1
		#if(flag!=0):
		if(whitecheck!=0):
			return 1
		i=herei+1
		j=herej-1
		while(i<=7 and i>herei and j>=0 and j<herej):
			holder=a[i][j]
			if(a[i][j]=="BQ" or a[i][j]=="BB"):
				#return 1
				whitecheck+=1
			if(a[i][j]!="BQ" and a[i][j]!="BB" and a[i][j]!="  "):
				break
			if(holder[0]=="W"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			flag+=1
			i+=1
			j-=1
		#if(flag!=0):
	if(white==1):
		if(whitecheck!=0):
			return 1
		else:
			return 0
	
		#CHECK CHECK FOR BLACK
	if(white==0):
		#print("TEST LOC asdasd  asa sdasd  asd")
		flag=0
		'''if((a[herei-2][herej+1]=="WH") or (a[herei-1][herej+2]=="WH") or (a[herei-2][herej-1]=="WH") or (a[herei-1][herej-2]=="WH") or (a[herei-1][herej+1]=="WP") or (a[herei-1][herej-1]=="WP")):
			print("123")
			return 1'''
		#conitinue here
		i=herei-1
		while(i<herei and i>=0):
			holder=a[i][herej]
			if(a[i][herej]=="WR" or a[i][herej]=="WQ"):
				#return 1
				#print("TEST LOC0")
				whitecheck+=1
			if(a[i][herej]!="WR" and a[i][herej]!="WQ" and a[i][herej]!="  "):
				break
			if(holder[0]=="B"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			#flag+=1
			i-=1
		#if(flag!=0):
		#if(inbetween!=0):
		#	return 0
		if(whitecheck!=0):
			return 1
		i=herei+1
		while(i<=7):
			holder=a[i][herej]
			if(a[i][herej]=="WR" or a[i][herej]=="WQ"):
				#print("TEST LOC1")
				#return 1
				whitecheck+=1
			if(a[i][herej]!="WR" and a[i][herej]!="WQ" and a[i][herej]!="  "):
				break
			if(holder[0]=="B"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			flag+=1
			i+=1
		#if(flag!=0):
		if(whitecheck!=0):
			return 1
		j=herej-1
		while(i<herej and i>=0):
			holder=a[herei][j]
			if(a[herei][j]=="WR" or a[herei][j]=="WQ"):
				#print("TEST LOC2")
				#return 1
				whitecheck+=1
			if(a[herei][j]!="WR" and a[herei][j]!="WQ" and a[herei][j]!="  "):
				break
			if(holder[0]=="B"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			flag+=1
			i-=1
		#if(flag!=0):
		if(whitecheck!=0):
			return 1
		j=herej+1
		while(j<=7 and j>herej):
			holder=a[herei][j]
			if(a[herei][j]=="WR" or a[herei][j]=="WQ"):
				#print("TEST LOC3")
				#return 1
				whitecheck+=1
			if(a[herei][j]!="WR" and a[herei][j]!="WQ" and a[herei][j]!="  "):
				break
			if(holder[0]=="B"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			flag+=1
			j+=1
		#if(flag!=0):
		if(whitecheck!=0):
			return 1
		i=herei-1
		j=herej-1
		while(i<herei and j<herej and i>=0 and j>=0):
			holder=a[i][j]
			if(a[i][j]=="WQ" or a[i][j]=="WB"):
				#print("TEST LOC4")
				#return 1
				whitecheck+=1
			if(a[i][j]!="WQ" and a[i][j]!="WB" and a[i][j]!="  "):
				break
			if(holder[0]=="B"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			flag+=1
			i-=1
			j-=1
		#if(flag!=0):
		if(whitecheck!=0):
			return 1
	

		i=herei+1
		j=herej+1
		while(i<=7 and j<=7 and i>herei and j>herej):
			holder=a[i][j]
			if(a[i][j]=="WQ" or a[i][j]=="WB"):
				#print("TEST LOC5")
				#return 1
				whitecheck+=1
			if(a[i][j]!="WQ" and a[i][j]!="WB" and a[i][j]!="  "):
				break
			if(holder[0]=="B"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			flag+=1
			i+=1
			j+=1
		#if(flag!=0):
		if(whitecheck!=0):
			return 1
		
		i=herei-1
		j=herej+1
		while(i<herei and i>=0 and j>herej and j<=7):
			holder=a[i][j]
			if(a[i][j]=="WQ" or a[i][j]=="WB"):
				#print("TEST LOC6")
				#return 1
				whitecheck+=1
			if(a[i][j]!="WQ" and a[i][j]!="WB" and a[i][j]!="  "):
				break
			if(holder[0]=="B"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			flag+=1
			i-=1
			j+=1
		#if(flag!=0):
		if(whitecheck!=0):
			return 1
		

		i=herei+1
		j=herej-1
		while(i<=7 and i>herei and j>=0 and j<herej):
			holder=a[i][j]
			if(a[i][j]=="WQ" or a[i][j]=="WB"):
				#print("TEST LOC7")
				#return 1
				whitecheck+=1
			if(a[i][j]!="WQ" and a[i][j]!="WB" and a[i][j]!="  "):
				break
			if(holder[0]=="B"):
				#return 0
				whitecheck+=0
			else:
				whitecheck+=0
			flag+=1
			i+=1
			j-=1
		#if(flag!=0):
	if(white==0):
		if(whitecheck!=0):
			return 1
		else:
			return 0

def matecheck():
	global state
	'''
	check all eight box use check() funtion and return ans and check it 
	if check by horse check if theere is any pieces to take the horse out .this is done using movetester func
	if pieces is not horse 
	if the pieces is bishop rook or queen then check if there is any other piece near to that piece to take it out
	'''
	global white
	valid=0
	matetest=0
	nomove=0
	for i in range(8):
		for j in range(8):
			if(white==1):#white
				if(a[i][j]=="WK"):
					posi=i
					posj=j
			if(white==0):#black
				if(a[i][j]=="BK"):
					posi=i
					posj=j
					#print("actuall balck king at ",posi,posj)
	
	#BLOCK 1
	if(white==1):
		if(posi-1>=0 and posj+1<=7):
			a[posi][posj]="  "
			temp=a[posi-1][posj+1]
			a[posi-1][posj+1]="WK"
			tposi=posi-1
			tposj=posj+1
			valid=blockcheck(posi,posj,tposi,tposj)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
				#return 1
				matetest+=0
		else:
			matetest+=1
		
		#BLOCK 2
		if(posi-1>=0):
			a[posi][posj]="  "
			temp=a[posi-1][posj]
			a[posi-1][posj]="WK"
			tposi=posi-1
			tposj=posj
			valid=blockcheck(posi,posj,tposi,tposj)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
				#return 1
				matetest+=0
		else:
			matetest+=1


		#BLOCK 3
		if(posi-1>=0 and posj-1>=0):
			a[posi][posj]="  "
			temp=a[posi-1][posj-1]
			a[posi-1][posj-1]="WK"
			tposi=posi-1
			tposj=posj-1
			valid=blockcheck(posi,posj,tposi,tposj)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
				#return 1
				matetest+=0
		else:
			matetest+=1


		#BLOCK 4
		if(posi>=0 and posj-1>=0):
			a[posi][posj]="  "
			temp=a[posi][posj-1]
			a[posi][posj-1]="WK"
			tposi=posi
			tposj=posj-1
			valid=blockcheck(posi,posj,tposi,tposj)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
				#return 1
				matetest+=0
		else:
			matetest+=1


		#BLOCK 5
		if(posi>=0 and posj+1<=7):
			a[posi][posj]="  "
			temp=a[posi][posj+1]
			a[posi][posj+1]="WK"
			tposi=posi
			tposj=posj+1
			valid=blockcheck(posi,posj,tposi,tposj)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
				#return 1
				matetest+=0
		else:
			matetest+1


		#BLOCK 6
		if(posi+1<=7 and posj-1>=0):
			a[posi][posj]="  "
			temp=a[posi+1][posj-1]
			a[posi+1][posj-1]="WK"
			tposi=posi+1
			tposj=posj-1
			valid=blockcheck(posi,posj,tposi,tposj)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
				#return 1
				matetest+=0
		else:
			matetest+=1

		#BLOCK 7
		if(posi+1<=7 and posj<=7):
			a[posi][posj]="  "
			temp=a[posi+1][posj]
			a[posi+1][posj]="WK"
			tposi=posi+1
			tposj=posj
			valid=blockcheck(posi,posj,tposi,tposj)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
				#return 1
				matetest+=0
		else:
			matetest+=1


		#BLOCK 8
		if(posi+1<=7 and posj+1<=7):
			a[posi][posj]="  "
			temp=a[posi+1][posj+1]
			a[posi+1][posj+1]="WK"
			tposi=posi+1
			tposj=posj+1
			valid=blockcheck(posi,posj,tposi,tposj)
			#print("the valid is ",valid)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="WK"
				valid=0
				#return 1
				matetest+=0
		#print("Helo the amtetest value is ",matetest)
		if(matetest>=8):
			#print("your matetest value ",matetest)
			print("GAME OVER BLACK WINS")
			exit()
	if(white==0):
		#print("blackchecmatecheck")
		if(posi-1>=0 and posj+1<=7):
			#print("mate0")
			a[posi][posj]="  "
			temp=a[posi-1][posj+1]
			a[posi-1][posj+1]="BK"
			tposi=posi-1
			tposj=posj+1
			valid=blockcheckb(posi,posj,tposi,tposj)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
				#return 1
				matetest+=0
		else:
			matetest+=1
		
		#BLOCK 2
		if(posi-1>=0):
			#print("mate0")
			a[posi][posj]="  "
			temp=a[posi-1][posj]
			a[posi-1][posj]="BK"
			tposi=posi-1
			tposj=posj
			valid=blockcheckb(posi,posj,tposi,tposj)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
				#return 1
				matetest+=0
		else:
			matetest+=1


		#BLOCK 3
		if(posi-1>=0 and posj-1>=0):
			#print("mate0")
			a[posi][posj]="  "
			temp=a[posi-1][posj-1]
			a[posi-1][posj-1]="BK"
			tposi=posi-1
			tposj=posj-1
			valid=blockcheckb(posi,posj,tposi,tposj)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
				#return 1
				matetest+=0
		else:
			matetest+=1


		#BLOCK 4
		if(posi>=0 and posj-1>=0):
			#print("mate0")
			a[posi][posj]="  "
			temp=a[posi][posj-1]
			a[posi][posj-1]="BK"
			tposi=posi
			tposj=posj-1
			valid=blockcheckb(posi,posj,tposi,tposj)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
				#return 1
				matetest+=0
		else:
			matetest+=1


		#BLOCK 5
		if(posi>=0 and posj+1<=7):
			#print("mate0")
			a[posi][posj]="  "
			temp=a[posi][posj+1]
			a[posi][posj+1]="BK"
			tposi=posi
			tposj=posj+1
			valid=blockcheckb(posi,posj,tposi,tposj)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
				#return 1
				matetest+=0
		else:
			matetest+1


		#BLOCK 6
		if(posi+1<=7 and posj-1>=0):
			#print("mate0")
			a[posi][posj]="  "
			temp=a[posi+1][posj-1]
			a[posi+1][posj-1]="BK"
			tposi=posi+1
			tposj=posj-1
			valid=blockcheckb(posi,posj,tposi,tposj)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
				#return 1
				matetest+=0
		else:
			matetest+=1

		#BLOCK 7
		if(posi+1<=7 and posj<=7):
			#print("mate0")
			a[posi][posj]="  "
			temp=a[posi+1][posj]
			a[posi+1][posj]="BK"
			tposi=posi+1
			tposj=posj
			valid=blockcheckb(posi,posj,tposi,tposj)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
				#return 1
				matetest+=0
		else:
			matetest+=1


		#BLOCK 8
		if(posi+1<=7 and posj+1<=7):
			#print("mate0")
			a[posi][posj]="  "
			temp=a[posi+1][posj+1]
			a[posi+1][posj+1]="BK"
			tposi=posi+1
			tposj=posj+1
			valid=blockcheckb(posi,posj,tposi,tposj)
			#print(valid)
			if(valid==1):#check
				matetest+=1
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
			if(valid==0):#nochecck
				a[tposi][tposj]=temp
				a[posi][posj]="BK"
				valid=0
				#return 1
				matetest+=0
		
		#print("matetest ",matetest)

		if(matetest>=8):
			#for now the king cant be moved
			'''tposi=0
			tposj=0
			state=1
			print("KING IS SURROUNDED AND CANT BE MOVED")'''
			print("GAMEOVER WHITE WINS")
			exit()
		#else:
		#	matetest+=1
def blockcheck(q,w,e,r):
	tobereturned=0
	a[q][w]="  "
	a[e][r]="WK"

	tobereturned=check()
	#print("HELLO THIS IS BLOCKKFUNC")
	#print("the tobereturned is ",tobereturned)
	#print("move king pos is ",e,r)
	if(tobereturned!=0):#check    this ,ay work for check or try this if(tobereturned==1):
		return 1
	else:#nocheck
		return 0

def blockcheckb(q,w,e,r):
	tobereturned=0
	a[q][w]="  "
	a[e][r]="BK"
	tobereturned=check()
	if(tobereturned!=0):#check    this ,ay work for check or try this if(tobereturned==1):
		return 1
	else:#nocheck
		return 0

def display():
	for i in range(8):
		for j in range(8):
			print("  ",a[i][j],end=" ")
		print(" ")
		
#BLACK=1
#WHITE=2
#EMPTY=0


i=0
j=0
state=0
turn=0
key=3
display()

while(state!=1):
	if(turn==0):
		key=3
		print("WHITES MOVE :")
		while(key==3):
			key=player1()		
		display()
		turn=1
	if(turn==1):
		key=3
		print("BLACKS MOVE :")
		while(key==3):
			key=player2()
		display()
		turn=0