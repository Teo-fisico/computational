import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np

# 1. Generar datos de entrenamiento (con ruido)
torch.manual_seed(0)

x_train = torch.linspace(-10, 10, 200).unsqueeze(1)  # (200, 1)
y_train = torch.sinc(x_train / np.pi)  # sinc(x) = sin(pi x)/(pi x)

# Agregar ruido
noise = 0.05 * torch.randn_like(y_train)
y_train_noisy = y_train + noise

# 2. Definir el modelo FCNN con tanh
class FCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(1, 64),
            nn.Tanh(),
            nn.Linear(64, 64),
            nn.Tanh(),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.net(x)

model = FCNN()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Entrenamiento
epochs = 1000
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    output = model(x_train)
    loss = criterion(output, y_train_noisy)
    loss.backward()
    optimizer.step()
    
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.6f}")

# 3. Datos de prueba
x_test = torch.linspace(-10, 10, 400).unsqueeze(1)
y_test = torch.sinc(x_test / np.pi)

# 4. Predicciones
model.eval()
with torch.no_grad():
    y_pred = model(x_test)

# 5. Evaluar y visualizar
mse = criterion(y_pred, y_test)
print(f"\nTest MSE: {mse.item():.6f}")

plt.figure(figsize=(10, 5))
plt.plot(x_test.numpy(), y_test.numpy(), label='Verdadeiro sinc(x)', linewidth=2)
plt.plot(x_test.numpy(), y_pred.numpy(), label='Predição', linestyle='--')
plt.scatter(x_train.numpy(), y_train_noisy.numpy(), label='Dados de treinamento com ruído', color='red', s=10)
plt.title('Aproximação de sinc(x) com FCNN (tanh) - PyTorch')
plt.xlabel('x')
plt.ylabel('sinc(x)')
plt.legend()
plt.grid(True)
plt.show()
