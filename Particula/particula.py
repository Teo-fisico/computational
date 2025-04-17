class particula:
    def __init__(self,x, y,vx,vy,massa):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.massa=massa

    def newton(self,fx,fy,dt):
        # ax=F/m
        ax=fx/self.massa
        ay=fy/self.massa
        # vx=v0+a*t
        self.vx+=ax*dt
        self.vx+=ay*dt
        # x=x0+v*dt
        self.x+=self.vx*dt
        self.y+=self.vy*dt

            