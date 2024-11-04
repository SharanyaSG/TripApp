import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os

#import streamlit as st
#from openai import OpenAI 
#import os 

# ADDED LIBRARIES
#from langchain.chat_models import ChatOpenAI
#from langchain.chains import LLMChain, RoutingChain
#from langchain.prompts import PromptTemplate

#MY API
#api_key = st.secrets["OpenAIkey"] #My API key is giving me a lot of errors so I used the option to ask users for their API instead
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
   st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:
  # Create an OpenAI client.
   client = OpenAI(api_key=openai_api_key)

#response = client.chat.completions.create(model="gpt-4o-mini", temperature = 0.8, 
  #messages=[
  #  {"role": "system", "content": "Complete the following prefix"},
   # {"role": "user", "content": prompt}
#  ],
#)
### Display
#st.write(
    #response.choices[0].message.content
#)
        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
       # with st.chat_message("assistant"):
           # response = st.write_stream(stream)
       # st.session_state.messages.append({"role": "assistant", "content": response})

## ANSWER 1 - USER INPUT: 
st.title(" TRAVEL REVIEW APP")
st.header("Share with us your experience of the latest trip")
prompt = st.text_input("Enter your feedback here please:", "My trip was")

##ANSWER 2 - Handling Negative Experiences Caused by the Airline
airlinefault = PromptTemplate.from_template("The airline was responsible for the user's negative experince and hence, the response would be that customer care will reach out to you to resolve your issue")
negative1_airline_fault = LLMChain(llm=chat, prompt=airlinefault)

## ANSWER 3 - Handling Negative Experiences NOT Caused by the Airline
notairlinefault = PromptTemplate.from_template("The airline was not responsible for the user's negative experince and hence, the response would be that we cannot help you as this was not the airline's fault")
negative2_airline_fault = LLMChain(llm=chat, prompt=airlinefault)
                                          
## ANSWER 4 - Handling Negative Experiences NOT Caused by the Airline
notairlinefault = PromptTemplate.from_template("The user had a positive experience and hence, the response would be thanking the user for their feedback and hoping that they travel with the airline again")
positive_airline_fault = LLMChain(llm=chat, prompt=airlinefault)

