"""
Módulo: Lei de Moore
Implementa análise e previsão baseada na Lei de Moore usando regressão logarítmica
"""

def resolver_lei_moore(anos, num_transistores, anos_previsao):
    """
    Resolve o problema da Lei de Moore (Questão 1).
    
    Parâmetros:
        anos: lista de anos
        num_transistores: lista com número de transistores
        anos_previsao: lista de anos para fazer previsão
    
    Retorna:
        dicionário com resultados da regressão e previsões
    """
    n = len(anos)
    detalhes = []
    
    detalhes.append("=== LEI DE MOORE - REGRESSÃO LOGARÍTMICA ===\n")
    detalhes.append(f"Número de pontos de dados: {n}\n")
    
    # Converter para log10
    detalhes.append("Dados originais:")
    for i in range(n):
        detalhes.append(f"  Ano: {anos[i]}, Transistores: {num_transistores[i]}")
    detalhes.append("")
    
    log_N = [logaritmo_base10(N) for N in num_transistores]
    
    detalhes.append("Dados transformados (log₁₀):")
    for i in range(n):
        detalhes.append(f"  Ano: {anos[i]}, log₁₀(N): {log_N[i]:.6f}")
    detalhes.append("")
    
    # Fazer regressão linear: log10(N) = a + b*ano
    from minimos_quadrados import regressao_linear
    
    a, b, erro, det_regressao = regressao_linear(anos, log_N)
    
    detalhes.append("Regressão linear: log₁₀(N) = a + b*ano")
    detalhes.append(f"  a = {a:.6f}")
    detalhes.append(f"  b = {b:.6f}")
    detalhes.append(f"  Erro quadrático: {erro:.6f}\n")
    
    # Fazer previsões
    detalhes.append("=== PREVISÕES ===\n")
    previsoes = []
    
    for ano in anos_previsao:
        log_N_prev = a + b * ano
        N_prev = potencia_base10(log_N_prev)
        
        previsoes.append({
            'ano': ano,
            'log_N': log_N_prev,
            'N': N_prev
        })
        
        detalhes.append(f"Ano {ano}:")
        detalhes.append(f"  log₁₀(N) = {a:.6f} + {b:.6f}*{ano} = {log_N_prev:.6f}")
        detalhes.append(f"  N = 10^{log_N_prev:.6f} = {N_prev:.2e} transistores")
        detalhes.append(f"  N ≈ {N_prev:,.0f} transistores\n")
    
    return {
        'coef_a': a,
        'coef_b': b,
        'erro': erro,
        'equacao_log': f'log₁₀(N) = {a:.6f} + {b:.6f}*ano',
        'previsoes': previsoes,
        'detalhes': '\n'.join(detalhes)
    }


def logaritmo_base10(x):
    """
    Calcula log₁₀(x) = ln(x) / ln(10)
    """
    from minimos_quadrados import logaritmo_natural
    
    if x <= 0:
        return float('nan')
    
    return logaritmo_natural(x) / logaritmo_natural(10)


def potencia_base10(x):
    """
    Calcula 10^x = e^(x*ln(10))
    """
    from minimos_quadrados import logaritmo_natural, exp_manual
    
    return exp_manual(x * logaritmo_natural(10))
