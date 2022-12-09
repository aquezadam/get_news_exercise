import datetime
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

import news
import back
title = st.markdown('''<h1 style= "text-align:center; color:#ff4b4b;">
                    NEWS AGGREGATOR
                    </h1>''',
                    unsafe_allow_html=True)
subtitle = st.markdown('''<h4 style= "text-align:center; color:#ff4b4b;">
                    Fetch the latest 10 news articles
                    </h4>''',
                    unsafe_allow_html=True)

with st.sidebar:  # to include sidebar
    option = option_menu("User Login", ["Register", "Login"])
    #                     ("name_sidebar", [element1, element2])
if option == "Register":
    with st.expander("Expand to register", expanded=True):
        cols = st.columns([1,3,1])  # 5 colums
        name = cols[1].text_input("Enter name: ")
        email = cols[1].text_input("Enter email:")
        password = cols[1].text_input("Enter password:", type="password")
        if st.button("Register"):
            result = back.user_registration(name, email, password)
            st.success(result)

if option == "Login":
    with st.expander("Expand to login", expanded=True):
        cols = st.columns([1,3,1])  #5 colums
        email = cols[1].text_input("Enter email:")
        password = cols[1].text_input("Enter password:", type="password")
        # if cols[1].checkbox("Submit"):
        if cols[1].checkbox("Submit"):
            global result_login
            result_login = back.login(email, password)
            st.success(result_login)

# if option == "Reset Password":
#     cols = st.columns([1, 3, 1])  # 5 colums
#     email = cols[1].text_input("Enter email:")
#     new_password = cols[1].text_input("Enter new password:", type="password")
#     if cols[1].button("Reset password"):
#         result_new_password = back.change_password(email, new_password)
#         st.success("Your password changed")

try:
    if result_login == "success":
        date = st.sidebar.date_input("Please enter a date to fetch news from that day", datetime.date(2022, 12, 7))
        query = st.sidebar.text_input("Please enter a search word. Then press enter to fetch news.")
        news_articles = news.news_fetch(query, date)
        st.markdown("")
    #   st.success(news_articles)
        # df = pd.DataFrame.from_dict(news_articles, orient="columns")
        # st.table(df)
        for i in news_articles:
            title = i['title']
            description = i['description']
            link = i["url"]
            st.markdown('''
            
            ''')
            st.markdown(f"<h6 style = 'color:#ff4b4b;'>{title}</h6>", unsafe_allow_html=True)
            st.markdown(f"<p>{description}</p>", unsafe_allow_html=True)
            st.write(f"[Click here for full article]({link })")
            st.write("______")

    elif result_login == "wrong password":
        new_password = st.text_input("Enter new password:", type="password")
        if st.checkbox("Reset password"):
            result_new_password = back.change_password(email, new_password)
            st.success("Your password changed")
except:
    st.warning("Please enter correct credentials")
