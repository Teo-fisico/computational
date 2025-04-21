from particula import particula
import matplotlib.pyplot as plt

# parâmetros de iniciais
x0=0 #(m)
y0=0 #(m)
vx0=10 #(m/s)
vy0=10 # (m/s)
massa=1 # massa (kg)
#
# Criando una particula
particula=particula(x0,y0,vx0,vy0,massa)

#Força gravitacional (N)
fx=0
fy=-9.8  
# intervalo de tempo
dt=0.1
# armazenar posição
xs=[particula.x]
ys=[particula.y]
vxs=[particula.vx]
vys=[particula.vy]
tempos=[0]
# a partícula não pode pasar o solo

tempo=0
while particula.y>=0:
    particula.newton(fx,fy,dt)
    tempo +=dt

    xs.append(particula.x)
    ys.append(particula.y)
    vxs.append(particula.vx)
    vys.append(particula.vy)
    tempos.append(tempo)

#plotando a trajetória
plt.plot(xs,ys)
plt.title("Movimento parabólico")
plt.xlabel("x(m)")
plt.ylabel("y(m)")
plt.grid(True)
plt.show()
