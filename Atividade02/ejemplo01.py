from particula import particula

# Criar uma partícula com posição inicial (0,0), velocidade (10, 10) e massa 1 kg
p = particula(0.1, 5, 10, 10, 1)

# Simular por 2 segundos com passos de 0.1s e força nula (só gravidade atuando)
#for _ in range(20):
#    p.newton(0, -9.8, 0.1)

# Simulação: parar quando y <= 0
dt = 0.1
while p.y > 0:
    p.newton(0, -9.8, dt)

# Plotar a trajetória
p.plotar_trajetoria()