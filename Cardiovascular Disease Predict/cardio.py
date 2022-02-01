import streamlit as st
import numpy as np
import pickle


def get_model(path):
    model = pickle.load(open(path, 'rb'))

    return model


def predict_m(model, age_days, gender_n, hei, wei, sys_p, dis_p, ch_n, gl_n, smok_n, alco_n, prat_n):
    input = np.array([[age_days, gender_n, hei, wei, sys_p,
                       dis_p, ch_n, gl_n, smok_n, alco_n, prat_n]]).astype(np.float64)
    prediction = model.predict_proba(input)
    pred = '{0:.{1}f}'.format(prediction[0][1], 1)

    return float(pred)


def values(model):
    st.header('Cardiovascular Disease')
    st.write("This app predicts the probability of cardiovascular diseases based on some information from the user.")

    age = st.text_input('AGE', max_chars=3)
    if len(age) > 0:
        age_days = int(age)
        age_days = age_days * 365
    else:
        age_days = 0

    gender = st.radio("GENDER", ('Female', 'Male'))
    if gender == 'Female':
        gender_n = 1
    else:
        gender_n = 2

    hei = st.text_input('HEIGHT', max_chars=3, placeholder='cm')
    if len(hei) > 0:
        hei_n = int(hei)
    else:
        hei_n = 0

    wei = st.text_input('WEIGHT', max_chars=3, placeholder='kg')
    if len(wei) > 0:
        wei_n = int(wei)
    else:
        wei_n = 0

    st.caption("PS: pressure 130/85 it's ideal")

    sys_p = st.slider('SYSTOLIC BLOOD PRESSURE', 50, 300, 130)

    dis_p = st.slider('DIASTOLIC BLOOD PRESSURE', 40, 200, 85)

    ch = st.selectbox(
        'CHOLESTEROL', ('Normal', 'Above Normal', 'Well Above Normal'))
    if ch == 'Normal':
        ch_n = 1

    elif ch == 'Above Normal':
        ch_n = 2

    else:
        ch_n = 3

    gl = st.selectbox(
        'GLUCOSE', ('Normal', 'Above Normal', 'Well Above Normal'))
    if gl == 'Normal':
        gl_n = 1

    elif gl == 'Above Normal':
        gl_n = 2

    else:
        gl_n = 3

    smok = st.selectbox(
        'DO YOU SMOKE CIGARETTES?', ('No', 'Yes'))
    if smok == 'No':
        smok_n = 0

    else:
        smok_n = 1

    alco = st.selectbox('DO YOU DRINK ALCOHOL?', ('No', 'Yes'))
    if alco == 'No':
        alco_n = 0
    else:
        alco_n = 1

    prat = st.selectbox('DO YOU PRACTICE PHYSICAL ACTIVITY?', ('No', 'Yes'))
    if prat == 'No':
        prat_n = 0
    else:
        prat_n = 1

    if st.button('Predict'):
        if (wei_n == 0):
            st.error('No value in WEIGHT')
        if (age_days == 0):
            st.error('No value in AGE')
        if (hei_n == 0):
            st.error('No value in HEIGHT')

        if (age_days > 0) & (wei_n > 0) & (hei_n > 0):
            alt = hei_n / 100
            bmi = round(wei_n / (alt * alt), 1)
            output = predict_m(model, age_days, gender_n, hei_n, wei_n, sys_p,
                               dis_p, ch_n, gl_n, smok_n, alco_n, prat_n)

            bmi_result = bmi_calcu(bmi)

            st.success(
                'The probability of cardiovascular disease is {0}% and your BMI is {1} ( {2} )'.format(output * 100, bmi, bmi_result))

    return None


def bmi_calcu(bmi):
    if (bmi < 18.5):
        msg = 'Underweight'
    elif (bmi >= 18.5) & (bmi <= 24.9):
        msg = 'Normal weight'
    elif (bmi >= 25) & (bmi <= 29):
        msg = 'Overweight'
    else:
        msg = 'Obesity'

    return msg


if __name__ == '__main__':
    path = 'model_k.pkl'

    model = get_model(path)

    values(model)
