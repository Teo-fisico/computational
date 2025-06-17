import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

# 1. Generate Training Data
np.random.seed(42)  # for reproducibility
num_samples = 100
x_train = np.random.uniform(-10, 10, num_samples).reshape(-1, 1)  # Reshape to (n_samples, n_features)
gauss_values_train = np.exp(-x_train**2)

# Add some noise to the training data (optional, but can make it more realistic)
noise = np.random.normal(0, 0.01, gauss_values_train.shape)
gauss_values_train += noise

# 2. Define and Train the FCNN Model
# MLPRegressor expects input features to be 2D arrays (n_samples, n_features)
# For a simple angle input, n_features is 1

# Define o modelo
model = MLPRegressor(
    hidden_layer_sizes=(10,10,10), # 3 camadas ocultas com  10 neuronas
    activation='tanh',         # Rectified Linear Unit activation function
    solver='adam',             # Optimização de algoritmo
    max_iter=100000,           # Maximo numero de iterações
    random_state=42,           # para reproducibilidade,
    learning_rate_init = 0.001,# taxa de aprendizado
    tol = 1e-8 # tolerância
)

# Train the model
model.fit(x_train, gauss_values_train)

# 3. Generate Test Data for Evaluation
num_test_samples = 50
x_test = np.linspace(-10, 10, num_test_samples).reshape(-1, 1)
gauss_values_true = np.exp(-x_test**2)

# 4. Make Predictions
gauss_values_predicted = model.predict(x_test)

# 5. Evaluate the Model (Optional, but good practice)
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(gauss_values_true, gauss_values_predicted)
print(f"Mean Squared Error on Test Data: {mse}")

# 6. Visualize the Results
plt.figure(figsize=(10, 6))
plt.scatter(x_train, gauss_values_train, label='Training Data', alpha=0.5)
plt.plot(x_test, gauss_values_true, label='True Gauss(x)', color='blue')
plt.plot(x_test, gauss_values_predicted, label='Predicted Gauss(x)', color='red')
plt.xlabel('x')
plt.ylabel('exp(-x^2)')
plt.title('FCNN Interpolation of G(x)')
plt.legend()
plt.grid(True)
#plt.savefig('Gauss',dpi=300)
plt.show()