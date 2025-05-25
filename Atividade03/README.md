Redes Neurais 

1. Scikit-Learn: 
Serve para Modelos simples, fácil de usar, tem o Interface de alto nível, treinamento como ajuste de modelos estatísticos.

Usa a classe MLPClassifier ou MLPRegressor para redes neurais feedforward (perceptron multicamadas), não permite redes complexas (como CNNs ou RNNs), o treinamento é feito com o método fit(), e utiliza algoritmos como backpropagation+otimização L-BFGS ou SGD.

2. Pythorch
É Flexível, intuitivo, muito usado redes complexas e pesquisas. Definição dinâmica de grafos computacionais.

Define a rede como uma classe (herdando de torch.nn.Module).

O loop de treinamento é manual: Forward pass → cálculo da saída, cálculo da função de perda,    Backward pass → computação dos gradientes (loss.backward()) e atualização dos pesos (optimizer.step()).

3. TensorFlow

Maior Produtividade, implementação e também usada na pesquisa.

Abordagem: Grafo computacional (TensorFlow Core) ou API de alto nível (Keras).

O funcionamento: com o Keras (API de alto nível), treinamento é simples com model.fit(),com o TensorFlow Core, é possível fazer treinamento manual com GradientTape(), suporta desde redes simples até arquiteturas complexas (CNN, RNN, Transformers, etc.).

O TensorFlow é mais utilizado na indústria, tem bom suporte para implementação (mobile, web, servidores) e escalabilidade.

Nessa atividade usou-se as três pincipais bibliotecas para conferir suas predições em funções trigonomêtricas, distribuição Gaussiana e a função Sinc (usado em óptica). Os resultados dependem muito de: parâmetros (pesos (w) e bias (b)) e hiperparâmetros (taxa de aprendizado, número de épocas (epochs), tamanho de batch, número de camadas, neurônios por camada, função de ativação, otimizador, etc.).  



