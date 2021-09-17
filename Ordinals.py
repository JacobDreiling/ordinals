def succ(a):
	return (lambda n:a),a[1]+'+1'

def fin(k):
	if k==0:return 0,'0'
	return succ(fin(k-1))[0],str(k)

def add(a,b):
	if b[0]==0:return a
	if b[0](0)==b[0](1):
		return succ(add(a,b[0](0)))
	return (lambda n:add(a,b[0](n))),'(%s+%s)'%(a[1],b[1])

def mult(a,b):
	if b[0]==0:return fin(0)
	if b[0](0)==b[0](1):
		return add(mult(a,b[0](0)),a)
	return (lambda n:mult(a,b[0](n))),'(%s*%s)'%(a[1],b[1])

def exp(a,b):
	if b[0]==0:return fin(1)
	if b[0](0)==b[0](1):
		return mult(exp(a,b[0](0)),a)
	return (lambda n:exp(a,b[0](n))),'(%s^%s)'%(a[1],b[1])

omega=lambda n:fin(n),'ω'

def hyper(a,b,l):
	if l==0:
		return succ(a)
	if b[0]==0:
		return [a,fin(0),fin(1)][l-1]
	if b[0](0)==b[0](1):
		return hyper(hyper(a,b[0](0),l),a,l-1)
	return (lambda n:hyper(a,b[0](n),l)),'('+a[1]+['+','*','^'][l-1]+b[1]+')'

def epsilon(a):
	s='ε_(%s)'%a[1]
	if a[0]==0 or a[0](0)==a[0](1):
		def tower(n):
			t=hyper(fin(0) if a[0]==0 else epsilon(a[0](0)),fin(1),1)
			for _ in range(n):
				t=hyper(omega,t,3)
			return t
		return tower,s
	return (lambda n:epsilon(a[0](n))),s

def zeta(a):
	s='ζ_(%s)'%a[1]
	if a[0]==0 or a[0](0)==a[0](1):
		def tower(n):
			t=fin(0) if a[0]==0 else add(zeta(a[0](0)),fin(1))
			for _ in range(n):
				t=epsilon(t)
			return t
		return tower,s
	return (lambda n:zeta(a[0](n))),s

def phi(a,b):
	s='φ(%s,%s)'%(a[1],b[1])
	if a[0]==0:
		return exp(omega,b)
	if a[0](0)==a[0](1):
		if b[0]==0 or b[0](0)==b[0](1):
			def tower(n):
				t=fin(a[0](0)[0]==0) if b[0]==0 else add(phi(a,b[0](0)),fin(1))
				for _ in range(n):
					t=phi(a[0](0),t)
				return t
			return tower,s
		return (lambda n:phi(a,b[0](n))),s
	if b[0]==0:
		return (lambda n:phi(a[0](n),b)),s
	if b[0](0)==b[0](1):
		def tower(n):
			t=add(phi(a,b[0](0)),fin(1))
			for _ in range(n):
				t=phi(a,t)
			return t
		return tower,s
	return (lambda n:phi(a,b[0](n))),s

Gamma0= (lambda n:fin(1) if n==0 else phi(Gamma0[0](n-1),fin(0))),'Γ_0'

def Phi(ords):
	s='φ(%s)'%(''.join(o[1]+',' for o in ords)[:-1])
	gamma=ords[-1]
	i=len(ords)-2
	while i>=0 and ords[i][0]==0:i-=1
	if i<0:
		return exp(omega,gamma)
	beta=ords[i]
	if beta[0](0)==beta[0](1):
		if gamma[0]==0 or gamma[0](0)==gamma[0](1):
			def tower(n):
				t=fin(0) if gamma[0]==0 else add(Phi(ords[:-1]+[gamma[0](0)]),fin(1))
				for _ in range(n):
					t=Phi(ords[:i]+[beta[0](0),t]+ords[i+2:])
				return t
			return tower,s
		return (lambda n:Phi(ords[:-1]+[gamma[0](n)])),s
	if gamma[0]==0:
		return (lambda n:Phi(ords[:i]+[beta[0](n)]+ords[i+1:])),s
	if gamma[0](0)==gamma[0](1):
		t=add(Phi(ords[:-1]+[gamma[0](0)]),fin(1))
		return (lambda n:Phi(ords[:i]+[beta[0](n),t]+ords[i+2:-1]+[fin(0)])),s
	return (lambda n:Phi(ords[:-1]+[gamma[0](n)])),s

def f(a,n):
	print('calculating f_%s(%d)'%(a[1],n))
	if a[0]==0:
		return n+1
	if a[0](0)==a[0](1):
		t=n
		for _ in range(n):
			t=f(a[0](0),t)
		return t
	return f(a[0](n),n)

def g(a,n):
	print('calculating g_%s(%d)'%(a[1],n))
	if a[0]==0:
		return 0
	if a[0](0)==a[0](1):
		return g(a[0](0),n)+1
	return g(a[0](n),n)

print(g(Phi([omega,fin(0),fin(1)]),2))
