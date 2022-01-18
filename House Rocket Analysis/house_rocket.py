import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')


@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    data['date'] = pd.to_datetime(data['date'])

    return data


def create_feature(data):
    data['year'] = data['date'].dt.year
    data['month_year'] = data['date'].dt.strftime('%Y-%m')

    data['season'] = 'NA'

    for i in range(len(data)):
        if (data.loc[i, 'month_year'] == '2014-03') | (data.loc[i, 'month_year'] == '2014-04') | (data.loc[i, 'month_year'] == '2014-05'):
            data.loc[i, 'season'] = 'spring'

        elif (data.loc[i, 'month_year'] == '2014-06') | (data.loc[i, 'month_year'] == '2014-07') | (data.loc[i, 'month_year'] == '2014-08'):
            data.loc[i, 'season'] = 'summer'

        elif (data.loc[i, 'month_year'] == '2014-09') | (data.loc[i, 'month_year'] == '2014-10') | (data.loc[i, 'month_year'] == '2014-11'):
            data.loc[i, 'season'] = 'fall'

        elif (data.loc[i, 'month_year'] == '2014-12') | (data.loc[i, 'month_year'] == '2015-01') | (data.loc[i, 'month_year'] == '2015-02'):
            data.loc[i, 'season'] = 'winter'

        else:
            data.loc[i, 'season'] = 'spring'

    return data


def reports(data):
    st.header('Data Overview')
    st.dataframe(data)

    c1, c2 = st.columns((1, 1))

    df1 = data[['zipcode', 'price']].groupby('zipcode').median().reset_index()
    df2 = data[['id', 'zipcode', 'condition', 'price']]
    df3 = pd.merge(df1, df2, on='zipcode', how='inner')

    df3.columns = ['zipcode', 'price_median', 'id', 'condition_house', 'price']
    report = df3[['id', 'zipcode', 'condition_house',
                  'price', 'price_median']].sort_values('zipcode')

    report['buy'] = 'NA'

    for i in range(len(report)):
        if (report.loc[i, 'condition_house'] >= 3) & (report.loc[i, 'price'] <= report.loc[i, 'price_median']):
            report.loc[i, 'buy'] = 'YES'
        else:
            report.loc[i, 'buy'] = 'no'

    report.columns = ['ID HOUSES', 'ZIPCODE',
                      'CONDITION HOUSE', 'PRICE', 'PRICE MEDIAN', 'BUY?']

    c1.header('Home Purchase Report')
    c1.dataframe(report, height=600)

    df1 = data[['id', 'price', 'zipcode', 'season']]
    df2 = data[['zipcode', 'price', 'season']].groupby(
        ['zipcode', 'season']).median().reset_index()

    df3 = pd.merge(df1, df2, on=['zipcode', 'season'], how='inner')

    df3.columns = ['id', 'price', 'zipcode', 'season', 'price_median']
    report_sell = df3[['id', 'zipcode', 'season',
                       'price', 'price_median']].sort_values('zipcode')

    report_sell['sales_price'] = 'NA'

    for i in range(len(report_sell)):
        if (report_sell.loc[i, 'price'] > report_sell.loc[i, 'price_median']):
            report_sell.loc[i,
                            'sales_price'] = report_sell.loc[i, 'price'] * 1.1
        else:
            report_sell.loc[i,
                            'sales_price'] = report_sell.loc[i, 'price'] * 1.3

    report_sell.columns = ['ID HOUSES', 'ZIPCODE',
                           'SEASON', 'PRICE', 'PRICE MEDIAN', 'SALES PRICE']

    c2.header('Home Sales Report')
    c2.dataframe(report_sell, height=600)

    return None


def make_barplot(data, x, y):
    fig = px.bar(data, x=x, y=y)
    st.plotly_chart(fig, use_container_width=True)

    return None


def hyphotesis(data):

    st.header(
        'Hyphotesis #1: Imóveis que possuem vista para água são 30% mais caros, na média.')
    st.subheader(
        'TRUE: Imóveis com vista para a água são 213% mais caros, na média.')
    hypo1 = data[['waterfront', 'price']].groupby(
        'waterfront').mean().reset_index()
    hypo1 = data[['waterfront', 'price']].groupby(
        'waterfront').mean().reset_index()

    make_barplot(hypo1, 'waterfront', 'price')

    st.header(
        'Hyphotesis #2: Imóveis com data de construção menor que 1955, são 50% mais baratos, na média.')
    st.subheader(
        'FALSE: Imóveis com data de construção menor que 1995 são 2% mais baratos, na média.')

    hypo2 = data[['price', 'yr_built']].copy()

    hypo2['status'] = 'NA'

    for i in range(len(hypo2)):
        if (hypo2.loc[i, 'yr_built'] <= 1955):
            hypo2.loc[i, 'status'] = 'old'
        else:
            hypo2.loc[i, 'status'] = 'new'

    hypo2.drop(['yr_built'], axis=1, inplace=True)
    hypo2 = hypo2.groupby('status')['price'].mean().reset_index()

    make_barplot(hypo2, 'status', 'price')

    st.header('Hyphotesis #3: Imóveis sem porão possuem área total (sqrt_lot), são 40% maiores do que os imóveis com porão, na média.')
    st.subheader(
        'FALSE: Imóveis sem porão são 23% maiores do que os imóveis com porão')

    hypo3 = data[['sqft_basement', 'sqft_lot']].copy()

    hypo3['status'] = 'NA'

    for i in range(len(hypo3)):
        if (hypo3.loc[i, 'sqft_basement'] != 0):
            hypo3.loc[i, 'status'] = 'with_basement'
        else:
            hypo3.loc[i, 'status'] = 'no_basement'

    hypo3.drop(['sqft_basement'], axis=1, inplace=True)
    hypo3 = hypo3.groupby('status')['sqft_lot'].mean().reset_index()

    make_barplot(hypo3, 'status', 'sqft_lot')

    st.header(
        'Hyphotesis #4: O crescimento do preço dos imóveis YoY (Year over Year) é de 10%.')
    st.subheader('FALSE: O crescimento é de apenas 1%.')

    hypo4 = data[['price', 'year']].copy()
    hypo4 = hypo4.groupby('year')['price'].mean().reset_index()

    make_barplot(hypo4, 'year', 'price')

    st.header(
        'Hyphotesis #5: Imóveis com 3 banheiros tem um crescimento de MoM (Month over Month) de 15%.')
    st.subheader('FALSE: O crescimento MoM não é constante igual a 15%.')

    hypo5 = data[['bathrooms', 'month_year', 'price']].copy()
    hypo5.drop(hypo5[hypo5.bathrooms != 3].index, inplace=True)
    hypo5 = hypo5.groupby('month_year')['price'].mean().reset_index()

    fig = px.line(hypo5, x='month_year', y='price')
    st.plotly_chart(fig, use_container_width=True)

    st.header(
        'Hyphotesis #6: Imóveis com mais de 3 quartos, tem a sala de estar 30% maior, na média.')
    st.subheader(
        'TRUE: Imóveis com mais de 3 quartos tem a sala de estar 82% maior.')

    hypo6 = data[['bedrooms', 'sqft_living']].copy()
    hypo6['status'] = 'NA'

    for i in range(len(hypo6)):
        if (hypo6.loc[i, 'bedrooms'] >= 3):
            hypo6.loc[i, 'status'] = 'three more bedrooms'
        else:
            hypo6.loc[i, 'status'] = 'less bedrooms'

    hypo6.drop(['bedrooms'], axis=1, inplace=True)
    hypo6 = hypo6.groupby('status')['sqft_living'].mean().reset_index()

    make_barplot(hypo6, 'status', 'sqft_living')

    st.header('Hyphotesis #7: Imóveis com construção e design de alta qualidade de 11 a 13 são 50% mais caros, na média.')
    st.subheader(
        'TRUE: Imóveis com construção e design de alta qualidade são 227% mais caros.')

    hypo7 = data[['grade', 'price']].copy()
    hypo7['status'] = 'NA'

    for i in range(len(hypo7)):
        if (hypo7.loc[i, 'grade']) <= 10:
            hypo7.loc[i, 'status'] = 'low quality'
        else:
            hypo7.loc[i, 'status'] = 'high quality'

    hypo7.drop(['grade'], axis=1, inplace=True)
    hypo7 = hypo7[['status', 'price']].groupby('status').mean().reset_index()

    make_barplot(hypo7, 'status', 'price')

    st.header(
        'Hyphotesis #8: Imóveis com o sotão com mais de 3500m² são 30% mais caros, na média.')
    st.subheader(
        'TRUE: Imóveis com o sotão com mais de 3500m² são 163% mais caros na média.')

    hypo8 = data[['sqft_above', 'price']].copy()
    hypo8['status'] = 'NA'

    for i in range(len(hypo8)):
        if (hypo8.loc[i, 'sqft_above'] < 3500):
            hypo8.loc[i, 'status'] = 'small_above'
        else:
            hypo8.loc[i, 'status'] = 'large_above'

    hypo8.drop(['sqft_above'], axis=1, inplace=True)
    hypo8 = hypo8[['status', 'price']].groupby('status').mean().reset_index()

    make_barplot(hypo8, 'status', 'price')

    st.header('Hyphotesis #9: Os preços dos imóveis são 20% mais caros na temporada de verão e primavera do que na temporada de inverno e outono, na média.')
    st.subheader(
        'FALSE: Os imóveis das temporadas de verão e primavera são 5% mais caros, na média.')

    hypo9 = data[['season', 'price']].copy()
    hypo9 = hypo9[['season', 'price']].groupby('season').mean().reset_index()

    season_mean = pd.DataFrame()
    season_mean.loc[0, 'status'] = 'fall_winter'
    season_mean.loc[1, 'status'] = 'summer_spring'

    season_mean.loc[0, 'price_mean'] = hypo9.loc[0,
                                                 'price'] + hypo9.loc[3, 'price']
    season_mean.loc[1, 'price_mean'] = hypo9.loc[1,
                                                 'price'] + hypo9.loc[2, 'price']

    make_barplot(season_mean, 'status', 'price_mean')

    st.header(
        'Hyphotesis #10: Imóveis com mais de 2 andares são 35% mais caros, na média.')
    st.subheader(
        'FALSE: Imóveis com mais de 2 andares são 28% mais caros, na média.')

    hypo10 = data[['price', 'floors']].copy()
    hypo10['status'] = 'NA'

    for i in range(len(hypo10)):
        if (hypo10.loc[i, 'floors'] < 2):
            hypo10.loc[i, 'status'] = 'little_floors'
        else:
            hypo10.loc[i, 'status'] = 'many floors'

    hypo10.drop(['floors'], axis=1, inplace=True)
    hypo10 = hypo10[['status', 'price']].groupby('status').mean().reset_index()

    make_barplot(hypo10, 'status', 'price')

    return None


if __name__ == '__main__':
    path = 'kc_house_data.csv'

    data = get_data(path)

    data = create_feature(data)

    reports(data)

    hyphotesis(data)
