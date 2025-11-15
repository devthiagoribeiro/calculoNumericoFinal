"""
Módulo: Interpolação e Mínimos Quadrados
Implementa regressões por mínimos quadrados (linear, parabólica, exponencial)
"""

def regressao_linear(x, y):
    """
    Ajusta uma reta y = a + bx aos pontos (x, y) usando mínimos quadrados.
    
    Parâmetros:
        x: lista de valores x
        y: lista de valores y
    
    Retorna:
        a, b: coeficientes da reta
        erro_quadratico: soma dos quadrados dos resíduos
        detalhes: string com cálculos detalhados
    """
    n = len(x)
    detalhes = []
    
    detalhes.append("=== REGRESSÃO LINEAR: y = a + bx ===\n")
    detalhes.append(f"Número de pontos: {n}\n")
    
    # Calcular somas necessárias
    soma_x = sum(x)
    soma_y = sum(y)
    soma_x2 = sum(xi**2 for xi in x)
    soma_xy = sum(x[i] * y[i] for i in range(n))
    
    detalhes.append("Somatórios calculados:")
    detalhes.append(f"  Σx = {soma_x:.4f}")
    detalhes.append(f"  Σy = {soma_y:.4f}")
    detalhes.append(f"  Σx² = {soma_x2:.4f}")
    detalhes.append(f"  Σxy = {soma_xy:.4f}\n")
    
    # Sistema normal para regressão linear:
    # n*a + (Σx)*b = Σy
    # (Σx)*a + (Σx²)*b = Σxy
    
    # Resolver usando determinantes (Regra de Cramer)
    det = n * soma_x2 - soma_x * soma_x
    det_a = soma_y * soma_x2 - soma_x * soma_xy
    det_b = n * soma_xy - soma_x * soma_y
    
    a = det_a / det
    b = det_b / det
    
    detalhes.append("Coeficientes calculados:")
    detalhes.append(f"  a = {a:.6f}")
    detalhes.append(f"  b = {b:.6f}\n")
    detalhes.append(f"Equação: y = {a:.6f} + {b:.6f}x\n")
    
    # Calcular erro quadrático
    erro_quad = sum((y[i] - (a + b*x[i]))**2 for i in range(n))
    detalhes.append(f"Erro quadrático total: {erro_quad:.6f}")
    
    return a, b, erro_quad, '\n'.join(detalhes)


def regressao_parabolica(x, y):
    """
    Ajusta uma parábola y = a + bx + cx² aos pontos (x, y) usando mínimos quadrados.
    
    Parâmetros:
        x: lista de valores x
        y: lista de valores y
    
    Retorna:
        a, b, c: coeficientes da parábola
        erro_quadratico: soma dos quadrados dos resíduos
        detalhes: string com cálculos detalhados
    """
    n = len(x)
    detalhes = []
    
    detalhes.append("=== REGRESSÃO PARABÓLICA: y = a + bx + cx² ===\n")
    detalhes.append(f"Número de pontos: {n}\n")
    
    # Calcular somas necessárias
    soma_x = sum(x)
    soma_y = sum(y)
    soma_x2 = sum(xi**2 for xi in x)
    soma_x3 = sum(xi**3 for xi in x)
    soma_x4 = sum(xi**4 for xi in x)
    soma_xy = sum(x[i] * y[i] for i in range(n))
    soma_x2y = sum(x[i]**2 * y[i] for i in range(n))
    
    detalhes.append("Somatórios calculados:")
    detalhes.append(f"  Σx = {soma_x:.4f}")
    detalhes.append(f"  Σy = {soma_y:.4f}")
    detalhes.append(f"  Σx² = {soma_x2:.4f}")
    detalhes.append(f"  Σx³ = {soma_x3:.4f}")
    detalhes.append(f"  Σx⁴ = {soma_x4:.4f}")
    detalhes.append(f"  Σxy = {soma_xy:.4f}")
    detalhes.append(f"  Σx²y = {soma_x2y:.4f}\n")
    
    # Sistema normal 3x3:
    # n*a + (Σx)*b + (Σx²)*c = Σy
    # (Σx)*a + (Σx²)*b + (Σx³)*c = Σxy
    # (Σx²)*a + (Σx³)*b + (Σx⁴)*c = Σx²y
    
    A = [
        [n, soma_x, soma_x2],
        [soma_x, soma_x2, soma_x3],
        [soma_x2, soma_x3, soma_x4]
    ]
    
    b_vec = [soma_y, soma_xy, soma_x2y]
    
    # Resolver usando eliminação de Gauss (importar do módulo de métodos diretos)
    from metodos_diretos import gauss_elimination
    
    solucao, _ = gauss_elimination(A, b_vec)
    a, b, c = solucao
    
    detalhes.append("Coeficientes calculados:")
    detalhes.append(f"  a = {a:.6f}")
    detalhes.append(f"  b = {b:.6f}")
    detalhes.append(f"  c = {c:.6f}\n")
    detalhes.append(f"Equação: y = {a:.6f} + {b:.6f}x + {c:.6f}x²\n")
    
    # Calcular erro quadrático
    erro_quad = sum((y[i] - (a + b*x[i] + c*x[i]**2))**2 for i in range(n))
    detalhes.append(f"Erro quadrático total: {erro_quad:.6f}")
    
    return a, b, c, erro_quad, '\n'.join(detalhes)


def regressao_exponencial(x, y):
    """
    Ajusta uma exponencial y = a*e^(bx) aos pontos (x, y) usando mínimos quadrados.
    Lineariza para ln(y) = ln(a) + bx e depois ajusta linearmente.
    
    Parâmetros:
        x: lista de valores x
        y: lista de valores y (devem ser positivos)
    
    Retorna:
        a, b: coeficientes da exponencial
        erro_quadratico: soma dos quadrados dos resíduos (na escala original)
        detalhes: string com cálculos detalhados
    """
    n = len(x)
    detalhes = []
    
    detalhes.append("=== REGRESSÃO EXPONENCIAL: y = a*e^(bx) ===\n")
    detalhes.append(f"Número de pontos: {n}\n")
    
    # Linearização: ln(y) = ln(a) + bx
    # Fazendo z = ln(y), temos: z = ln(a) + bx
    
    detalhes.append("Linearização: ln(y) = ln(a) + bx\n")
    
    # Calcular logaritmos
    ln_y = []
    for i in range(n):
        if y[i] <= 0:
            detalhes.append(f"ERRO: y[{i}] = {y[i]} não é positivo!")
            return None, None, None, '\n'.join(detalhes)
        ln_y.append(logaritmo_natural(y[i]))
    
    detalhes.append("Valores transformados (ln(y)):")
    for i in range(n):
        detalhes.append(f"  x={x[i]:.4f}, ln(y)={ln_y[i]:.6f}")
    detalhes.append("")
    
    # Aplicar regressão linear em (x, ln_y)
    soma_x = sum(x)
    soma_lny = sum(ln_y)
    soma_x2 = sum(xi**2 for xi in x)
    soma_x_lny = sum(x[i] * ln_y[i] for i in range(n))
    
    detalhes.append("Somatórios calculados:")
    detalhes.append(f"  Σx = {soma_x:.4f}")
    detalhes.append(f"  Σln(y) = {soma_lny:.4f}")
    detalhes.append(f"  Σx² = {soma_x2:.4f}")
    detalhes.append(f"  Σx·ln(y) = {soma_x_lny:.4f}\n")
    
    det = n * soma_x2 - soma_x * soma_x
    det_lna = soma_lny * soma_x2 - soma_x * soma_x_lny
    det_b = n * soma_x_lny - soma_x * soma_lny
    
    ln_a = det_lna / det
    b = det_b / det
    
    # Calcular a = e^(ln_a)
    a = exp_manual(ln_a)
    
    detalhes.append("Coeficientes calculados:")
    detalhes.append(f"  ln(a) = {ln_a:.6f}")
    detalhes.append(f"  a = e^({ln_a:.6f}) = {a:.6f}")
    detalhes.append(f"  b = {b:.6f}\n")
    detalhes.append(f"Equação: y = {a:.6f}*e^({b:.6f}x)\n")
    
    # Calcular erro quadrático na escala original
    erro_quad = sum((y[i] - a * exp_manual(b * x[i]))**2 for i in range(n))
    detalhes.append(f"Erro quadrático total: {erro_quad:.6f}")
    
    return a, b, erro_quad, '\n'.join(detalhes)


def logaritmo_natural(x, termos=50):
    """
    Calcula ln(x) usando série de Taylor: ln(x) = 2*Σ(1/(2k+1) * ((x-1)/(x+1))^(2k+1))
    Válido para x > 0
    """
    if x <= 0:
        return float('nan')
    
    # Para convergência mais rápida, usar ln(x) = ln(x/e^k) + k onde escolhemos k apropriado
    # Ou usar a série ln((1+z)/(1-z)) = 2(z + z³/3 + z⁵/5 + ...)
    # onde z = (x-1)/(x+1)
    
    z = (x - 1) / (x + 1)
    soma = 0.0
    z_potencia = z
    
    for k in range(termos):
        soma += z_potencia / (2*k + 1)
        z_potencia *= z * z
    
    return 2 * soma


def exp_manual(x, termos=50):
    """
    Calcula e^x usando série de Taylor: e^x = Σ(x^k / k!)
    """
    soma = 1.0
    termo = 1.0
    
    for k in range(1, termos):
        termo *= x / k
        soma += termo
        
        # Parar se termo muito pequeno
        if abs(termo) < 1e-15:
            break
    
    return soma


def resolver_regressoes(x_dados, y_dados):
    """
    Aplica as três regressões (linear, parabólica, exponencial) aos dados fornecidos.
    """
    # Regressão linear
    a_lin, b_lin, erro_lin, det_lin = regressao_linear(x_dados, y_dados)
    
    # Regressão parabólica
    a_par, b_par, c_par, erro_par, det_par = regressao_parabolica(x_dados, y_dados)
    
    # Regressão exponencial
    a_exp, b_exp, erro_exp, det_exp = regressao_exponencial(x_dados, y_dados)
    
    return {
        'linear': {
            'a': a_lin,
            'b': b_lin,
            'erro': erro_lin,
            'equacao': f'y = {a_lin:.6f} + {b_lin:.6f}x',
            'detalhes': det_lin
        },
        'parabolica': {
            'a': a_par,
            'b': b_par,
            'c': c_par,
            'erro': erro_par,
            'equacao': f'y = {a_par:.6f} + {b_par:.6f}x + {c_par:.6f}x²',
            'detalhes': det_par
        },
        'exponencial': {
            'a': a_exp,
            'b': b_exp,
            'erro': erro_exp,
            'equacao': f'y = {a_exp:.6f}*e^({b_exp:.6f}x)',
            'detalhes': det_exp
        } if a_exp is not None else None
    }
