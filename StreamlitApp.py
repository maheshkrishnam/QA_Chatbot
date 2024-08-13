import streamlit as st
from QAWithData.data_ingestion import load_data
from QAWithData.embeddings import download_gemini_embedding
from QAWithData.model_api import load_model

headers = {
    "authorization": st.secrets["GEMINI_API_KEY"],
    "content-type": "application/json"
}

def main():
    st.set_page_config(page_title="QA with Custom Data", page_icon=":book:", layout="wide")
    st.markdown("""
        <style>
        h1 {
            font-size: 50px !important;
        }
        h2 {
            font-size: 40px !important;
        }
        h3 {
            font-size: 30px !important;
        }
        p, li {
            font-size: 20px !important;
        }
        .big-font {
            font-size: 22px !important;
        }
        .stButton>button {
            font-size: 20px !important;
        }
        .stTextInput>div>div>input {
            font-size: 20px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "About", "Help", "Contact Us"])

    # Home Page
    if selection == "Home":
        st.title("QA with Custom Data")
        st.subheader("Empowering your data with intelligent answers")

        st.markdown('<p class="big-font">Upload your dataset and ask questions directly from it!</p>', unsafe_allow_html=True)

        # Data Upload Section
        st.markdown("### Step 1: Upload Your Data")
        doc = st.file_uploader("Choose a file", type=['csv', 'xlsx', 'txt'])
        
        if doc:
            st.success("File uploaded successfully!")

        # Question Section
        st.markdown("### Step 2: Ask Your Question")
        user_question = st.text_input("What would you like to know from your data?")

        if st.button("Submit & Process"):
            if doc and user_question:
                with st.spinner("Processing your request..."):
                    progress_bar = st.progress(0)
                    document = load_data(doc)
                    model = load_model()
                    query_engine = download_gemini_embedding(model, document)
                    
                    progress_bar.progress(25) 

                    response = query_engine.query(user_question)
                    progress_bar.progress(50)
                    
                    st.success("Here's what we found:")
                    st.write(f"You asked: **{user_question}**")
                    st.write(response.response)
                    progress_bar.progress(75)

                    progress_bar.progress(100)

            else:
                st.error("Please upload a file and enter a question.")
    
    # About Page
    elif selection == "About":
        st.title("About QA with Custom Data")
        st.markdown("""
        This application allows you to upload your own datasets and query them in real-time using advanced machine learning models. 
        Whether you're analyzing business data or conducting research, this tool provides quick insights directly from your data.
        """)
        
    # Help Page
    elif selection == "Help":
        st.title("Help & Support")
        st.markdown("""
        **How to Use the App:**
        1. Upload a CSV, Excel, or text file.
        2. Enter a question that you want to ask about the data.
        3. Click 'Submit & Process' to get your answer.

        **FAQs:**
        - **What file formats are supported?** CSV, Excel, and text files.
        - **Why is my file not uploading?** Ensure the file format is supported and the file is not too large.

        For more assistance, please contact our support team.
        """)
        
    
    elif selection == "Contact Us":
        st.title("Contact Us")
        st.write("For any queries or support, reach out to us at:")
        st.markdown("[220120011@iitdh.ac.in](220120011@iitdh.ac.in)")
        st.write("Follow us on social media for updates and more:")
        st.markdown("[Instagram](https://www.instagram.com/krishnam_mahesh/) | [LinkedIn](https://www.linkedin.com/in/mahesh-krishnam-a8a0b422b/)")

if __name__ == "__main__":
    main()
