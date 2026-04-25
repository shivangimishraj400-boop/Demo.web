import streamlit as st

Name=st.text_input("Enter Your Name")
Title=st.text_input("Enter your Title")
Content=st.text_area("Enter your text")
Date=st.text_input("Enter your Date")


button= st.button ("Submit")
if button: st.markdown(f"""
                        Name:{Name}
                        Title:{Title}
                        Content:{Content}
                        Date:{Date}""")
