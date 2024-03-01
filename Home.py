import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.header("The Best Company")
about_company = """
                A company is a legal entity formed by a group of individuals to engage in 
and operate a business—commercial or industrial—enterprise. A company may be organized in 
various ways for tax and financial liability purposes depending on the corporate law of 
its jurisdiction.
"""
st.write(about_company)

st.subheader("Our Team")

df = pandas.read_csv("data.csv")

col1, wt_space1, col2, wt_space2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

for index, title in df[:4].iterrows():
    with col1:
        name = f'{title["first name"]} {title["last name"]}'.title()
        st.subheader(name)
        st.write(title["role"])
        st.image("images/" + title["image"])


for index, title in df[4:8].iterrows():
    with col2:
        name = f'{title["first name"]} {title["last name"]}'.title()
        st.subheader(name)
        st.write(title["role"])
        st.image("images/" + title["image"])

for index, title in df[8:12].iterrows():
    with col3:
        name = f'{title["first name"]} {title["last name"]}'.title()
        st.subheader(name)
        st.write(title["role"])
        st.image("images/" + title["image"])
