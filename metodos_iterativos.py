"""
Módulo: Métodos Iterativos para Sistemas Lineares
Implementa o método de Gauss-Seidel para resolver sistemas Ax = b
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
    historico.append(f"=== MÉTODO DE GAUSS-SEIDEL ===")
    historico.append(f"Tolerância: {tol}")
    historico.append(f"Estimativa inicial: {[f'{val:.6f}' for val in x]}\n")
    
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


def resolver_ponte_wheatstone(E, R1, R2, R3, R4, R5, tol=0.0001, valores_iniciais=None):
    """
    Resolve o problema da Ponte de Wheatstone usando as Leis de Kirchhoff.
    
    Circuito:
        - E: tensão da fonte (V)
        - R1, R2, R3, R4, R5: resistências (ohms)
    
    Sistema de equações das correntes (i1, i2, i3):
    Usando as Leis de Kirchhoff:
        Malha 1: i1*R1 + i2*R5 = E
        Malha 2: i2*R2 + (i2-i3)*R5 = 0  =>  i2*(R2+R5) - i3*R5 = 0
        Malha 3: i3*R3 + i3*R4 + (i3-i2)*R5 = 0  =>  -i2*R5 + i3*(R3+R4+R5) = 0
    
    Ajustando para o formato padrão:
        Nó superior: i1 = i2 + i3
        Malha esquerda: E = i1*R1 + i2*R2
        Malha direita: i2*R2 + (i2-i3)*R5 = i3*R3 + i3*R4
    
    Sistema matricial (usando 3 correntes principais):
        i1, i2, i3
    """
    
    # Montagem do sistema baseado nas malhas
    # Malha 1 (externa esquerda): E = i1*R1 + i2*R2
    # Malha 2 (central): 0 = i2*(R2+R5) - i3*R5 - i1*R2  =>  -i1*R2 + i2*(R2+R5) - i3*R5 = 0
    # Malha 3 (externa direita): 0 = i3*(R3+R4+R5) - i2*R5
    # Lei dos nós: i1 = i2 + i3  =>  i1 - i2 - i3 = 0
    
    # Sistema reformulado para 3 correntes:
    # Equação 1 (nó): i1 - i2 - i3 = 0
    # Equação 2 (malha esquerda): i1*R1 + i2*R2 = E
    # Equação 3 (malha direita): i2*R5 - i3*(R4+R5) = 0
    
    A = [
        [1, -1, -1],                    # Lei dos nós
        [R1, R2, 0],                    # Malha esquerda
        [0, R5, -(R4 + R5)]            # Malha direita com R3
    ]
    
    b = [0, E, 0]
    
    # Reordenar para melhor convergência (diagonal dominante se possível)
    A_reord = [
        [R1, R2, 0],                    # Malha esquerda
        [0, R2 + R5, -R5],              # Malha central
        [0, -R5, R3 + R4 + R5]          # Malha direita
    ]
    
    b_reord = [E, 0, 0]
    
    x, num_iter, historico = gauss_seidel(A_reord, b_reord, x0=valores_iniciais, tol=tol)
    
    return {
        'i1': x[0],
        'i2': x[1],
        'i3': x[2],
        'num_iteracoes': num_iter,
        'historico': '\n'.join(historico),
        'sistema': f"""Sistema Linear (Leis de Kirchhoff):
Equação 1 (Malha esquerda):  {R1}*i1 + {R2}*i2 = {E}
Equação 2 (Malha central):   {R2 + R5}*i2 - {R5}*i3 = 0
Equação 3 (Malha direita):   -{R5}*i2 + {R3 + R4 + R5}*i3 = 0
"""
    }
