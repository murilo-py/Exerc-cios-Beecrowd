vetor = []
vetor.append(float(input()))

for c in range(0,100):
    vetor.append(vetor[c]/2)
    print(f'N[{c}] = {vetor[c]:.4f}')


