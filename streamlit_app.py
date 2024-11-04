
import streamlit as st
from openai import OpenAI 
#from langchain.chat_models import ChatOpenAI
import os 

# ADDED LIBRARIES
#from langchain.chains import LLMChain, RoutingChain
#from langchain.prompts import PromptTemplate

#MY API
#api_key = st.secrets["OpenAIkey"] #My API key is giving me errors so I used the option to ask users for their API insteaf
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
   st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:
  # Create an OpenAI client.
   client = OpenAI(api_key=openai_api_key)

# Generate a response using the OpenAI API
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini", temperature = 0.8,
  #messages=[
    #{"role": "system", "content": "Complete the following prefix"},
   # {"role": "user", "content": prompt}
  #],
)
### Display
#st.write(
    #response.choices[0].message.content
)

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
       # with st.chat_message("assistant"):
           # response = st.write_stream(stream)
       # st.session_state.messages.append({"role": "assistant", "content": response})

## ANSWER 1 - USER INPUT: 
st.title(" TRAVEL REVIEW APP")
st.header("Share with us your experience of the latest trip")
prompt = st.text_input("Enter your feedback here please:", "My trip was")

# Classifying Feedback - 
#feedback_classification = ""Analyze the review shared by the client and classify it as a 
                            #1)negative expierince caused by the airline, 
                            #2)negative expierince that was beyond the airline's control, or 
                            #3)positive experience Feedback : {feedback} ""




## ANSWER 2 - Handling Negative Experiences Caused by the Airline

    #Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
   #if "messages" not in st.session_state:
    # st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    #for message in st.session_state.messages:
        #with st.chat_message(message["role"]):
           # st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
   # if prompt := st.chat_input("What is up?"):

        # Store and display the current prompt.
       # st.session_state.messages.append({"role": "user", "content": prompt})
       # with st.chat_message("user"):
          #  st.markdown(prompt)

    
