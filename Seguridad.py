
def func1():
	f = open("poema20.txt",encoding="utf8")
	g = open("poema20_pre.txt","w")

	for linea in f:
		for x in linea:
			if(x=="j"):
				x="i"
			if(x=="h"):
				x="i"
			if(x=="ñ"):
				x="n"
			if(x=="k"):
				x="l"
			if(x=="u"):
				x="v"
			if(x=="w"):
				x="v"
			if(x=="y"):
				x="z"
			g.write(x)

	g.close()
	f.close()
def func2():
	f = open("poema20.txt",encoding="utf8")
	g = open("poema20_pre.txt","w")

	for linea in f:
		for x in linea:
			if(x=="á"):
				x="a"
			if(x=="é"):
				x="e"
			if(x=="í"):
				x="i"
			if(x=="ó"):
				x="o"
			if(x=="ú"):
				x="u"
			g.write(x)

	g.close()
	f.close()
def func2():
	f = open("poema20.txt",encoding="utf8")
	g = open("poema20_pre.txt","w")

	for linea in f:
		for x in linea:
			if(x=="á"):
				x="a"
			if(x=="é"):
				x="e"
			if(x=="í"):
				x="i"
			if(x=="ó"):
				x="o"
			if(x=="ú"):
				x="u"
			g.write(x)

	g.close()
	f.close()
def func3():
	f = open("poema20.txt",encoding="utf8")
	g = open("poema20_pre.txt","w")
	for linea in f:
		for x in linea:
			z = ord(x)
			if(z>=97 and z<=122):
				z-=32
			x = str(chr(z))
			g.write(x)


	g.close()
	f.close()
def func4():
	f = open("poema20.txt",encoding="utf8")
	g = open("poema20_pre.txt","w")
	for linea in f:
		for x in linea:
			if(x==" " or x=="." or x=="," or x=="“" or x==":"):
				x=""
			g.write(x)

	g.close()
	f.close()

def todo(archivo):
	f = open(archivo+".txt",encoding="utf8")
	g = open("poema20_pre.txt","w")
	for linea in f:
		for x in linea:
			if(x=="j"):
				x="i"
			if(x=="h"):
				x="i"
			if(x=="ñ"):
				x="n"
			if(x=="k"):
				x="l"
			if(x=="u"):
				x="v"
			if(x=="w"):
				x="v"
			if(x=="y"):
				x="z"
			if(x=="á"):
				x="a"
			if(x=="é"):
				x="e"
			if(x=="í"):
				x="i"
			if(x=="ó"):
				x="o"
			if(x=="ú"):
				x="u"
			z = ord(x)
			if(z>=97 and z<=122):
				z-=32
				x = str(chr(z))
			if(x=="\n" or x==" " or x=="." or x=="," or x=="”" or x=="“" or x==":"):
				x=""
			g.write(x)
	g.close()
	f.close()


def frecuencias(archivo):
	f = open(archivo+".txt",encoding="utf8")
	c=[]
	for i in range(26):
	    c.append([])
	    for j in range(2):
	        c[i].append(None)

	for i in range(26):
		c[i][0]=str(chr(i+65))
		c[i][1]=0

	for linea in f:
		for x in linea:
			z=ord(x)
			if(z!=10):
				z=z-65
				c[z][1]=c[z][1]+1
	c.sort(key=lambda frecuencia: frecuencia[1],reverse=True)
	for i in range(26):
		print(c[i])
	print("Las letras mas frecuentes son: ")
	for i in range(5):
		print(c[i])
	f.close()


def Kasiski(archivo):
	f = open(archivo+".txt",encoding="utf8")
	c=[]
	cont=0
	ini=0
	fin=0
	dist=0
	for linea in f:
		for i in range(0,len(linea),3):
			tri=linea[i:3+i]
			ini=i+3
			for j in range(i,len(linea),3):
				auxtri=linea[j:3+j]
				
				if(tri==auxtri):

					dist=(j-ini)
					if(dist==-3):
						dist=0
					c.append([])
					for k in range(2):
						c[cont].append(None)
					c[cont][0]=tri
					c[cont][1]=dist
					ini=j+3
					cont=cont+1
					dist=0
	f.close()
	for i in range(len(c)):
		if(c[i][1]!=0):
			print(c[i])



def aqui(archivo):
	f = open(archivo+".txt",encoding="utf8")
	g = open("poema20_pre2.txt","w")
	cont=0
	contotal=0
	for linea in f:
		for j in linea:
			cont=cont+1
			contotal=contotal+1
			if(cont==21):
				cont=1
				contotal=contotal+4
				g.write("AQUI")
				g.write(j)
			else:
				g.write(j)
	contotal=contotal%4
	if(contotal!=0):
		g.write("X"*contotal)
	g.close()
	f.close()


def main():
	#todo("poema20")
	#frecuencias("poema20_pre")
	#Kasiski("poema20_pre")
	aqui("poema20_pre")

main()	
	
	




