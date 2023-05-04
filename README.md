
# VirtualBrainGPT: Digital Journal 📝

VirtualBrainGPT is a digital journal application that leverages the power of OpenAI's Embeddings API and Langchain to create a seamless and efficient journaling experience. With the capability to search and extract information from journal entries in seconds, VirtualBrainGPT becomes an indispensable tool for users who want to recall specific details from their past entries.

# Web App
Click [Here](https://huggingface.co/spaces/Kaludi/VirtualBrainGPT "Here") To View This Application Online!

![virtualbrain1](https://user-images.githubusercontent.com/63890666/236136026-c6f1a3f9-4e58-4ddf-a5a7-c349395b67af.png)
![virtualbrain2](https://user-images.githubusercontent.com/63890666/236136020-bb10c286-deac-436c-99cc-67b6a86f5672.png)
![virtualbrain3](https://user-images.githubusercontent.com/63890666/236136028-65f4f874-9076-4e4f-9887-cbc1a2e6fd20.png)

## Features

-   Create and manage journal entries using a clean interface.
-   Search and extract information from journal entries quickly and accurately.
-   Support for both TXT and PDF file formats.
-   Powered by OpenAI's Embeddings API and Langchain for efficient information retrieval.

## Usage

### Brain Entry

In the 'Brain Entry' section, users can create a new journal entry or edit an existing one by choosing a date using the date picker. Once you have completed your entry, click 'Submit' and it will be saved or updated to the brain_journal.txt file in the brain folder.

### Brain Search

The 'Brain Search' section of the application unlocks the full potential of your digital journal. Here, you can ask any questions related to your journal entries, and the combination of OpenAI's Embeddings API and Langchain will provide accurate responses in seconds, no matter how long the entry or document may be. The virtual brain can help in all aspects of a user's life, enabling users to easily recall specific information, even if they can't remember it themselves. Users also have an option to select other file types if they wish to upload their own file, the current file types include TXT and PDF files, which can be selected in the file type dropdown option.

## Examples of Use-Cases

This application can be used in many ways. Imagine five years from now, you're trying to recollect a specific event that you documented in your journal, or you may have kept a journal from your childhood. VirtualBrainGPT will locate the exact date and provide you with a detailed account of that exact situation in a matter of seconds, as well as any other memories that you may have forgotten about. This type of  application also could offer invaluable support for individuals with Alzheimer's, helping them retrieve memories from the past that may have been lost and share them with their loved ones.

## Tools & Libraries Used

### Tools
-   OpenAI [Embeddings](https://platform.openai.com/docs/guides/embeddings)
-   [LangChain](https://python.langchain.com/en/latest/use_cases/question_answering.html)
-   [Streamlit](https://streamlit.io/)

### Libraries
-   Streamlit
-   OpenAI
-   PyPDF2
-   LangChain
-   python-dotenv
-   tiktoken
-   faiss-cpu

## Installation

To install VirtualBrainGPT, you need to have Python 3.7+ installed. Follow these steps to install the necessary dependencies:

1.  Clone this repository:

`git clone https://github.com/Kaludii/VirtualBrainGPT.git` 

2.  Change directory to the cloned repository:

`cd VirtualBrainGPT` 

3.  Install the required packages:

`pip install -r requirements.txt` 

4.  Run the Streamlit application:

`streamlit run VirtualBrainGPT.py` 

## About the Developer

This application was developed by [Kaludii](https://github.com/Kaludii)  using the the different tools and libraries linked above. Kaludii is an AI enthusiast who is passionate about developing and applying large learning models to solve real-world problems quickly and stress-free.

## Contributions

If you have any suggestions or improvements for this project, feel free to open an issue or submit a pull request. Your contributions are always welcome!
