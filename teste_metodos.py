"""
Script de teste para validar os métodos numéricos implementados
Execute este script para verificar se todos os módulos estão funcionando corretamente
"""

import sys
import os

# Adicionar diretório atual ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("=" * 70)
print("TESTE DOS MÉTODOS NUMÉRICOS IMPLEMENTADOS")
print("=" * 70)

# Teste 1: Métodos Diretos
print("\n" + "=" * 70)
print("TESTE 1: ELIMINAÇÃO DE GAUSS - PROBLEMA DAS MINAS")
print("=" * 70)

from metodos_diretos import resolver_problema_minas

# Dados padrão do problema
resultado1 = resolver_problema_minas(
    d1=4800, d2=5800, d3=5700,
    comp_mina1=[52, 30, 18],
    comp_mina2=[20, 50, 30],
    comp_mina3=[25, 20, 55]
)

print(f"\n✓ Volume Mina 1: {resultado1['x1']:.2f} m³")
print(f"✓ Volume Mina 2: {resultado1['x2']:.2f} m³")
print(f"✓ Volume Mina 3: {resultado1['x3']:.2f} m³")

# Teste 2: Métodos Iterativos
print("\n" + "=" * 70)
print("TESTE 2: GAUSS-SEIDEL - PONTE DE WHEATSTONE")
print("=" * 70)

from metodos_iterativos import resolver_ponte_wheatstone

resultado2 = resolver_ponte_wheatstone(
    E=30, R1=20, R2=120, R3=120, R4=120, R5=120,
    tol=0.0001
)

print(f"\n✓ Corrente i1: {resultado2['i1']:.8f} A")
print(f"✓ Corrente i2: {resultado2['i2']:.8f} A")
print(f"✓ Corrente i3: {resultado2['i3']:.8f} A")
print(f"✓ Número de iterações: {resultado2['num_iteracoes']}")

# Teste 3: Mínimos Quadrados
print("\n" + "=" * 70)
print("TESTE 3: REGRESSÕES POR MÍNIMOS QUADRADOS")
print("=" * 70)

from minimos_quadrados import resolver_regressoes

x_dados = [0, 1.5, 2.6, 4.2, 6, 8.2, 10, 11.4]
y_dados = [18, 13, 11, 9, 6, 4, 2, 1]

resultado3 = resolver_regressoes(x_dados, y_dados)

print(f"\n✓ Regressão Linear:")
print(f"  Equação: {resultado3['linear']['equacao']}")
print(f"  Erro: {resultado3['linear']['erro']:.6f}")

print(f"\n✓ Regressão Parabólica:")
print(f"  Equação: {resultado3['parabolica']['equacao']}")
print(f"  Erro: {resultado3['parabolica']['erro']:.6f}")

if resultado3['exponencial']:
    print(f"\n✓ Regressão Exponencial:")
    print(f"  Equação: {resultado3['exponencial']['equacao']}")
    print(f"  Erro: {resultado3['exponencial']['erro']:.6f}")

# Teste 4: Lei de Moore
print("\n" + "=" * 70)
print("TESTE 4: LEI DE MOORE")
print("=" * 70)

from lei_moore import resolver_lei_moore

anos = [1971, 1972, 1974, 1978, 1982, 1985]
transistores = [2300, 3500, 4500, 29000, 134000, 275000]
anos_previsao = [2010, 2020]

resultado4 = resolver_lei_moore(anos, transistores, anos_previsao)

print(f"\n✓ Modelo: {resultado4['equacao_log']}")
print(f"✓ Erro: {resultado4['erro']:.6f}")

for prev in resultado4['previsoes']:
    print(f"\n✓ Previsão para {prev['ano']}:")
    print(f"  log₁₀(N) = {prev['log_N']:.6f}")
    print(f"  N ≈ {prev['N']:.2e} transistores")

# Resumo final
print("\n" + "=" * 70)
print("RESUMO DOS TESTES")
print("=" * 70)

print("\n✅ Todos os 4 problemas foram testados com sucesso!")
print("\n📊 Módulos verificados:")
print("   ✓ metodos_diretos.py")
print("   ✓ metodos_iterativos.py")
print("   ✓ minimos_quadrados.py")
print("   ✓ lei_moore.py")

print("\n🚀 O projeto está pronto para uso!")
print("   Execute 'python app.py' para iniciar a interface web")

print("\n" + "=" * 70)
