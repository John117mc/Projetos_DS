
<p align="center">
  <img  width="1000px" height="570" src="https://github.com/joaovitps/Data_Science_Projects/blob/main/Cardiovascular%20Disease%20Predict/image/cardio.jpg">
</p>

# Cardiovascular Disease Predict
Predição de Doenças Cardiovasculares.

## 1- Business Problem
A **Cardio Catch Diseases** (fictício) é uma empresa especializada em detecção de doenças cardíacas em estágios iniciais. 
O seu modelo de negócio é do tipo Serviço, ou seja, a empresa ofereço o diagnóstico precoce de uma doença cardiovascular por um certo preço.

O **preço do diagnóstico**, pago pelo cliente, varia de acordo com a precisão conseguida pelo time de especialistas, 
o cliente paga US$ 500.00 a cada 5% de acurácia acima de 50%. Por exemplo, para uma precisão de 55%, o diagnóstico c
usta US$ 500.00 para o cliente, para uma precisão de 60%, o valor é de US$1000.00 e assim por diante. 
Se a precisão do diagnóstico for 50% o cliente não paga por ele.

| Accuracy        |Cost Diagnostics |
| :------:        | :------------:  |
| 50%            | US$ 0         |
| 55%            | US$ 500       |
| 60%            | US$ 1000      |

Observe que a variação da precisão dada pelo time de especialistas, faz com que a empresa tenha ora uma operação com lucro, receita maior que o custo, ora uma operação com prejuízo, receita menor que o custo. Essa instabilidade do diagnóstico faz com que a empresa tenha um **Cashflow** imprevisível.

### Main Objective:
* Criar uma máquina preditiva com a precisão estável e evitar o cashflow.

## 2- Business Assumptions
As Minhas premissas de negócios foram:

* Os valores acima da máxima dos atributos **Systolic blood pressure** e **Diastolic blood pressure** são erros de digitação e será feito a correção.

## 3- Solution Strategy
A minha estratégia para resolver o problema foi:

**Step 01. Data Collect:** Coletar os dados pela API do Kaggle.

**Step 02. Data Cleaning:** Verificar se contém dados faltantes ou inconsistente.

**Step 03. Exploratory Data Analysis:** Analisar os atributos, validar as hipóteses e verificar a correlação entre elas. 

**Step 04. Data Preprocessing:** Preparar os dados para que o modelo de Machine Learning possa aprender corretamente.

**Step 05. Feature Scaling:** Normalizar as variaveis.

**Step 06. Machine Learning Modelling:** Treinar três classificadores de Machine Learning.

**Step 07. Hyperparameter fine-tuning:** Melhorar os parâmetros do classificador escolhido na etapa anterior.

**Step 08. Convert Model Performance to Business Values:** Converter a perfomance do modelo para a perfomance de negócio.

**Step 09. Deploy Model to Production:** Publicar o modelo na cloud: [Cardiovascular Disease App](https://cardio-disease-predict-sc30.herokuapp.com/)


## 4- Top 5 Data Insights

**Hyphotesis 01:** O grupo de pacientes com a idade acima de 50 anos são 60% das que apresentam a doença.</br>
**TRUE:** O grupo de pacientes com a idade acima de 50 anos são **77.5%** das que apresentam a doença. 

**Hyphotesis 02:** O grupo de pacientes que fumam são 40% das que apresentam a doença.</br>
**FALSE:** O grupo de pacientes que fumam são **8.4%** das que apresentam a doença.

**Hyphotesis 03:** O grupo de pacientes do gênero masculino são 30% das que apresentam a doença.</br>
**TRUE:** O grupo de pacientes do gênero masculino são **35.3%** das que apresentam a doença. 

**Hyphotesis 04:** O grupo de pacientes com o peso maior do que 90kg são 60% das que apresentam a doença.</br>
**FALSE:** O grupo de pacientes com o peso maior do que 90kg são **18.2%** das que apresentam a doença.

**Hyphotesis 05:** O grupo de pacientes que consomem álcool são 75% das que apresentam a doença. </br>
**FALSE:** O grupo de pacientes que consomem álcool são **5.2%** das que apresentam a doença.

## 5- Machine Learning Model Applied
Foram treinados três tipos de Machine Learning para poder resolver o problema:
* kNN
* Random Forest
* XGBoost

## 6- Machine Learning Model Performance
Com a base de dados pré-processada e pronta para ser submetida para os modelos de Machine Learning treinarem, os resultos obtidos foram:

| Machine Learning | Accuracy        |
| :--------------: | :-------------: |
| XGBoost          | 73.32%          |
| Random Forest    | 71.64%          |
|  kNN             | 69.96%          |

O modelo **XGBoost** foi o escolhido por ter conseguido uma precisão mais alta do que os outros modelos e seus parâmetros foram melhorados para poder aumentar seu desempenho.

| Machine Learning (tuning) | Accuracy        |
| :--------------: | :-------------: |
| XGBoost          |   74.04%       |

## 7- Business Results
O serviço atual da Cardio Catch Diseases gerava prejuizo, não tendo uma precisão dos diagnósticos estáveis. Comparando com a precisão estável do projeto finalizado, a empresa sairia ganhando implementando esse modelo de serviço.

A comparação foi feita levando em conta o **melhor e o pior cenário** de cada situação. 

| Type                               | Best Scenario   | Worst Scenario |
| :-----------------------------:    | :-------------: | :------------: |
| Specialist Team                    | US$ 70.000.000  | US$ 35.000.000 |
| Machine Learning Algorithm         | US$ 140.000.000 | US$ 105.000.000|

Cada diagnóstico pago pelo cliente, agora terá o preço de **US$ 2000.00** sem alguma variação nesse preço.

## 8- Conclusions
O objetivo proposto pela empresa era de conseguir uma precisão estável para evitar o prejuizo que estava tendo e melhorar os seus diagnósticos para os seus pacientes. Assim aumentando a procura por um diagnóstico confiável e o lucro. 

## 9- Next Steps to Improve
* Criar um pipeline para automatizar os processos.
* Tratar os outliers com mais eficiência.
* Selecionar os atributos mais relevantes.
