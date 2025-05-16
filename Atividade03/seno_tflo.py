import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 1. Generar datos de entrenamiento (con ruido)
np.random.seed(42)
tf.random.set_seed(42)

x_train = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
y_train = np.sin(x_train)
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
x_test = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
y_test = np.sin(x_test)

# 4. Realizar predicciones
y_pred = model.predict(x_test)

# 5. Evaluar con MSE y visualizar resultados
mse = tf.keras.losses.MeanSquaredError()
test_mse = mse(y_test, y_pred).numpy()
print(f"Test MSE: {test_mse:.4f}")

plt.figure(figsize=(10, 5))
plt.plot(x_test, y_test, label='True sin(x)', linewidth=2)
plt.plot(x_test, y_pred, label='Predicted', linestyle='--')
plt.scatter(x_train, y_train_noisy, label='Noisy Train Data', color='red', s=10)
plt.title('Aproximación de sin(x) con FCNN (tanh) - TensorFlow')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()
