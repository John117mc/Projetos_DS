# HOUSE PRICE PREDICTION 

<p align="center">
  <img  width="1000px" height="350" src="https://s2.best-wallpaper.net/wallpaper/3840x2160/1809/Some-money-dollars_3840x2160.jpg">
</p>




## 1- Business Problem
O CEO da **House Moon Company**(fictÍcio), deseja comprar casas com preço baixo e revende-lás com o preço mais alto. Encontre bons negócios dentro do portfólio disponível, ou seja, encontrar casas com preço baixo, que tenham um ótimo potencial de venda.

### Main Objective:
Uma vez o imóvel comprado, qual o melhor preço para vendê-lo?

* A House Moon deveria fazer uma reforma para aumentar o preço da venda? Quais seriam as sugestões de mudanças? Qual o incremento no preço dado por cada opção de reforma?

## 2- Business Assumptions
As Minhas premissas de negócios foram:

* Todos os imóveis no portfolio estão disponiveis para a compra.

## 3- Solution Strategy
A minha estratégia para resolver o problema foi:

**Step 01. Data Collect:** Coletar os dados do Kaggle.

**Step 02. Data Cleaning:** Verificar se contém dados faltantes ou inconsistente.

**Step 03. Exploratory Data Analysis:** Analisar os atributos, validar as hipóteses e verificar a correlação entre elas. 

**Step 04. Data Preprocessing:** Preparar os dados para que o modelo de Machine Learning possa aprender corretamente.

**Step 05. Feature Selection:** Escolhar os atributos mais relevantes.

**Step 06. Feature Scaling:** Normalizar as variaveis.

**Step 07. Machine Learning Modelling:** Treinar três algoritmo de Machine Learning.

**Step 08. Cross-validation:** Avaliar o desempenho dos algoritmos.

**Step 09. Hyperparameter fine-tuning:** Melhorar os parâmetros do classificador escolhido na etapa anterior.

**Step 10. Convert Model Performance to Business Values:** Converter a perfomance do modelo para a perfomance de negócio.

**Step 11. Deploy Model to Production:** Publicar o modelo na cloud: [House Price App](https://house-price-predict-sc30.herokuapp.com/)


## 4- Top 3 Data Insights

**Hyphotesis 01:** Os imóveis que foram construídos antes de 1960 são 10% mais caros, na média.</br>
**FALSE:** Os imóveis que foram construídos antes de 1960 são **4%** mais baratos do que os novos, na média. 

**Hyphotesis 02:** Os imóveis com a sala de estar maior que 2000ft são 25% mais caros, na média.</br>
**TRUE:** Os imóveis com a sala de estar maior que 2000ft são **55%** mais caros, na média

**Hyphotesis 03:** Os imóveis com mais de dois banheiros são 10% mais caros, na média.</br>
**TRUE:** Os imóveis com mais de dois banheiros são **37%** mais caros, na média. 

## 5- Machine Learning Model Applied
Foram treinados três tipos de Machine Learning para poder resolver o problema:
* Random Forest 
* ElasticNet
* Lasso

## 6- Machine Learning Model Performance
Com a base de dados pré-processada e pronta para ser submetida para os modelos de Machine Learning treinarem, os resultos obtidos foram:

| Machine Learning | Mean Absolute Error       |
| :--------------: | :-------------: |
| Random Forest          | 64920          |
| ElasticNet    | 121162         |
| Lasso             | 116520          |

Os modelos foram submetidos em cross validation com seus hiperparâmetros e o desempenho do algoritmo Lasso e Random Forest teve uma média ruim. Somente o ElasticNet teve um desempenho melhor.

A média do Mean Absolute Error após encontrar o hiperparâmetros e treina-los utilizando cross-validation.

| Machine Learning | Mean Absolute Error       |
| :--------------: | :-------------: |
| Random Forest          | 66452          |
| ElasticNet    | 117945        |
| Lasso             | 117941         |

## 7- Business Results
O preço da venda dos imóveis foi calculado nas seguintes condições:

* 1- 30% a mais no preço caso o imóvel não foi renovado nenhuma vez.
* 2- 10% a mais no preço caso o imóvel ja foi renovado.

| Renovated Condition | Total Cost          | Sales Revenue        |Profit               |
| :---------------:   | :-------------:     | :-----------:        | :----:              |
| 1                   | US$ 9.251.729.974|US$ 12.027.248.966 |US$ 2.775.518.992 |
| 2                   | US$ 424.000.423  |US$ 466.400.465    |US$ 42.400.042    |
| **TOTAL**           | US$ 9.675.730.397|US$ 12.493.649.431 |US$ 2.817.919.034 |

A House Moon reformando seus imóveis teria um lucro de: **US$ 2.817.919.034**

## 8- Conclusions
Utilizando a métrica **Mean Absolute Error** o modelo de regressão conseguiu um bom resultado em seu treino e na fase exploratória de dados foi possível extrair alguns Insights valiosos para a House Moon.

## 9- Next Steps to Improve
* Melhorar as métricas de avaliação.
