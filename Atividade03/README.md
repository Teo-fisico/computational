## 🧠 Resumo de Redes Neurais

As **Redes Neurais Artificiais (RNAs)** são modelos computacionais inspirados no funcionamento do cérebro humano, utilizados principalmente para tarefas de **aprendizado supervisionado e não supervisionado**, como classificação, regressão, detecção de padrões, tradução automática, reconhecimento de fala e imagens, entre outros.

### 🧩 Estrutura Básica

- **Neuronios (ou unidades)**: recebem entradas, aplicam pesos, somam e passam por uma função de ativação.
- **Camadas**:
  - **Entrada (Input Layer)**: recebe os dados.
  - **Ocultas (Hidden Layers)**: fazem o processamento intermediário.
  - **Saída (Output Layer)**: produz o resultado final.
- **Pesos e Biases**: parâmetros treináveis que determinam como a rede transforma os dados.

### ⚙️ Funcionamento

1. **Forward Propagation**: os dados entram e passam pelas camadas até a saída.
2. **Função de perda (Loss Function)**: calcula o erro entre a saída da rede e o valor real.
3. **Backpropagation**: o erro é propagado para ajustar os pesos usando **gradientes**.
4. **Otimização**: algoritmos como **Gradient Descent** ou **Adam** atualizam os pesos para minimizar a perda.

### 🔥 Tipos Comuns de Redes Neurais

| Tipo                        | Aplicação Principal                     |
|-----------------------------|------------------------------------------|
| **Perceptron Multicamadas (MLP)** | Classificação, regressão                |
| **Convolucional (CNN)**         | Visão computacional (imagens, vídeos)   |
| **Recorrente (RNN, LSTM, GRU)** | Sequências temporais (texto, áudio)     |
| **Transformers**               | NLP, tradução automática, LLMs          |
| **Autoencoders**              | Compressão, redução de dimensionalidade  |
| **GANs (Redes Generativas)**  | Geração de imagens, dados sintéticos     |

### 🧮 Funções de Ativação

- **ReLU**: \( f(x) = \max(0, x) \) (mais usada em redes profundas)
- **Sigmoid**: saída entre 0 e 1 (problemas binários)
- **Tanh**: saída entre -1 e 1
- **Softmax**: transforma vetores em probabilidades (multi-classe)

### 📈 Treinamento

- **Dados de entrada** (X) e saídas esperadas (Y)
- Divisão: treino, validação e teste
- **Épocas**: número de vezes que a rede vê todos os dados
- **Batch size**: número de amostras por atualização
- **Overfitting**: quando a rede aprende demais os dados de treino — prevenir com regularização, dropout, etc.

---
## 🔍 Scikit-learn — Biblioteca de Machine Learning em Python

**Scikit-learn** é uma biblioteca open-source voltada para **aprendizado de máquina (machine learning)** clássico. Baseada em NumPy, SciPy e matplotlib, é amplamente utilizada por sua **facilidade de uso, desempenho e integração com o ecossistema científico Python**.

### 🧠 Principais Funcionalidades

- **Modelos Supervisionados**:
  - Classificação: `LogisticRegression`, `RandomForestClassifier`, `SVC`, etc.
  - Regressão: `LinearRegression`, `Ridge`, `SVR`, etc.
- **Modelos Não Supervisionados**:
  - Clustering: `KMeans`, `DBSCAN`, `AgglomerativeClustering`
  - Redução de dimensionalidade: `PCA`, `TSNE`
- **Pré-processamento de Dados**:
  - Normalização, padronização: `StandardScaler`, `MinMaxScaler`
  - Codificação de variáveis: `OneHotEncoder`, `LabelEncoder`
  - Transformações: `PolynomialFeatures`, `PowerTransformer`
- **Seleção de Modelos**:
  - Validação cruzada: `cross_val_score`, `GridSearchCV`, `RandomizedSearchCV`
  - Pipelines para encadeamento de etapas
- **Métricas de Avaliação**:
  - Acurácia, precisão, recall, f1-score, curva ROC, matriz de confusão, etc.

---

## 🔥 PyTorch — Framework de Deep Learning Flexível e Poderoso

**PyTorch** é um framework de **aprendizado profundo (deep learning)** desenvolvido pelo Facebook AI Research. É conhecido por sua **flexibilidade, código limpo e execução dinâmica**, o que o torna muito popular em pesquisa e prototipagem rápida.

### 🧠 Principais Características

- **Tensores**: estrutura de dados similar ao NumPy, mas com suporte a GPU.
- **Autograd**: sistema de diferenciação automática para treinar redes neurais.
- **Rede Neural Modular**: uso de `torch.nn` para definir modelos customizados.
- **Treinamento Dinâmico**: define-by-run (gráficos computacionais dinâmicos).
- **Integração com CUDA**: fácil uso de GPUs para aceleração.
- **Comunidade ativa e grande ecossistema**: TorchVision, TorchText, TorchAudio, etc.
---

## 🧠 TensorFlow — Framework de Deep Learning Escalável e de Produção

**TensorFlow** é um framework open-source desenvolvido pelo **Google** para **aprendizado de máquina e deep learning**. Projetado para rodar de forma eficiente em CPUs, GPUs e TPUs, é altamente utilizado em ambientes de **produção, pesquisa e dispositivos móveis**.

### 🌟 Principais Características

- **Desenvolvimento e Produção**: ideal para escalar modelos em servidores, edge devices e navegadores.
- **Keras**: API de alto nível integrada ao TensorFlow para construção rápida de modelos.
- **Execução Eager e Grafos**: combina facilidade de prototipação com desempenho otimizado.
- **Suporte a GPU/TPU**: paralelização e aceleração automática.
- **Ferramentas adicionais**: TensorBoard (visualização), TensorFlow Lite (mobile), TensorFlow.js (web), TF-Serving (deploy).
---