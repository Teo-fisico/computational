import matplotlib.pyplot as plt
class particula:
    def __init__(self,x, y,vx,vy,massa):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.massa=massa
        self.g = 9.81  # gravidade
        self.trajetoria_x = [x]
        self.trajetoria_y = [y]

    def newton(self,fx,fy,dt):
        # Calcula aceleração
        ax = fx / self.massa
        ay = (fy / self.massa)  

        # Atualiza velocidades
        self.vx += ax * dt
        self.vy += ay * dt

        # Atualiza posições
        self.x += self.vx * dt
        self.y += self.vy * dt - 0.5 * self.g * dt**2  # fórmula ajustada para gravidade

        # Armazena para plot
    #  self.trajetoria_x.append(self.x)
    #    self.trajetoria_y.append(self.y)
    # Armazena para plot se ainda não atingiu o chão
        if self.y >= 0:
            self.trajetoria_x.append(self.x)
            self.trajetoria_y.append(self.y)
        else:
            self.y = 0
            self.trajetoria_x.append(self.x)
            self.trajetoria_y.append(self.y)

    def plotar_trajetoria(self):
        plt.plot(self.trajetoria_x, self.trajetoria_y,color='red', marker='o')
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.title('Trajetória da Partícula')
        plt.grid(True)
        #plt.savefig('Simulação.png',dpi=300)
        plt.show()
     
    

            