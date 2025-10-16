#EXEMPLO LISTAS

#frutas = ['maças','banana','laranja']
#frutas.append('uva')
#print(frutas)
#print(frutas[1])
#print(len(frutas))
#frutas.append(22)
#print(frutas)altura


#a = [1,2,3,4]
#print (a[0])
# (a[-1])
#print (a[1:3])
#a[0] = 42
#print(a)


A = [1,2,3]
b = A
print(b) 
b[0]= 42
print(A) 
c = A[:]
print(c) 
c[0] = 0
print(c) 
print(A) 


#programadores = ['Victor','Juliana','Samuel','Caio','Luana']
#print(type(programadores)) #type 'list'
#print(len(programadores)) #5
#programadores.pop(5) #erro


aluno = ['Carlos',50,1.70]
cabecalho = ['Nome',' Idade',' altura']

print(f"{cabecalho[0]}: {aluno[0]},{cabecalho[1]}: {aluno[1]},{cabecalho[2]}: {aluno[2]}m")


diasDaSemana = {1:"domingo", 2:"segunda", 3:"terça", 4:"quarta", 5:"quinta", 6:"sexta"}
print(diasDaSemana)
diasDaSemana[7] = "sabado"
print(diasDaSemana[3])
print(list(diasDaSemana.keys()))

for key in diasDaSemana.keys():
    print(key)