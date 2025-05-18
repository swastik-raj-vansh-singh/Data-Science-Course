# import streamlit as st
# import numpy as np 
# import pandas as pd

# # Title of the application
# st.title("my nams is swastik")

# # Display the simple text
# st.write("i am 22 year old")

# # Creating a simple data frame
# df = pd.DataFrame({
#     'first_col' : [1,2,3,4],
#     'second_col' : [5,6,7,8]
# })
# # display the data frame
# st.write(df)

# # Creating the Line chart
# line_chart_data = pd.DataFrame(
#     np.random.rand(20,3), columns= ['a','b','c']
# )

# st.line_chart(line_chart_data) 

# # some more components

# # here i show you the text input 
# name = st.text_input("Enter your name")
# if name:
#     st.write(f"Hello {name}")


# # Creating slider 
# age = st.slider("Enter how old are you",0,100,25)
# st.write(f"Ok so your age is {age}")


# # creating select box
# options =['java','c++','python']
# choice = st.selectbox("what language you know well ?", options)
# st.write(choice)

# # Creating a file uploader
# upload_file= st.file_uploader("Choose your csv file",type="csv",accept_multiple_files=True)
# if upload_file is not None:
#     df = pd.read_csv(upload_file)
#     st.write(df)


# lets try something more cool
import streamlit as st
import wikipedia

from streamlit_searchbox import st_searchbox


def search_wikipedia(searchterm: str) -> list:
    # search wikipedia for the searchterm
    return wikipedia.search(searchterm) if searchterm else []


# pass search function and other options as needed
selected_value = st_searchbox(
    search_wikipedia,
    placeholder="Search Wikipedia... ",
    key="my_key",
)

st.write(f"Selected value: {selected_value}")