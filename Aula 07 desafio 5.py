#desafio 1
n = int(input('Digite um valor: '))
print ('O número digitado foi {} e tem como sucessor o número {} e como antecessor {}.'.format(n, n+1, n-1))
n1 = int(input('Digite outro valor: '))
print ('O valor que você digitou agora foi {} e seu antecessor é {}, e seu sucessor é {},'.format(n1, n1-1, n1+1), end=' ')
print ('e a soma dos dois valores que foram digitados é de  {}!'.format(n+n1))
