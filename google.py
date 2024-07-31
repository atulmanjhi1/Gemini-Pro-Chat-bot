import streamlit as st
import google.generativeai as gpt

# Configure the generative model
gpt.configure(api_key='AIzaSyC21pVS8cmOG-HA3_QzVhDKQW87ehxMDTs')
geminipro = gpt.GenerativeModel('gemini-pro')

# Define function to generate response
def generate_response(prompt, category):
    if prompt:
        full_prompt = f"Provide the {category} of the following:\n\n{prompt}"
        response = geminipro.generate_content(full_prompt)
        return response.text
    else:
        return "Please enter a prompt."

# Streamlit interface
def main():
    st.title("Quickchat")
    
    category = st.selectbox("Select the type of information you need", ["definition", "mean", "type", "Instraction", "basic information","Notes"])
    prompt = st.text_input("Ask me a Question")
    
    if st.button("Run"):
        generated_response = generate_response(prompt, category)
        st.text("Answer to your question:")
        st.write(generated_response)

if __name__ == "__main__":
    main()
