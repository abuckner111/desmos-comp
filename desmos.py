#!/data/data/com.termux/files/usr/bin/python
import time
inull = 1
igoto = 2
iifeq = 3
iifgt = 4
iiflt = 5
iifle = 6
iifge = 7
icall = 8
iretn = 9
iseta = 10
imema = 11
iamem = 12
isetb = 13
imemb = 14
ibmem = 15
iadd  = 16
isub  = 17
imul  = 18
idiv  = 19
ipow  = 20
imod  = 21
iabs  = 22
isin  = 23
icos  = 24
itan  = 25
iasin = 26
iacos = 27
iatan = 28

dnum = -1
dpoi = -2
ast = 0
arch = [ 16,2, dnum,0, dnum,0, dpoi,5, dpoi,0, dpoi,0, dpoi,0, dpoi,0, dpoi,0, dpoi,0, dpoi,0, dpoi,0, dpoi,0, dnum,0 ]
prgp = len(arch)/2+1
print ( "prgp: "+str(prgp))
prg = [igoto,prgp+1, igoto, prgp]
varp = len(arch)+len(prg)
vars = [-1,69]
D = arch
D.extend(prg)
D.extend(vars)
D[0] = prgp

def change(pos, datax, datay):
	D[2*pos-2] = datax
	D[2*pos-1] = datay

def next():
	change(1, D[0]+1, 2)
def read(index, pos):
	if pos == 'x':
		return D[int(index*2-2)]
	if pos == 'y':
		return D[int(index*2-1)]


def tick():
	global ast
	if ast == 0:
		ins = read(D[0], 'x')
		ast = 1
	else:
		ins = inull
		ast = 0
	cnt = D[1]
	dat = read(D[0], 'y')
	if ins == igoto:
		if cnt >= 2:
			change(1,dat,2)
		else:
			next()
	if ins == iifeq:
		if cnt >= 2:
			if D[3] == D[5]:
				change(14, dnum, 1)
			else:
				change(14, dnum, 0)
		else:
			next()
	if ins == iifgt:
		if cnt >= 2:
			if D[3] > D[5]:
				change(14, dnum, 1)
			else:
				change(14, dnum, 0)
		else:
			next()
	if ins == iiflt:
		if cnt >= 2:
			if D[3] < D[5]:
				change(14, dnum, 1)
			else:
				change(14, dnum, 0)
		else:
			next()
	if ins == iifge:
		if cnt >= 2:
			if D[3] >= D[5]:
				change(14, dnum, 1)
			else:
				change(14, dnum, 0)
		else:
			next()
	if ins == iifle:
		if cnt >= 2:
			if D[3] <= D[5]:
				change(14, dnum, 1)
			else:
				change(14, dnum, 0)
		else:
			next()

	if ins == icall:
		if cnt == 2:
			change(4, dpoi, read(4,'y')+1)
		if cnt == 3:
			change(read(4,'y'), dpoi, D[0]+1)
		if cnt == 4:
			change(1, read(D[0],'y'), 2)
	if ast == 0 and D[1] >= 2:
		change(1, D[0], D[1]+1)
	if ast == 0 and D[1] == 1:
		change(1, D[0]+1, D[1])

	if D[1] <= 0:
		return -1
	return 0




while (tick() >= 0):
	print (str(D[0])+", "+str(D[1])+", "+str(ast), end='\r')
	time.sleep(0.5)
print ()
