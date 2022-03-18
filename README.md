# st-write

`st.write` is a versatile Swiss Army knife of Streamlit commands that can display text, plots, etc. depending on the input argument given to it.

In addition to `st.write` there are several ways to display text in a Streamlit app:
- `st.write`
- `st.header`
- `st.subheader`
- `st.markdown`

## Demo app
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st-write/)

## Code
Contents of the `streamlit_app.py` file:
```python
import streamlit as st
import pandas as pd

st.title('This is using st.title')
st.header('This is using st.header')
st.subheader('This is using st.subheader')
st.write('This is using st.write')
st.markdown("This is using st.markdown, which can leverage markdown's functionality, e.g. *bold*, **italic**, ***bold and italic***, `highlights`, etc.")
st.markdown('''
Text can also be entered on multiple lines by encapsulating via three opening and closing quotes.
Code snippets can also be displayed like so:
```python
import streamlit as st
st.write('Hello world!')
```
''')


x = 'This text is from a variable and displayed in Streamlit via the built-in magic by simply calling the variable.'
x


st.header('Displaying a DataFrame')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv')
df
```

## References
Read in the Streamlit API Documentation about:
- [`st.write`](https://docs.streamlit.io/library/api-reference/text/st.write)
- [`st.header`](https://docs.streamlit.io/library/api-reference/text/st.header)
- [`st.subheader`](https://docs.streamlit.io/library/api-reference/text/st.subheader)
- [`st.markdown`](https://docs.streamlit.io/library/api-reference/text/st.markdown)
