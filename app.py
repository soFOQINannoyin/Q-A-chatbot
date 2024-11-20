import streamlit as st
import cohere

# Initialize the Cohere API client
COHERE_API_KEY = "UvQcnNHSF42oPDGTWv6P9OpGrOCMb9lPgKOjxj3m"  # Replace this with your actual Cohere API key
cohere_client = cohere.Client(COHERE_API_KEY)

# Function to load Cohere model and get response
def get_cohere_response(question):
    response = cohere_client.generate(
        model='command',  # You can use other models like 'medium' or 'large'
        prompt=question,
        max_tokens=100,  # Adjust based on how long you want the response to be
        temperature=0.5  # Control the creativity of the response (0.0 = deterministic, 1.0 = creative)
    )
    return response.generations[0].text.strip()

# Initialize the Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application with Cohere")

# Text input from the user
input = st.text_input("Input: ", key="input_field")

# When the user clicks the "Ask the question" button
submit = st.button("Ask the question")

if submit:
    if input:
        # Get response from Cohere API
        response = get_cohere_response(input)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please enter a question.")
