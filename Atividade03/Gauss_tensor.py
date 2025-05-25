import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 1. Generar datos de entrenamiento (con ruido)
np.random.seed(42)
tf.random.set_seed(42)

x_train = np.linspace(-10, 10, 100).reshape(-1, 1)
sigma=0.8
y_train = np.exp(-x_train**2/(2*sigma**2))
noise = 0.1 * np.random.randn(*y_train.shape)
y_train_noisy = y_train + noise

# 2. Definir y entrenar el modelo FCNN con tanh
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='tanh', input_shape=(1,)),
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(x_train, y_train_noisy, epochs=1000, verbose=0)

# 3. Generar datos de prueba
x_test = np.linspace(-11, 11, 100).reshape(-1, 1)
y_test = np.exp(-x_test**2/(2*sigma**2))

# 4. Realizar predicciones
y_pred = model.predict(x_test)

# 5. Evaluar con MSE y visualizar resultados
mse = tf.keras.losses.MeanSquaredError()
test_mse = mse(y_test, y_pred).numpy()
print(f"Test MSE: {test_mse:.4f}")

plt.figure(figsize=(10, 5))
plt.plot(x_test, y_test, label='Verdadeiro Gaussiana', linewidth=2)
plt.plot(x_test, y_pred, label='Predição', linestyle='--')
plt.scatter(x_train, y_train_noisy, label=' Dados de Treinamento com ruído', color='red', s=10)
plt.title('Aproximación de exp(-x^2/(2*s^2)) con FCNN (tanh) - TensorFlow')
plt.xlabel('x')
plt.ylabel('exp(-x^2/(2*s^2))')
plt.legend()
plt.grid(True)
plt.savefig('sen_tensor.png', dpi=300)
plt.show()
