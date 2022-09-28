#!/data/data/com.termux/files/usr/bin/python
import time
import math

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

rega = 2
regb = 3
stack = 4
cond = 13

dnum = -1
dpoi = -2

arch = [ 16,2, dnum,0, dnum,0, dpoi,5, dpoi,0, dpoi,0, dpoi,0, dpoi,0, dpoi,0, dpoi,0, dpoi,0, dpoi,0, dnum,-2 ]
prgp = int(len(arch)/2)
print ( "prgp: "+str(prgp))
prg = [
iseta,-5,
isetb,1,
iadd,rega,
iifge,prgp+3,
igoto,0 ]
varp = len(arch)+len(prg)
vars = [-1,69]
D = arch
D.extend(prg)
D.extend(vars)
D[0] = prgp+1

def change(pos, datax, datay):
	global D
	D[2*pos-2] = datax
	D[2*pos-1] = datay

def next():
	global D
	change(1, D[0]+1, 2)

def read(index, pos):
	global D
	if pos == 'x':
		return D[int(index*2-2)]
	if pos == 'y':
		return D[int(index*2-1)]

def jump(pos):
	global D
	change(1, pos, 2)

def tick():
	global D
	ins = read(D[0], 'x')
	cnt = D[1]
	dat = read(D[0], 'y')

	if D[1] >= 2:
		change(1, D[0], D[1]+1)
	if D[1] == 1:
		jump(D[0]+1)


	if ins == inull:
		next()
	if ins == igoto:
		if cnt >= 2:
			jump(dat)
		else:
			next()
	if ins == iifeq:
		if cnt == 2:
			if read(rega, 'y') == read(regb, 'y'):
				change(cond, dnum, 1)
			else:
				change(cond, dnum, 0)
		if cnt > 2:
			if read(cond, 'y') == 1:
				next()
			else:
				jump(dat)
		if cnt < 2:
			next()
	if ins == iifgt:
		if cnt == 2:
			if read(rega, 'y') > read(regb, 'y'):
				change(cond, dnum, 1)
			else:
				change(cond, dnum, 0)
		if cnt > 2:
			if read(cond, 'y') == 1:
				next()
			else:
				jump(dat)
		if cnt < 2:
			next()
	if ins == iiflt:
		if cnt == 2:
			if read(rega, 'y') < read(regb, 'y'):
				change(cond, dnum, 1)
			else:
				change(cond, dnum, 0)
		if cnt > 2:
			if read(cond, 'y') == 1:
				next()
			else:
				jump(dat)
		if cnt < 2:
			next()
	if ins == iifge:
		if cnt == 2:
			if read(rega, 'y') >= read(regb, 'y'):
				change(cond, dnum, 1)
			else:
				change(cond, dnum, 0)
		if cnt > 2:
			if read(cond, 'y') == 1:
				next()
			else:
				jump(dat)
		if cnt < 2:
			next()
	if ins == iifle:
		if cnt == 2:
			if read(rega, 'y') <= read(regb, 'y'):
				change(cond, dnum, 1)
			else:
				change(cond, dnum, 0)
		if cnt > 2:
			if read(cond, 'y') == 1:
				next()
			else:
				jump(dat)
		if cnt < 2:
			next()

	if ins == icall:
		if cnt == 2:
			change(stack, dpoi, read(stack,'y')+1)
		if cnt == 3:
			change(read(stack,'y'), dpoi, D[0]+1)
		if cnt == 4:
			change(1, dat, 2)
		if cnt > 4 or cnt < 2:
			next()

	if ins == iretn:
		if cnt == 2:
			change(stack, dpoi, read(stack, 'y')-1)
		if cnt == 3:
			jump(read(read(stack,'y'),'y'))
		if cnt > 3 or cnt < 2:
			next()

	if ins == iseta:
		if cnt == 2:
			change(rega, dnum, dat)
		else:
			next()

	if ins == imema:
		if cnt == 2:
			change(rega, dnum, read(dat, 'y'))
		else:
			next()
	if ins == iamem:
		if cnt == 2:
			change(dat, dnum, read(rega, 'y'))
		else:
			next()

	if ins == isetb:
		if cnt == 2:
			change(regb, dnum, dat)
		else:
			next()

	if ins == imemb:
		if cnt == 2:
			change(regb, dnum, read(dat, 'y'))
		else:
			next()

	if ins == ibmem:
		if cnt == 2:
			change(dat, dnum, read(regb, 'y'))
		else:
			next()

	if ins == iadd:
		if cnt == 2:
			change(dat, dnum, read(rega, 'y') + read(regb, 'y'))
		else:
			next()

	if ins == isub:
		if cnt == 2:
			change(dat, dnum, read(rega, 'y') - read(regb, 'y'))
		else:
			next()

	if ins == imul:
		if cnt == 2:
			change(dat, dnum, read(rega, 'y') * read(regb, 'y'))
		else:
			next()

	if ins == idiv:
		if cnt == 2:
			change(dat, dnum, read(rega, 'y') / read(regb, 'y'))
		else:
			next()

	if ins == ipow:
		if cnt == 2:
			change(dat, dnum, pow(read(rega, 'y'), read(regb, 'y')))
		else:
			next()

	if ins == imod:
		if cnt == 2:
			change(dat, dnum, divmod(read(rega, 'y'), read(regb, 'y')))
		else:
			next()

	if ins == iabs:
		if cnt == 2:
			change(dat, dnum, abs(read(rega, 'y')))
		else:
			next()

	if ins == isin:
		if cnt == 2:
			change(dat, dnum, math.sin(read(rega, 'y')))
		else:
			next()

	if ins == icos:
		if cnt == 2:
			change(dat, dnum, math.cos(read(rega, 'y')))
		else:
			next()

	if ins == itan:
		if cnt == 2:
			change(dat, dnum, math.tan(read(rega, 'y')))
		else:
			next()

	if ins == iasin:
		if cnt == 2:
			change(dat, dnum, math.asin(read(rega, 'y')))
		else:
			next()

	if ins == iacos:
		if cnt == 2:
			change(dat, dnum, math.acos(read(rega, 'y')))
		else:
			next()

	if ins == iatan:
		if cnt == 2:
			change(dat, dnum, math.atan(read(rega, 'y')))
		else:
			next()

	if D[0] <= 0 or D[1] < 1:
		return -1
	return 0



b = 0
while (b >= 0):
	b = tick()
	print (str(D[0]-prgp)+", "+str(D[1])+", rega: "+str(read(rega,'y'))+", cond: "+str(read(cond,'y'))+"       ", end='\r')
	time.sleep(1/5)
print ()
