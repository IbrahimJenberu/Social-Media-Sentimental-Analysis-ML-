import streamlit as st
import pandas as pd
import sqlite3
import time
import pickle

conn = sqlite3.connect('data.db')
c = conn.cursor()


def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable (username TEXT , password TEXT)')


def add_userdata(username, password):
    c.execute('INSERT INTO usertable(username,password) VALUES(?,?)', (username, password))
    conn.commit()


def login_user(username, password):
    c.execute('SELECT * FROM usertable WHERE username = ? AND password = ?', (username, password))
    data = c.fetchall()
    return data


def view_all_user():
    c.execute("SELECT * FROM usertable")
    data = c.fetchall()
    return data


def main():
    st.title("Social media App")
    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type="password")
        create_usertable()
        if st.sidebar.button("Login"):
            result = login_user(username, password)
            if result:
                st.success("Logged In as {}".format(username))

                # Input field for user to enter a tweet
                model = pickle.load(open('sentiment_model.pkl', 'rb'))

                st.title('Social media Sentiment Analysis')

                tweet = st.text_input('Enter your tweet')

                submit = st.button('Predict')

                if submit:
                    start = time.time()
                    prediction = model.predict([tweet])
                    end = time.time()
                    st.write('Prediction time taken: ', round(end - start, 2), 'seconds')
                    if prediction[0] == "Positive":
                        st.image("positive.jpg",caption="Positive",use_column_width=False, width = 150)
                        
                        st.write(prediction[0])
                    elif prediction[0] == "Negative":
                        st.image("negative.jpg",caption="Negative",use_column_width=False, width = 150)
                        
                        st.write(prediction[0])
                    elif prediction[0] == "Neutral":
                        st.image("neutral.jpg",caption="Neutral",use_column_width=False, width = 150)
                        st.write(prediction[0])
                    else:
                        st.image("irrelevant.jpg",caption="Irrelevant",use_column_width=False, width = 150)
                        
                        st.write(prediction[0])
            else:
                st.warning("Incorrect Username or Password")

    elif choice == "SignUp":
            st.subheader("Create New Account")
            new_user = st.text_input("User Name")
            new_password = st.text_input("Password", type='password')

            if st.button("SignUp"):
                create_usertable()
                add_userdata(new_user, new_password)
                st.success("you have successfully created a valid account")
                st.info("Go to Logon Menu To Login")
main()
