# app.py
import streamlit as st
import hashlib
import database_operations as db

st.set_page_config(page_title="Client Query System", layout="centered")

#Helper function for SHA-256 Hashing
def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

#Session State Management
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.role = None
    st.session_state.username = ""

#Login view
if not st.session_state.authenticated:
    st.title("Login")
    with st.container():
        user = st.text_input("Username")
        pw = st.text_input("Password", type="password")
        if st.button("Sign In"):
            role = db.login_user(user, hash_text(pw))
            if role:
                st.session_state.authenticated = True
                st.session_state.role = role
                st.session_state.username = user
                st.rerun()
            else:
                st.error("Invalid credentials. Please check your username/password.")

#Application
else:
    st.sidebar.success(f"User: {st.session_state.username} | Role: {st.session_state.role}")
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()

    #Client page
    if st.session_state.role == "Client":
        st.header("Submit a Query")
        with st.form("submission_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                email = st.text_input("Email ID")
                mobile = st.text_input("Mobile Number")
            with col2:
                heading = st.text_input("Query Title")
            
            description = st.text_area("Detailed Description")
            
            if st.form_submit_button("Submit"):
                if email and heading and description:
                    db.insert_query(email, mobile, heading, description)
                    st.success("Query submitted! Our support team will review it soon.")
                else:
                    st.warning("Please fill in all required fields.")

    #Support page
    elif st.session_state.role == "Support":
        st.header("Support Team Dashboard")
        df = db.fetch_all_queries()

        if not df.empty:
            # Stats Section
            total = len(df)
            open_q = len(df[df['status'] == 'Open'])
            closed_q = len(df[df['status'] == 'Closed'])
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Total Queries", total)
            c2.metric("Pending", open_q, delta_color="inverse")
            c3.metric("Resolved", closed_q)

            # Data Table
            st.subheader("Query Logs")
            st.dataframe(df, use_container_width=True)

            # Action Bar
            st.subheader("Status")
            open_list = df[df['status'] == 'Open']['query_id'].tolist()
            if open_list:
                selected_id = st.selectbox("Select Query ID to Resolve", open_list)
                if st.button("Close Query"):
                    db.mark_as_closed(selected_id)
                    st.success(f"Query #{selected_id} marked as Closed.")
                    st.rerun()
            else:
                st.info("Great job! All queries are currently resolved.")
        else:
            st.info("The query database is currently empty.")