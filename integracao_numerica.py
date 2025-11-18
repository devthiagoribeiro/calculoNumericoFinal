"""
Módulo: Integração Numérica
Implementa métodos de integração numérica: Trapézio e Simpson 1/3 Repetido
"""

def area_trapezio(x, y):
    """
    Calcula a área sob a curva usando o método do Trapézio.
    
    Parâmetros:
        x: lista de posições (distâncias)
        y: lista de valores da função (profundidades)
    
    Retorna:
        area: valor da área calculada
        detalhes: descrição dos passos
    """
    x = list(x)
    y = list(y)
    n = len(x) - 1
    
    if n < 1:
        raise ValueError("São necessários pelo menos 2 pontos")
    
    detalhes = []
    detalhes.append("=== MÉTODO DO TRAPÉZIO ===\n")
    detalhes.append(f"Número de intervalos (n): {n}")
    
    # Calcular h (espaçamento)
    h_values = []
    for i in range(n):
        h_i = x[i + 1] - x[i]
        h_values.append(h_i)
    
    detalhes.append(f"Espaçamentos (h):")
    for i, h_i in enumerate(h_values):
        detalhes.append(f"  h[{i}] = x[{i+1}] - x[{i}] = {x[i+1]} - {x[i]} = {h_i}")
    
    # Verificar se espaçamento é uniforme
    is_uniform = all(abs(h - h_values[0]) < 1e-10 for h in h_values)
    if is_uniform:
        h = h_values[0]
        detalhes.append(f"\nEspaçamento uniforme: h = {h}")
    else:
        detalhes.append(f"\nEspaçamento não-uniforme detectado")
        h = None
    
    detalhes.append(f"\nPontos de integração:")
    for i in range(len(x)):
        detalhes.append(f"  x[{i}] = {x[i]}, y[{i}] = {y[i]}")
    
    # Fórmula do Trapézio: A = (h/2) * (y0 + 2*y1 + 2*y2 + ... + 2*y(n-1) + yn)
    detalhes.append(f"\nFórmula: A = (h/2) * (y[0] + 2*Σy[i] + y[n])")
    
    soma_interior = sum(y[1:-1])
    area = 0
    
    for i in range(n):
        h_i = x[i + 1] - x[i]
        area_trap = (h_i / 2) * (y[i] + y[i + 1])
        area += area_trap
        detalhes.append(f"  Trapézio {i}: ({h_i}/2) * ({y[i]} + {y[i+1]}) = {area_trap}")
    
    detalhes.append(f"\n{'='*50}")
    detalhes.append(f"ÁREA TOTAL (Trapézio) = {area}")
    detalhes.append(f"{'='*50}")
    
    return {
        'area': area,
        'detalhes': '\n'.join(detalhes),
        'numero_intervalos': n
    }


def area_simpson13_repetido(x, y):
    """
    Calcula a área sob a curva usando o método de Simpson 1/3 Repetido.
    Requer número PAR de intervalos.
    
    Parâmetros:
        x: lista de posições (distâncias)
        y: lista de valores da função (profundidades)
    
    Retorna:
        area: valor da área calculada
        detalhes: descrição dos passos
    """
    x = list(x)
    y = list(y)
    n = len(x) - 1
    
    if n < 2:
        raise ValueError("São necessários pelo menos 3 pontos")
    
    detalhes = []
    detalhes.append("=== MÉTODO DE SIMPSON 1/3 REPETIDO ===\n")
    detalhes.append(f"Número de intervalos (n): {n}")
    
    if n % 2 == 1:
        detalhes.append(f"\n⚠️  AVISO: O número de intervalos ({n}) é ÍMPAR!")
        detalhes.append("Simpson 1/3 Repetido requer número PAR de intervalos.")
        detalhes.append("Este método NÃO será aplicado.")
        
        return {
            'area': None,
            'detalhes': '\n'.join(detalhes),
            'numero_intervalos': n,
            'aplicavel': False
        }
    
    # Calcular h
    h_values = []
    for i in range(n):
        h_i = x[i + 1] - x[i]
        h_values.append(h_i)
    
    detalhes.append(f"Espaçamentos (h):")
    for i, h_i in enumerate(h_values):
        detalhes.append(f"  h[{i}] = x[{i+1}] - x[{i}] = {x[i+1]} - {x[i]} = {h_i}")
    
    # Verificar se espaçamento é uniforme
    is_uniform = all(abs(h - h_values[0]) < 1e-10 for h in h_values)
    if is_uniform:
        h = h_values[0]
        detalhes.append(f"\nEspaçamento uniforme: h = {h}")
    else:
        detalhes.append(f"\nEspaçamento não-uniforme detectado")
        detalhes.append("Usaremos trapézios para cada intervalo individual")
        h = None
    
    detalhes.append(f"\nPontos de integração:")
    for i in range(len(x)):
        detalhes.append(f"  x[{i}] = {x[i]}, y[{i}] = {y[i]}")
    
    detalhes.append(f"\nFórmula Simpson 1/3: A = (h/3) * (y[0] + 4*Σy_ímpar + 2*Σy_par + y[n])")
    
    # Índices ímpares (1, 3, 5, ...) e pares (2, 4, 6, ...)
    odd_indices = list(range(1, n, 2))
    even_indices = list(range(2, n - 1, 2))
    
    detalhes.append(f"\nÍndices dos pontos ímpares: {odd_indices}")
    detalhes.append(f"Índices dos pontos pares: {even_indices}")
    
    odd_sum = sum(y[i] for i in odd_indices)
    even_sum = sum(y[i] for i in even_indices)
    
    detalhes.append(f"\nΣy[índices ímpares] = {' + '.join([f'y[{i}]({y[i]})' for i in odd_indices])} = {odd_sum}")
    detalhes.append(f"Σy[índices pares] = {' + '.join([f'y[{i}]({y[i]})' for i in even_indices])} = {even_sum}")
    
    if h is not None:
        area = (h / 3) * (y[0] + 4 * odd_sum + 2 * even_sum + y[-1])
        detalhes.append(f"\nA = ({h}/3) * ({y[0]} + 4*{odd_sum} + 2*{even_sum} + {y[-1]})")
    
    detalhes.append(f"\n{'='*50}")
    detalhes.append(f"ÁREA TOTAL (Simpson 1/3) = {area}")
    detalhes.append(f"{'='*50}")
    
    return {
        'area': area,
        'detalhes': '\n'.join(detalhes),
        'numero_intervalos': n,
        'aplicavel': True
    }


def area_simpson_com_trapezio(x, y):
    """
    Calcula área usando Simpson 1/3 para os primeiros n-1 intervalos (se n ímpar)
    e trapézio para o último intervalo. Se n é par, usa só Simpson 1/3.
    
    Parâmetros:
        x: lista de posições (distâncias)
        y: lista de valores da função (profundidades)
    
    Retorna:
        area: valor da área calculada
        detalhes: descrição dos passos
    """
    x = list(x)
    y = list(y)
    n = len(x) - 1
    
    if n < 1:
        raise ValueError("São necessários pelo menos 2 pontos")
    
    detalhes = []
    detalhes.append("=== MÉTODO DE SIMPSON 1/3 + TRAPÉZIO (HÍBRIDO) ===\n")
    detalhes.append(f"Número de intervalos (n): {n}")
    
    if n % 2 == 0:
        detalhes.append(f"\nNúmero de intervalos é PAR ({n})")
        detalhes.append("Aplicando Simpson 1/3 Repetido em todo o domínio")
        
        result = area_simpson13_repetido(x, y)
        detalhes.append("\n" + result['detalhes'])
        
        return {
            'area': result['area'],
            'detalhes': '\n'.join(detalhes) + "\n" + result['detalhes'],
            'numero_intervalos': n,
            'modo': 'simpson_completo'
        }
    
    else:
        detalhes.append(f"\nNúmero de intervalos é ÍMPAR ({n})")
        detalhes.append("Aplicando Simpson 1/3 nos primeiros (n-1) intervalos")
        detalhes.append("Aplicando Trapézio no último intervalo")
        
        # Simpson nos primeiros n-1 pontos
        result_simpson = area_simpson13_repetido(x[:-1], y[:-1])
        area_simpson = result_simpson['area']
        
        detalhes.append(f"\n--- Parte 1: Simpson 1/3 (primeiros {n-1} intervalos) ---")
        detalhes.append(result_simpson['detalhes'])
        
        # Trapézio no último intervalo
        h_last = x[-1] - x[-2]
        area_trap_last = (h_last / 2) * (y[-2] + y[-1])
        
        detalhes.append(f"\n--- Parte 2: Trapézio (último intervalo) ---")
        detalhes.append(f"h = {x[-1]} - {x[-2]} = {h_last}")
        detalhes.append(f"A_trapézio = ({h_last}/2) * ({y[-2]} + {y[-1]}) = {area_trap_last}")
        
        area_total = area_simpson + area_trap_last
        
        detalhes.append(f"\n{'='*50}")
        detalhes.append(f"ÁREA PARTE 1 (Simpson) = {area_simpson}")
        detalhes.append(f"ÁREA PARTE 2 (Trapézio) = {area_trap_last}")
        detalhes.append(f"ÁREA TOTAL = {area_simpson} + {area_trap_last} = {area_total}")
        detalhes.append(f"{'='*50}")
        
        return {
            'area': area_total,
            'detalhes': '\n'.join(detalhes),
            'numero_intervalos': n,
            'modo': 'simpson_trapezio'
        }


def resolver_integracao(x, y, metodo='trapezio'):
    """
    Resolve o problema de integração numérica usando o método escolhido.
    
    Parâmetros:
        x: lista de posições (distâncias)
        y: lista de valores da função (profundidades)
        metodo: 'trapezio', 'simpson', ou 'automatico'
    
    Retorna:
        dicionário com resultado e detalhes
    """
    
    x = list(x)
    y = list(y)
    
    if len(x) != len(y):
        return {
            'sucesso': False,
            'erro': 'Os vetores x e y devem ter o mesmo tamanho'
        }
    
    if len(x) < 2:
        return {
            'sucesso': False,
            'erro': 'São necessários pelo menos 2 pontos'
        }
    
    resultados = {}
    
    try:
        # Sempre calcular trapézio (sempre aplicável)
        resultado_trap = area_trapezio(x, y)
        resultados['trapezio'] = resultado_trap
    except Exception as e:
        resultados['trapezio'] = {
            'area': None,
            'detalhes': f"Erro ao calcular trapézio: {str(e)}",
            'erro': True
        }
    
    try:
        # Calcular Simpson com híbrido (aplicável sempre)
        resultado_simpson = area_simpson_com_trapezio(x, y)
        resultados['simpson'] = resultado_simpson
    except Exception as e:
        resultados['simpson'] = {
            'area': None,
            'detalhes': f"Erro ao calcular Simpson: {str(e)}",
            'erro': True
        }
    
    return {
        'sucesso': True,
        'resultados': resultados,
        'numero_pontos': len(x),
        'sistema_original': f"Pontos: x = {x}, y = {y}"
    }
