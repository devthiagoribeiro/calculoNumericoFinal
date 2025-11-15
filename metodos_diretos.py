"""
Módulo: Métodos Diretos para Sistemas Lineares
Implementa métodos numéricos para resolver sistemas Ax = b
Métodos: Eliminação de Gauss com pivoteamento parcial
"""

def gauss_elimination(A, b):
    """
    Resolve sistema linear Ax = b usando Eliminação de Gauss com pivoteamento parcial.
    
    Parâmetros:
        A: matriz de coeficientes (lista de listas)
        b: vetor de termos independentes (lista)
    
    Retorna:
        x: vetor solução (lista)
        passos: lista com descrição dos passos executados
    """
    n = len(b)
    passos = []
    
    # Criar cópias para não modificar originais
    A = [linha[:] for linha in A]
    b = b[:]
    
    passos.append("=== ELIMINAÇÃO DE GAUSS COM PIVOTEAMENTO PARCIAL ===\n")
    passos.append("Sistema Original:")
    passos.append(formatar_sistema(A, b))
    
    # Fase de eliminação
    for k in range(n - 1):
        # Pivoteamento parcial
        max_idx = k
        max_val = abs(A[k][k])
        
        for i in range(k + 1, n):
            if abs(A[i][k]) > max_val:
                max_val = abs(A[i][k])
                max_idx = i
        
        if max_idx != k:
            A[k], A[max_idx] = A[max_idx], A[k]
            b[k], b[max_idx] = b[max_idx], b[k]
            passos.append(f"\nTroca linha {k+1} com linha {max_idx+1} (pivoteamento)")
        
        passos.append(f"\n--- Passo {k+1}: Eliminação abaixo do pivô A[{k+1}][{k+1}] = {A[k][k]:.4f} ---")
        
        # Eliminação
        for i in range(k + 1, n):
            if A[k][k] == 0:
                passos.append("ERRO: Pivô zero encontrado!")
                return None, passos
            
            fator = A[i][k] / A[k][k]
            passos.append(f"Fator m[{i+1}][{k+1}] = {fator:.4f}")
            
            for j in range(k, n):
                A[i][j] = A[i][j] - fator * A[k][j]
            
            b[i] = b[i] - fator * b[k]
        
        passos.append("\nSistema após eliminação:")
        passos.append(formatar_sistema(A, b))
    
    # Substituição reversa
    passos.append("\n=== SUBSTITUIÇÃO REVERSA ===")
    x = [0.0] * n
    
    for i in range(n - 1, -1, -1):
        soma = 0.0
        for j in range(i + 1, n):
            soma += A[i][j] * x[j]
        
        x[i] = (b[i] - soma) / A[i][i]
        passos.append(f"x[{i+1}] = {x[i]:.6f}")
    
    passos.append("\n=== SOLUÇÃO FINAL ===")
    for i in range(n):
        passos.append(f"x[{i+1}] = {x[i]:.6f}")
    
    return x, passos


def formatar_sistema(A, b):
    """Formata sistema linear para exibição"""
    n = len(b)
    linhas = []
    
    for i in range(n):
        linha = "[ "
        for j in range(n):
            linha += f"{A[i][j]:8.4f} "
        linha += f"] [ x{i+1} ]   [ {b[i]:8.4f} ]"
        linhas.append(linha)
    
    return "\n".join(linhas)


def resolver_problema_minas(d1, d2, d3, comp_mina1, comp_mina2, comp_mina3):
    """
    Resolve o problema das três minas (Questão 3).
    
    Parâmetros:
        d1, d2, d3: demandas de areia, cascalho fino e cascalho grosso (m³)
        comp_mina1, comp_mina2, comp_mina3: composição de cada mina [areia%, casc_fino%, casc_grosso%]
    
    Retorna:
        solucao: dicionário com x1, x2, x3 e passos
    """
    # Montar sistema: cada linha representa um material
    # x1*comp1[material] + x2*comp2[material] + x3*comp3[material] = demanda[material]
    
    A = [
        [comp_mina1[0]/100, comp_mina2[0]/100, comp_mina3[0]/100],  # areia
        [comp_mina1[1]/100, comp_mina2[1]/100, comp_mina3[1]/100],  # cascalho fino
        [comp_mina1[2]/100, comp_mina2[2]/100, comp_mina3[2]/100]   # cascalho grosso
    ]
    
    b = [d1, d2, d3]
    
    x, passos = gauss_elimination(A, b)
    
    return {
        'x1': x[0] if x else 0,
        'x2': x[1] if x else 0,
        'x3': x[2] if x else 0,
        'passos': '\n'.join(passos),
        'sistema_original': formatar_sistema(A, b)
    }
