import os
import datetime
import streamlit as st

st.set_page_config(
    page_title="VirtualBrainGPT",
    page_icon="📝",
)
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.write("# VirtualBrainGPT: Digital Journal 📝")

st.sidebar.success("Select either the Brain Entry or Brain Search from above.")

st.markdown(
    """
    This application uses the Streamlit interface to take journaling to a whole new level.
    Welcome to VirtualBrainGPT, an application that streamlines the process of creating and managing personal journal entries. By leveraging the power of OpenAI's Embeddings and Langchain, this application not only simplifies journaling but also offers a new way to effortly and immediately search between multiple different journal entries, no matter how many or how long they may be.
    
    To begin, simply select either **'Brain Entry'** or **'Brain Search'** from the **sidebar menu**! 👈
    
    ### Brain Entry
    In the 'Brain Entry' section, users can create a new journal entry or edit an existing one by choosing a date using the date picker. Once you have completed your entry, click 'Submit' and it will be saved or updated to the brain_journal.txt file in the brain folder.

    ### Brain Search
    The 'Brain Search' section of the application unlocks the full potential of your digital journal. Here, you can ask any questions related to your journal entries, and the combination of OpenAI's Embeddings and Langchain will provide accurate responses in seconds, no matter how long the entry or document may be. The virtual brain can help in all aspects of a user's life, enabling users to easily recall specific information, even if they can't remember it themselves. Users also have an option to select other file types if they wish to upload their own file, the current file types include TXT and PDF files, which can be selected in the file type dropdown option. Along with the response, you will also get information about the amount of tokens that were used and the Total Cost of the query.
    
    ### Tools Used
    - OpenAI [Embeddings](https://platform.openai.com/docs/guides/embeddings)
    - [LangChain](https://python.langchain.com/en/latest/use_cases/question_answering.html)
    - [Streamlit](https://streamlit.io/)

    ### Application Info
    
    - **GitHub Application & Documentation:** [https://github.com/Kaludii/VirtualBrainGPT](https://github.com/Kaludii/VirtualBrainGPT)
    
    - **Web Application:** [https://huggingface.co/spaces/Kaludi/VirtualBrainGPT](https://huggingface.co/spaces/Kaludi/VirtualBrainGPT)
    
    ### About the Developer
    This application was developed by [Kaludii](https://github.com/Kaludii)  using the the different tools and libraries linked above. Kaludii is an AI enthusiast who is passionate about developing and applying large learning models to solve real-world problems quickly and stress-free.
    
"""
)

st.markdown("---")
st.markdown("")
st.markdown("<p style='text-align: center'><a href='https://github.com/Kaludii'>Github</a> | <a href='https://huggingface.co/Kaludi'>HuggingFace</a></p>", unsafe_allow_html=True)
