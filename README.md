# Sistema de Cálculo Numérico - Interface Web

Projeto completo de resolução de problemas de Cálculo Numérico usando métodos implementados manualmente em Python, com interface web Flask.

## 📋 Descrição

Este projeto implementa soluções para quatro problemas específicos de Cálculo Numérico:

1. **Problema das Três Minas** - Sistema linear resolvido por Eliminação de Gauss
2. **Ponte de Wheatstone** - Sistema linear resolvido por Gauss-Seidel
3. **Regressões por Mínimos Quadrados** - Ajuste de curvas (linear, parabólica, exponencial)
4. **Lei de Moore** - Previsão usando regressão logarítmica

## 🎯 Características

- ✅ Todos os métodos numéricos implementados **manualmente** (sem numpy.linalg, scipy, etc.)
- ✅ Interface web simples e intuitiva usando Flask
- ✅ Código modular e bem comentado
- ✅ Exibição detalhada dos passos de cada método
- ✅ Permite entrada de novos dados para todos os problemas

## 📁 Estrutura do Projeto

```
calculoNumerico/
│
├── app.py                      # Aplicação Flask principal
├── metodos_diretos.py          # Eliminação de Gauss
├── metodos_iterativos.py       # Método de Gauss-Seidel
├── minimos_quadrados.py        # Regressões (linear, parabólica, exponencial)
├── lei_moore.py                # Análise da Lei de Moore
│
├── templates/                  # Templates HTML
│   ├── index.html             # Página principal
│   ├── problema1.html         # Interface Problema 1
│   ├── problema2.html         # Interface Problema 2
│   ├── problema3.html         # Interface Problema 3
│   └── problema4.html         # Interface Problema 4
│
├── requirements.txt           # Dependências Python
└── README.md                  # Este arquivo
```

## 🔧 Instalação e Execução

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passo 1: Instalar dependências

```bash
cd /Users/thiagoribeiro/Documents/calculoNumerico
pip install -r requirements.txt
```

### Passo 2: Executar a aplicação

```bash
python app.py
```

### Passo 3: Acessar a interface web

Abra seu navegador e acesse:
```
http://127.0.0.1:5000
```

## 📊 Problemas Resolvidos

### Problema 1: Três Minas (Métodos Diretos)

**Enunciado:** Calcular volumes a extrair de três minas para atender demandas de areia, cascalho fino e cascalho grosso.

**Dados padrão:**
- Demandas: 4800 m³ (areia), 5800 m³ (cascalho fino), 5700 m³ (cascalho grosso)
- Composições das minas em percentuais

**Método:** Eliminação de Gauss com pivoteamento parcial

**Recursos:**
- Entrada personalizável de demandas
- Ajuste da composição de cada mina
- Exibição do sistema linear
- Passos detalhados da eliminação

### Problema 2: Ponte de Wheatstone (Métodos Iterativos)

**Enunciado:** Calcular correntes elétricas em um circuito usando as Leis de Kirchhoff.

**Dados padrão:**
- E = 30 V
- R1 = 20 Ω
- R2 = R3 = R4 = R5 = 120 Ω

**Método:** Gauss-Seidel

**Recursos:**
- Ajuste de tensões e resistências
- Configuração da tolerância (padrão: 0.0001)
- Valores iniciais personalizáveis
- Histórico completo de iterações
- Número de iterações até convergência

### Problema 3: Regressões por Mínimos Quadrados

**Enunciado:** Ajustar três tipos de curvas aos dados experimentais.

**Dados padrão:**
- x = [0, 1.5, 2.6, 4.2, 6, 8.2, 10, 11.4]
- F(x) = [18, 13, 11, 9, 6, 4, 2, 1]

**Métodos:** 
- Regressão Linear: y = a + bx
- Regressão Parabólica: y = a + bx + cx²
- Regressão Exponencial: y = a·e^(bx)

**Recursos:**
- Entrada de novos conjuntos de dados
- Cálculo simultâneo das três regressões
- Comparação de erros quadráticos
- Detalhes completos dos cálculos

### Problema 4: Lei de Moore

**Enunciado:** Prever o número de transistores em anos futuros usando dados históricos.

**Dados padrão:**
- Anos: 1971, 1972, 1974, 1978, 1982, 1985
- Transistores: 2300, 3500, 4500, 29000, 134000, 275000
- Previsões para: 2010, 2020

**Método:** Regressão linear sobre log₁₀(N)

**Recursos:**
- Entrada de novos dados históricos
- Previsões para múltiplos anos
- Resultados em formato logarítmico e normal
- Notação científica e valor aproximado

## 🧮 Métodos Numéricos Implementados

### 1. Eliminação de Gauss com Pivoteamento Parcial

Resolve sistemas lineares Ax = b através de:
1. Fase de eliminação (triangularização)
2. Pivoteamento parcial para estabilidade numérica
3. Substituição reversa

### 2. Método de Gauss-Seidel

Método iterativo que:
1. Parte de uma estimativa inicial
2. Atualiza cada variável usando valores já calculados
3. Converge quando o erro relativo < tolerância
4. Exibe número de iterações

### 3. Mínimos Quadrados

Implementa três tipos de ajuste:

**Linear:** Resolve sistema normal 2x2
**Parabólica:** Resolve sistema normal 3x3 usando Gauss
**Exponencial:** Lineariza com ln(y) e aplica regressão linear

### 4. Funções Matemáticas Manuais

Implementações próprias de:
- `logaritmo_natural(x)`: usando série de Taylor
- `exp_manual(x)`: usando série de Taylor
- `logaritmo_base10(x)`: ln(x)/ln(10)
- `potencia_base10(x)`: e^(x·ln(10))

## 💻 Uso da Interface Web

### Menu Principal

Selecione um dos quatro problemas para resolver.

### Formulários

Cada problema possui um formulário com:
- Campos pré-preenchidos com valores padrão
- Possibilidade de alterar todos os parâmetros
- Botão "Calcular" para executar

### Resultados

A interface exibe:
- Valores calculados com precisão adequada
- Sistema linear montado
- Passos detalhados dos métodos
- Histórico de iterações (quando aplicável)
- Comparações de erros (regressões)

### Novo Cálculo

Após ver os resultados, basta alterar os valores no formulário e clicar em "Calcular" novamente.

## 📝 Observações Importantes

1. **Implementação Manual:** Nenhuma função pronta de bibliotecas numéricas foi utilizada. Todos os algoritmos foram codificados do zero.

2. **Validação:** Os métodos foram testados com os dados padrão dos problemas propostos.

3. **Precisão:** A tolerância padrão de 0.0001 garante convergência adequada no Gauss-Seidel.

4. **Exponencial:** Para regressão exponencial, todos os valores de y devem ser positivos.

5. **Convergência:** O método de Gauss-Seidel pode não convergir para alguns sistemas. Certifique-se de que o sistema tem diagonal dominante quando possível.

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido para demonstrar a implementação prática de métodos numéricos fundamentais:

- **Tópico 01:** Métodos Diretos para Sistemas Lineares
- **Tópico 02:** Métodos Iterativos para Sistemas Lineares  
- **Tópico 03:** Interpolação e Mínimos Quadrados