import streamlit as st

st.header('This is using st.header')
st.subheader('This is using st.subheader')
st.write('This is using st.write')
st.markdown("This is using st.markdown, which can leverage markdown's functionality, e.g. *bold*, **italic**, ***bold and italic***, `highlights`, etc.")

x = 'This text is from a variable and displayed in Streamlit via the built-in magic by simply calling the variable.'
x
