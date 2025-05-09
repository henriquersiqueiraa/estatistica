import numpy as np
import matplotlib.pyplot as plt

# Definindo a área de plotagem
plt.figure(figsize=(12, 4))

# Fixando a inicialização do gerador de números aleatórios
np.random.seed(0)

# Dados de exemplo
x = np.random.randn(100)
y = np.random.randn(100)

# Criando o gráfico de dispersão
plt.scatter(x, y, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de Dispersão')
plt.grid(True)

# Exibindo o gráfico
plt.show()