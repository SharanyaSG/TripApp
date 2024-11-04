import streamlit as st
from openai import OpenAI 
import os 

# ADDED LIBRARIES - these keep giving  me errors
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

##ANSWER 2 - Handling Negative Experiences Caused by the Airline
airlinefault = PromptTemplate.from_template("The airline was responsible for the user's negative experince and hence, the response would be that customer care will reach out to you to resolve your issue")
negativereview1_airline_fault = LLMChain(llm=chat, prompt=airlinefault)

## ANSWER 3 - Handling Negative Experiences NOT Caused by the Airline
notairlinefault = PromptTemplate.from_template("The airline was not responsible for the user's negative experince and hence, the response would be that we cannot help you as this was not the airline's fault")
negativereview2_not_airline_fault = LLMChain(llm=chat, prompt=airlinefault)
                                          
## ANSWER 4 - Handling Negative Experiences NOT Caused by the Airline
notairlinefault = PromptTemplate.from_template("The user had a positive experience and hence, the response would be thanking the user for their feedback and hoping that they travel with the airline again")
positive_airline_review = LLMChain(llm=chat, prompt=airlinefault)

## ROUTING CODE TO TEMPLATE ANSWERS ABOVE
def review_chain(reviews):
    if "bad" in reviews or "lost luggage" in reviews or "rude staff" in reviews or "bad food" in reviews:
        return negativereview1_airline_fault
    elif "turbulance" in user_input or "bad weather" in user_input:
        return negativereview2_not_airline_fault
    elif "great" in user_input or "good" in user_input or "happy" in user_input:
        return positive_airline_review
    else:
        return None
       
#USER INTERFACE DETAILS
reviews = st.text_input("Enter your feedback here please:", "My trip was")
if st.button("SUBMIT REVIEW"):
    routing_code = review_chain(reviews)
   
    if routing_code:
        userreview = routing_code.run(reviews=reviews)
        st.write("USER REVIEW :", userreview)
    else:
        st.write("Thank you for your review. We take your review seriously, Please fly with us again! ")

