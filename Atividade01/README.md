# 📉 Gradiente Descendente

Este repositório apresenta uma implementação simples do algoritmo de **Gradiente Descendente**, um dos métodos de otimização mais utilizados em aprendizado de máquina. A aplicação é feita sobre umas funções quadráticas unidimensional e bidimensional com visualizações gráficas que demonstram a convergência ao mínimo.

---

## 📌 Descrição

O **Gradiente Descendente** é um algoritmo iterativo que ajusta os parâmetros de uma função na direção oposta ao gradiente, com o objetivo de minimizar seu valor. É um componente fundamental de muitos algoritmos de machine learning, como regressão linear, regressão logística e redes neurais.

A equação de atualização do gradiente descendente é:

$$
\theta_{t+1} = \theta_t - \alpha \nabla J(\theta_t)
$$

- $\theta$: parâmetro que queremos otimizar

- $t$: índice da iteração

- $\alpha$: taxa de aprendizado (learning rate)

- $\nabla J(\theta_t)$: gradiente da função de custo $J$ em relação a $\theta$

---

## 📉 Resultados

A função utilizada para teste é uma parábola com mínimo conhecido. O algoritmo foi executado com diferentes taxas de aprendizado, e observou-se que:

- O algoritmo converge ao mínimo em poucas iterações com taxa adequada;
- Taxas muito altas causam oscilações ou divergência;
- Taxas muito baixas tornam a convergência lenta.

---

## 📊 Gráficos incluídos

Os seguintes gráficos foram gerados e estão disponíveis na pasta `image1/`:

- **Gráfico de convergência questão 1**  
  Mostra como o valor de `x` se aproxima do mínimo ao longo das iterações com taxa de aprendizado $\alpha=0,2$.  
  ![Gráfico de convergência](./image1/alfame.png)


  Além disso, mostra o caminho percorrido pelo algoritmo sobre a curva da função para uma taxa de aprendizado maior ($\alpha=0,9$) e tem uma convergência oscilante.  
  ![Gráfico da descida](./image1/alfama.png)

---
- **Gráfico de convergência de questão 2**

Na seguinte figura mostra-se a convergência lenta, para um ponto inicial perto do máximo global e uma taxa $\alpha=0,1$.
![Gráfico de convergência](./image1/q21.png)

Para o mesmo ponto inicial e uma taxa de aprendizado maior não converge e dá como resultado errado (ao máximo global). 

![Gráfico de convergência](./image1/q21b.png)


Para um ponto inicial $x=2$ e uma taxa de aprendizado $\alpha=0,1$ a convergência é rápida.
![Gráfico de convergência](./image1/q21c.png)

Na mesma concição inical e uma taxa maior converge rápidamente no mínimo do lado oposto. 

![Gráfico de convergência](./image1/q21d.png)


Para determinar o valor mínimo global depende de taxa de aprendizado e ponto inicial. 

---

- **Gráfico de convergência de questão 3**

As figuras mostram-se as convergências dos mínimos dependentes do taxa de aprendizado.


![Gráfico de convergência](./image1/31.png)

![Gráfico de convergência](./image1/32.png)

---
- **Gráfico de convergência de questão 4**

Na seguinte figura também apresenta-se a dependência da taxa de aprendizado e ponto inicial para converger a um mínimo local ou global.

![Gráfico de convergência](./image1/min_glo.png)

Finalmente, a figura mostra a convergência em função de épocas e existendo uma estabilidade para maiores que época=20. 

![Gráfico de convergência](./image1/conv.png)
