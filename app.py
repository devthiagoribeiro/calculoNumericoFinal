"""
Aplicação Web Flask para Cálculo Numérico
Interface web para resolução dos quatro problemas propostos
"""

from flask import Flask, render_template, request, jsonify
import sys
import os

# Adicionar diretório atual ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from metodos_diretos import resolver_problema_minas, resolver_sistema_generico
from metodos_iterativos import resolver_ponte_wheatstone
from minimos_quadrados import resolver_regressoes
from lei_moore import resolver_lei_moore

app = Flask(__name__)


@app.route('/')
def index():
    """Página principal com menu dos problemas"""
    return render_template('index.html')


@app.route('/problema1')
def problema1():
    """Problema das Minas - Métodos Diretos"""
    return render_template('problema1.html')


@app.route('/problema2')
def problema2():
    """Ponte de Wheatstone - Métodos Iterativos"""
    return render_template('problema2.html')


@app.route('/problema3')
def problema3():
    """Regressões por Mínimos Quadrados"""
    return render_template('problema3.html')


@app.route('/problema4')
def problema4():
    """Lei de Moore"""
    return render_template('problema4.html')


@app.route('/calcular_minas', methods=['POST'])
def calcular_minas():
    """Endpoint para calcular problema das minas"""
    try:
        data = request.get_json()
        
        # Extrair dados
        d1 = float(data['d1'])
        d2 = float(data['d2'])
        d3 = float(data['d3'])
        
        comp_mina1 = [float(data['mina1_areia']), float(data['mina1_fino']), float(data['mina1_grosso'])]
        comp_mina2 = [float(data['mina2_areia']), float(data['mina2_fino']), float(data['mina2_grosso'])]
        comp_mina3 = [float(data['mina3_areia']), float(data['mina3_fino']), float(data['mina3_grosso'])]
        
        # Extrair método escolhido
        metodo = data.get('metodo', 'gauss')
        
        # Resolver
        resultado = resolver_problema_minas(d1, d2, d3, comp_mina1, comp_mina2, comp_mina3, metodo)
        
        return jsonify({
            'sucesso': True,
            'resultado': resultado
        })
    
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': str(e)
        }), 400


@app.route('/calcular_wheatstone', methods=['POST'])
def calcular_wheatstone():
    """Endpoint para calcular Ponte de Wheatstone"""
    try:
        data = request.get_json()
        
        # Extrair dados
        E = float(data['E'])
        R1 = float(data['R1'])
        R2 = float(data['R2'])
        R3 = float(data['R3'])
        R4 = float(data['R4'])
        R5 = float(data['R5'])
        tol = float(data.get('tolerancia', 0.0001))
        
        # Valores iniciais (se fornecidos)
        valores_iniciais = None
        if 'i1_inicial' in data and data['i1_inicial']:
            valores_iniciais = [
                float(data['i1_inicial']),
                float(data['i2_inicial']),
                float(data['i3_inicial'])
            ]
        
        # Resolver
        resultado = resolver_ponte_wheatstone(E, R1, R2, R3, R4, R5, tol, valores_iniciais)
        
        return jsonify({
            'sucesso': True,
            'resultado': resultado
        })
    
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': str(e)
        }), 400


@app.route('/calcular_regressoes', methods=['POST'])
def calcular_regressoes():
    """Endpoint para calcular regressões"""
    try:
        data = request.get_json()
        
        # Extrair dados
        x_str = data['x_valores']
        y_str = data['y_valores']
        
        # Converter strings para listas de floats
        x_dados = [float(val.strip()) for val in x_str.split(',')]
        y_dados = [float(val.strip()) for val in y_str.split(',')]
        
        if len(x_dados) != len(y_dados):
            raise ValueError("Os vetores x e y devem ter o mesmo tamanho")
        
        if len(x_dados) < 2:
            raise ValueError("São necessários pelo menos 2 pontos")
        
        # Resolver
        resultado = resolver_regressoes(x_dados, y_dados)
        
        return jsonify({
            'sucesso': True,
            'resultado': resultado
        })
    
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': str(e)
        }), 400


@app.route('/calcular_moore', methods=['POST'])
def calcular_moore():
    """Endpoint para calcular Lei de Moore"""
    try:
        data = request.get_json()
        
        # Extrair dados
        anos_str = data['anos']
        transistores_str = data['transistores']
        previsoes_str = data['anos_previsao']
        
        # Converter strings para listas
        anos = [int(val.strip()) for val in anos_str.split(',')]
        num_transistores = [float(val.strip()) for val in transistores_str.split(',')]
        anos_previsao = [int(val.strip()) for val in previsoes_str.split(',')]
        
        if len(anos) != len(num_transistores):
            raise ValueError("As listas de anos e transistores devem ter o mesmo tamanho")
        
        if len(anos) < 2:
            raise ValueError("São necessários pelo menos 2 pontos de dados")
        
        # Resolver
        resultado = resolver_lei_moore(anos, num_transistores, anos_previsao)
        
        return jsonify({
            'sucesso': True,
            'resultado': resultado
        })
    
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': str(e)
        }), 400




@app.route('/calcular_sistema', methods=['POST'])
def calcular_sistema():
    """Endpoint para calcular sistema linear genérico"""
    try:
        data = request.get_json()
        
        # Extrair dados da matriz e vetor b
        A = data['matriz']  # Lista de listas
        b = data['vetor_b']  # Lista
        metodo = data.get('metodo', 'gauss')
        
        # Validar dimensões
        n = len(b)
        if len(A) != n or any(len(linha) != n for linha in A):
            raise ValueError("A matriz deve ser quadrada NxN onde N é o tamanho do vetor b")
        
        # Resolver
        resultado = resolver_sistema_generico(A, b, metodo)
        
        return jsonify({
            'sucesso': resultado['sucesso'],
            'resultado': resultado
        })
    
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': str(e)
        }), 400


if __name__ == '__main__':
    print("=" * 60)
    print("SISTEMA DE CÁLCULO NUMÉRICO")
    print("=" * 60)
    print("\nServidor Flask iniciado!")
    print("Acesse: http://127.0.0.1:5000")
    print("\nProblemas disponíveis:")
    print("  1. Problema das Minas (Métodos Diretos)")
    print("  2. Ponte de Wheatstone (Gauss-Seidel)")
    print("  3. Regressões por Mínimos Quadrados")
    print("  4. Lei de Moore")
    print("\nPressione Ctrl+C para encerrar")
    print("=" * 60)
    
    app.run(debug=True, host='127.0.0.1', port=5000)
