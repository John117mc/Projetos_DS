<p align="center">
  <img  width="1000px" height="570" src="https://github.com/joaovitps/Data_Science_Projects/blob/main/House%20Rocket%20Analysis/image/house.jpg">
</p>
Gerar Insights acionáveis para o time de negócio.

## 1- Business Problem
O CEO da House Rocket Company, deseja comprar casas com preço baixo e revende-lás com o preço mais alto. Encontre bons negócios dentro do portfólio disponível, ou seja, encontrar casas com preço baixo, em ótima localização e que tenham um ótimo potencial de venda

**Main Objective:**
* Quais são os imóveis que a House Rocket deveria comprar e por qual preço?
* Uma vez o imóvel comprado, qual o melhor momento para vendê-lo e por qual preço?</br>
        **1-** Se o preço da compra for maior que a mediana da região + sazonalidade. O preço da venda será igual ao preço da compra + 10%</br>
        **2-** Se o preço da compra for menor que a mediana da região + sazonalidade. O preço da venda será igual ao preço da compra + 30%

## 2- Business Assumptions
* As estações do ano influenciam nos preços dos imóveis.
* Todos os imóveis do dataset estão disponíveis para a compra.

## 3- Solution Strategy
**Data Collect:** Coletar os dados no site do Kaggle.

**Data Cleaning:** Verificar se têm dados missing e alterar os tipos de dados.

**Hyphotesis:** Criar as hipóteses.

**Feature Engineering:** Criar novos atributos para a construção dos relatórios.

**EDA:** Validar as hipóteses gerando novos Insights para a empresa.

**Reports:** Criar os relatórios com base nas perguntas de negócio.

**Deploy:** Criar uma aplicação web com o Streamlit com os relatórios e as hipóteses e subir na Cloud Heroku. [Aplicação do Streamlit no Heroku.](https://houseanalyticssc30.herokuapp.com/)


## 4- Top 5 Data Insights

**Hyphotesis 01:** Imóveis com mais de 3 quartos, tem a sala de estar 30% maior, na média.</br>
**TRUE:** Imóveis com mais de 3 quartos tem a sala de estar 82% maior, na média.

**Hyphotesis 02:** Imóveis com construção e design de alta qualidade de 11 a 13 são 50% mais caros, na média.</br>
**TRUE:** Imóveis com construção e design de alta qualidade são 227% mais caros, na média.

**Hyphotesis 03:** Imóveis com data de construção menor que 1955, são 50% mais baratos, na média.</br>
**FALSE:** Imóveis com data de construção menor que 1995 são 2% mais baratos, na média.

**Hyphotesis 04:** Imóveis que possuem vista para água, são 30% mais caros, na média.</br>
**TRUE:** Imóveis com vista para a água são 213% mais caros, na média.

**Hyphotesis 05:** Imóveis com construção e design de alta qualidade de 11 a 13 são 50% mais caros, na média.</br>
**TRUE:** Imóveis com construção e design de alta qualidade são 227% mais caros, na média.

## 5- Business Results
O preço de venda dos imóveis foi calculado nas seguintes condições:

* **1-** Se o preço da compra for maior que a mediana da região + sazonalidade. O preço da venda será igual ao preço da compra + 10%
    
* **2-** Se o preço da compra for menor que a mediana da região + sazonalidade. O preço da venda será igual ao preço da compra + 30%


| Sale Condition | Total Cost | Sales Revenue  | Profit |
| :------------: | :--------: | :------------: | :-----: |
|1               |7.427.092.990.00	 |8.169.802.289.00 |742.709.299.00 |
| 2              | 4.245.832.018.00 | 5.519.581.623.40 | 1.273.749.605.40 |
| **TOTAL**      | 11.672.925.008.00 | 13.689.383.912.40 | 2.016.458.904.40 |


O lucro total obtido foi de: **US$ 2.016.458.904.40**

## 6- Conclusions
O plano desse projeto era de gerar descobertas (insights) utilizando ferramentas de visualização e de cálculos, sendo assim, foi possível resolver os problemas e ajudar o time de negócios em suas decisões podendo melhorar suas aquisições no ramo do mercado imobiliário.

## 7- Next Steps to Improve
* Adicionar filtros na aplicação web.
* Fazer uma análise de dados mais robusta.
