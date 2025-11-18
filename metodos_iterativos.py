"""
Módulo: Métodos Iterativos para Sistemas Lineares
Implementa os métodos de Jacobi e Gauss-Seidel para resolver sistemas Ax = b
"""

def gauss_seidel(A, b, x0=None, tol=0.0001, max_iter=1000):
    """
    Resolve sistema linear Ax = b usando o método de Gauss-Seidel.
    
    Parâmetros:
        A: matriz de coeficientes (lista de listas)
        b: vetor de termos independentes (lista)
        x0: estimativa inicial (lista) - se None, usa vetor zero
        tol: tolerância para convergência
        max_iter: número máximo de iterações
    
    Retorna:
        x: vetor solução (lista)
        num_iter: número de iterações realizadas
        historico: lista de iterações com valores de x
    """
    n = len(b)
    
    # Inicializar x0 se não fornecido
    if x0 is None:
        x = [0.0] * n
    else:
        x = x0[:]
    
    historico = []
    historico.append("=== MÉTODO DE GAUSS-SEIDEL ===")
    historico.append(f"Tolerância: {tol}")
    historico.append(f"Estimativa inicial: {[f'{val:.6f}' for val in x]}")
    historico.append("")
    
    # Adicionar sistema original
    historico.append("Sistema Linear Original:")
    for i in range(n):
        eq = f"Eq {i+1}: "
        for j in range(n):
            if j > 0 and A[i][j] >= 0:
                eq += " + "
            elif A[i][j] < 0:
                eq += " - "
            if j == 0 and A[i][j] < 0:
                eq += "-"
            
            if abs(A[i][j]) != 1 or j == n-1:
                eq += f"{abs(A[i][j]):.1f}"
            
            eq += f"*x{j+1}"
        eq += f" = {b[i]:.1f}"
        historico.append(eq)
    historico.append("")
    
    for k in range(max_iter):
        x_old = x[:]
        
        historico.append(f"--- Iteração {k+1} ---")
        
        for i in range(n):
            soma = 0.0
            
            # Usar valores já atualizados (à esquerda do pivô)
            for j in range(i):
                soma += A[i][j] * x[j]
            
            # Usar valores da iteração anterior (à direita do pivô)
            for j in range(i + 1, n):
                soma += A[i][j] * x_old[j]
            
            x[i] = (b[i] - soma) / A[i][i]
            historico.append(f"  x[{i+1}] = {x[i]:.8f}")
        
        # Calcular erro relativo máximo
        erro = 0.0
        for i in range(n):
            if x[i] != 0:
                erro_rel = abs((x[i] - x_old[i]) / x[i])
                if erro_rel > erro:
                    erro = erro_rel
        
        historico.append(f"  Erro relativo máximo: {erro:.8f}")
        
        # Verificar convergência
        if erro < tol:
            historico.append("")
            historico.append("=== CONVERGÊNCIA ATINGIDA ===")
            historico.append(f"Número de iterações: {k+1}")
            historico.append("")
            historico.append("Solução final:")
            for i in range(n):
                historico.append(f"  x[{i+1}] = {x[i]:.8f}")
            
            return x, k + 1, historico
    
    historico.append("")
    historico.append(f"AVISO: Número máximo de iterações ({max_iter}) atingido!")
    return x, max_iter, historico


def jacobi(A, b, x0=None, tol=0.0001, max_iter=1000):
    """
    Resolve sistema linear Ax = b usando o método de Jacobi.
    
    Parâmetros:
        A: matriz de coeficientes (lista de listas)
        b: vetor de termos independentes (lista)
        x0: estimativa inicial (lista) - se None, usa vetor zero
        tol: tolerância para convergência
        max_iter: número máximo de iterações
    
    Retorna:
        x: vetor solução (lista)
        num_iter: número de iterações realizadas
        historico: lista de iterações com valores de x
    """
    n = len(b)
    
    # Inicializar x0 se não fornecido
    if x0 is None:
        x = [0.0] * n
    else:
        x = x0[:]
    
    historico = []
    historico.append("=== MÉTODO DE JACOBI ===")
    historico.append(f"Tolerância: {tol}")
    historico.append(f"Estimativa inicial: {[f'{val:.6f}' for val in x]}\n")
    
    for k in range(max_iter):
        x_old = x[:]
        
        historico.append(f"--- Iteração {k+1} ---")
        
        # Calcular novos valores usando APENAS valores da iteração anterior
        for i in range(n):
            soma = 0.0
            
            # Somatório completo excluindo o elemento diagonal
            for j in range(n):
                if j != i:
                    soma += A[i][j] * x_old[j]
            
            x[i] = (b[i] - soma) / A[i][i]
            historico.append(f"  x[{i+1}] = {x[i]:.8f}")
        
        # Calcular erro relativo máximo
        erro = 0.0
        for i in range(n):
            if x[i] != 0:
                erro_rel = abs((x[i] - x_old[i]) / x[i])
                if erro_rel > erro:
                    erro = erro_rel
        
        historico.append(f"  Erro relativo máximo: {erro:.8f}\n")
        
        # Verificar convergência
        if erro < tol:
            historico.append(f"=== CONVERGÊNCIA ATINGIDA ===")
            historico.append(f"Número de iterações: {k+1}")
            historico.append(f"\nSolução final:")
            for i in range(n):
                historico.append(f"  x[{i+1}] = {x[i]:.8f}")
            
            return x, k + 1, historico
    
    historico.append(f"\nAVISO: Número máximo de iterações ({max_iter}) atingido!")
    return x, max_iter, historico



def formatar_sistema_matricial(A, b):
    """Formata sistema linear no formato matricial para exibição"""
    n = len(b)
    linhas = []
    
    # Matriz A
    linhas.append("Matriz A:")
    for i in range(n):
        linha = "[ "
        for j in range(n):
            linha += f"{A[i][j]:8.2f} "
        linha += "]"
        linhas.append(linha)
    
    # Vetor x
    linhas.append("")
    linhas.append("Vetor x:")
    for i in range(n):
        linhas.append(f"[ x{i+1} ]")
    
    # Vetor b
    linhas.append("")
    linhas.append("Vetor b:")
    for i in range(n):
        linhas.append(f"[ {b[i]:8.2f} ]")
    
    return "\n".join(linhas)


def resolver_ponte_wheatstone(E, R1, R2, R3, R4, R5, tol=0.0001, valores_iniciais=None, metodo='gauss_seidel'):
    """
    Resolve o problema da Ponte de Wheatstone usando as Leis de Kirchhoff.
    
    Circuito:
        - E: tensão da fonte (V)
        - R1, R2, R3, R4, R5: resistências (ohms)
    
    Sistema de equações baseado nas malhas:
    """
    
    # Montagem do sistema baseado nas 3 malhas principais
    A = [
        [R1 + R2 + R5, -R2, -R5],           # Malha 1
        [-R2, R2 + R3 + R4, -R4],           # Malha 2  
        [-R5, -R4, R4 + R5]                 # Malha 3
    ]
    
    b = [E, 0, 0]
    
    # Usar zeros se valores iniciais não forem fornecidos
    if valores_iniciais is None:
        valores_iniciais = [0.0, 0.0, 0.0]
    
    # Escolher método
    if metodo == 'jacobi':
        x, num_iter, historico = jacobi(A, b, x0=valores_iniciais, tol=tol)
        nome_metodo = 'JACOBI'
    else:
        x, num_iter, historico = gauss_seidel(A, b, x0=valores_iniciais, tol=tol)
        nome_metodo = 'GAUSS-SEIDEL'
    
    # Calcular correntes nos ramos
    i1, i2, i3 = x
    corrente_R1 = i1
    corrente_R2 = i1 - i2
    corrente_R3 = i2
    corrente_R4 = i2 - i3
    corrente_R5 = i3
    
    sistema_formatado = f"""Sistema Linear (Leis de Kirchhoff):

Equação da Malha 1: ({R1} + {R2} + {R5})·i1 - {R2}·i2 - {R5}·i3 = {E}
Equação da Malha 2: -{R2}·i1 + ({R2} + {R3} + {R4})·i2 - {R4}·i3 = 0  
Equação da Malha 3: -{R5}·i1 - {R4}·i2 + ({R4} + {R5})·i3 = 0

Forma Matricial:
[ {R1+R2+R5:5.1f}  {-R2:5.1f}  {-R5:5.1f} ] [ i1 ]   [ {E:5.1f} ]
[ {-R2:5.1f}  {R2+R3+R4:5.1f}  {-R4:5.1f} ] [ i2 ] = [ {0:5.1f} ]
[ {-R5:5.1f}  {-R4:5.1f}  {R4+R5:5.1f} ] [ i3 ]   [ {0:5.1f} ]
"""
    
    return {
        'i1': x[0],
        'i2': x[1], 
        'i3': x[2],
        'corrente_R1': corrente_R1,
        'corrente_R2': corrente_R2,
        'corrente_R3': corrente_R3,
        'corrente_R4': corrente_R4,
        'corrente_R5': corrente_R5,
        'num_iteracoes': num_iter,
        'historico': '\n'.join(historico),
        'sistema': sistema_formatado,
        'metodo': nome_metodo,
        'parametros': f"""Parâmetros do Circuito:
Tensão: E = {E} V
Resistências: R1 = {R1} Ω, R2 = {R2} Ω, R3 = {R3} Ω, R4 = {R4} Ω, R5 = {R5} Ω
Tolerância: {tol}
Método: {nome_metodo}
"""
    }