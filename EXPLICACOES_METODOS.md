# Explicações dos Métodos Numéricos Implementados

## 1. Eliminação de Gauss com Pivoteamento Parcial

### Descrição
Método direto para resolver sistemas lineares Ax = b através da transformação da matriz em uma forma triangular superior.

### Algoritmo

**Fase 1: Eliminação (Triangularização)**

Para cada coluna k (de 0 a n-2):
1. **Pivoteamento Parcial:**
   - Encontrar o elemento de maior valor absoluto na coluna k, das linhas k até n
   - Trocar a linha k com a linha do pivô máximo
   - Isso aumenta a estabilidade numérica

2. **Eliminação:**
   - Para cada linha i abaixo de k:
     - Calcular fator: m[i,k] = A[i,k] / A[k,k]
     - Para cada coluna j de k até n:
       - A[i,j] = A[i,j] - m[i,k] * A[k,j]
     - b[i] = b[i] - m[i,k] * b[k]

**Fase 2: Substituição Reversa**

Para i de n-1 até 0:
- x[i] = (b[i] - Σ(A[i,j] * x[j])) / A[i,i]
  - onde j vai de i+1 até n-1

### Complexidade
O(n³) operações de ponto flutuante

### Vantagens
- Método exato (exceto por erros de arredondamento)
- Garantido para matrizes não singulares
- Pivoteamento melhora estabilidade

### Desvantagens
- Modifica a matriz original
- Pode ser instável para matrizes mal condicionadas sem pivoteamento

---

## 2. Método de Gauss-Seidel

### Descrição
Método iterativo para resolver sistemas lineares que usa os valores mais recentes já calculados em cada iteração.

### Algoritmo

**Inicialização:**
- Escolher estimativa inicial x⁰ (geralmente vetor zero)
- Definir tolerância ε (ex: 0.0001)

**Iteração k:**

Para cada variável i (de 0 a n-1):
1. Calcular:
   ```
   x[i]^(k+1) = (b[i] - Σ(A[i,j] * x[j]^(k+1)) - Σ(A[i,j] * x[j]^k)) / A[i,i]
   ```
   - Primeiro somatório: j < i (valores já atualizados)
   - Segundo somatório: j > i (valores da iteração anterior)

2. Calcular erro relativo máximo:
   ```
   erro = max(|x[i]^(k+1) - x[i]^k| / |x[i]^(k+1)|)
   ```

3. Se erro < ε, parar (convergiu)

### Diferença com Jacobi
- **Jacobi:** usa todos os valores da iteração anterior
- **Gauss-Seidel:** usa valores já calculados na iteração atual
- Gauss-Seidel geralmente converge mais rápido

### Condição de Convergência
O método converge se a matriz A for:
- Estritamente diagonal dominante: |A[i,i]| > Σ|A[i,j]| para j≠i
- Simétrica e definida positiva

### Vantagens
- Requer menos memória que métodos diretos
- Bom para sistemas grandes e esparsos
- Não modifica a matriz original

### Desvantagens
- Pode não convergir para alguns sistemas
- Número de iterações depende do sistema

---

## 3. Método dos Mínimos Quadrados

### Descrição
Ajusta uma função aos dados minimizando a soma dos quadrados dos resíduos (diferenças entre valores observados e previstos).

### 3.1 Regressão Linear: y = a + bx

**Objetivo:** Minimizar E = Σ(y[i] - (a + b*x[i]))²

**Sistema Normal:**
```
n*a + (Σx)*b = Σy
(Σx)*a + (Σx²)*b = Σxy
```

**Solução (Regra de Cramer):**
```
det = n*Σx² - (Σx)²
a = (Σy*Σx² - Σx*Σxy) / det
b = (n*Σxy - Σx*Σy) / det
```

### 3.2 Regressão Parabólica: y = a + bx + cx²

**Sistema Normal 3x3:**
```
n*a + (Σx)*b + (Σx²)*c = Σy
(Σx)*a + (Σx²)*b + (Σx³)*c = Σxy
(Σx²)*a + (Σx³)*b + (Σx⁴)*c = Σx²y
```

Resolve usando Eliminação de Gauss.

### 3.3 Regressão Exponencial: y = a*e^(bx)

**Linearização:**
1. Aplicar ln em ambos lados: ln(y) = ln(a) + bx
2. Fazer z = ln(y), então: z = ln(a) + bx
3. Aplicar regressão linear em (x, z)
4. Recuperar: a = e^(ln_a)

**Nota:** Requer y > 0 para todos os pontos.

### Erro Quadrático
```
E = Σ(y[i] - ŷ[i])²
```
onde ŷ[i] é o valor previsto pelo modelo.

**Interpretação:**
- Menor erro → melhor ajuste
- Comparar erros entre modelos diferentes

---

## 4. Funções Matemáticas Implementadas Manualmente

### 4.1 Logaritmo Natural: ln(x)

**Método:** Série de Taylor

Para x > 0, usando z = (x-1)/(x+1):
```
ln(x) = 2 * Σ(z^(2k+1) / (2k+1))
```
onde k = 0, 1, 2, ..., n

**Convergência:** Rápida para x próximo de 1.

### 4.2 Exponencial: e^x

**Método:** Série de Taylor
```
e^x = Σ(x^k / k!)
```
onde k = 0, 1, 2, ..., n

**Implementação otimizada:**
```
termo[0] = 1
termo[k] = termo[k-1] * x / k
```

### 4.3 Logaritmo Base 10: log₁₀(x)

**Fórmula de mudança de base:**
```
log₁₀(x) = ln(x) / ln(10)
```

### 4.4 Potência Base 10: 10^x

**Fórmula:**
```
10^x = e^(x * ln(10))
```

---

## 5. Aplicações nos Problemas

### Problema 1: Três Minas

**Modelagem:**
- Variáveis: x₁, x₂, x₃ (volumes das minas)
- Equações: uma para cada material

Exemplo:
```
0.52*x₁ + 0.20*x₂ + 0.25*x₃ = 4800  (areia)
0.30*x₁ + 0.50*x₂ + 0.20*x₃ = 5800  (casc. fino)
0.18*x₁ + 0.30*x₂ + 0.55*x₃ = 5700  (casc. grosso)
```

**Solução:** Eliminação de Gauss

### Problema 2: Ponte de Wheatstone

**Modelagem (Leis de Kirchhoff):**

1. **Lei dos Nós:** Σi_entrada = Σi_saída
2. **Lei das Malhas:** ΣV = ΣR*i

Sistema resultante (3 correntes):
```
R₁*i₁ + R₂*i₂ = E
(R₂+R₅)*i₂ - R₅*i₃ = 0
-R₅*i₂ + (R₃+R₄+R₅)*i₃ = 0
```

**Solução:** Gauss-Seidel

### Problema 3: Regressões

**Dados experimentais F(x)** ajustados a:
- Modelo linear (tendência geral)
- Modelo parabólico (captura curvatura)
- Modelo exponencial (decaimento)

Comparar erros para escolher melhor modelo.

### Problema 4: Lei de Moore

**Modelagem:**
- N(t) = N₀ * 2^(t/T) onde T ≈ 2 anos
- Equivalente: log₁₀(N) = a + b*t

**Processo:**
1. Transformar N → log₁₀(N)
2. Regressão linear em (ano, log₁₀(N))
3. Previsão: log₁₀(N_futuro) = a + b*ano_futuro
4. Converter: N_futuro = 10^(log₁₀(N_futuro))

---

## 6. Considerações Numéricas

### Precisão
- Python usa float64 (16-17 dígitos decimais)
- Erros de arredondamento são inevitáveis
- Tolerâncias devem ser realistas (ex: 10⁻⁴, não 10⁻¹⁶)

### Estabilidade
- Pivoteamento essencial em Gauss
- Evitar divisão por números muito pequenos
- Verificar condicionamento da matriz

### Convergência
- Gauss-Seidel: verificar diagonal dominante
- Métodos iterativos: definir max_iter
- Monitorar erro a cada iteração

### Overflow/Underflow
- e^x pode crescer muito rápido
- ln(x) requer x > 0
- Verificar domínio das funções

---

## 7. Complexidade Computacional

| Método | Complexidade | Memória |
|--------|--------------|---------|
| Eliminação de Gauss | O(n³) | O(n²) |
| Gauss-Seidel | O(k*n²) | O(n²) |
| Regressão Linear | O(n) | O(1) |
| Regressão Parabólica | O(n + 27) | O(1) |

onde:
- n = tamanho do sistema/número de pontos
- k = número de iterações

---

## 8. Validação dos Resultados

### Verificação de Soluções
1. Substituir x na equação original Ax = b
2. Calcular resíduo: r = Ax - b
3. Verificar ||r|| < tolerância

### Verificação de Convergência
1. Comparar x^k com x^(k-1)
2. Erro relativo < tolerância
3. Número de iterações razoável

### Verificação de Regressões
1. Plotar dados e curva ajustada
2. Verificar resíduos
3. Comparar R² ou erro quadrático

---

**Nota:** Todos os métodos foram implementados do zero, sem uso de bibliotecas prontas como numpy.linalg, scipy.optimize, etc.
