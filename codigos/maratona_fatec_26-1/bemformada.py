def bemformada():
    n = int(input())
    resultados = []
    
    for _ in range(n):
        expressao = input()
        pilha = []
        bem_formada = True
        
        for char in expressao:
            if char in '([{':
                pilha.append(char)
            elif char in ')]}':
                if not pilha:
                    bem_formada = False
                    break
                topo = pilha.pop()
                if (char == ')' and topo != '(') or (char == ']' and topo != '[') or (char == '}' and topo != '{'):
                    bem_formada = False
                    break

        if pilha:
            bem_formada = False

        resultados.append('S' if bem_formada else 'N')

    return resultados

print(*bemformada(), sep='\n')