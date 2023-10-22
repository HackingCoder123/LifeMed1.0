import streamlit as st

import streamlit as st
from PIL import Image



st.title('Education About Diabetes')
st.header('Symptoms')
image = Image.open('diabetes.jpg')
st.image(image, caption='Symptoms')
st.header('What is Diabetes')
st.info('Diabetes is a chronic medical condition characterized by elevated blood sugar levels. It comes in two main types, Type 1 and Type 2. Type 1 diabetes is an autoimmune disease that typically develops in childhood, where the bodys immune system attacks and destroys insulin-producing cells in the pancreas. Type 2 diabetes is often associated with lifestyle factors like poor diet and lack of exercise, leading to insulin resistance. Both types can result in serious health complications if not properly managed.')
st.header('Types of Diabetes')
st.info('In Type 1 diabetes, the immune system mistakenly attacks and destroys the insulin-producing cells in the pancreas, leading to an absolute insulin deficiency. People with Type 1 diabetes need to take insulin injections or use insulin pumps to replace the missing hormone. On the other hand, Type 2 diabetes often develops due to a combination of genetic factors and poor lifestyle choices, such as an unhealthy diet and insufficient physical activity. In this case, the body becomes less responsive to the insulin it produces, which results in elevated blood sugar levels. Managing Type 2 diabetes typically involves dietary modifications, increased exercise, oral medications, and sometimes insulin therapy, all aimed at helping the body better utilize the insulin available. Proper management of diabetes is essential for preventing complications and maintaining a good quality of life.')