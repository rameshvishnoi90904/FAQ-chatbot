# E-commerce FAQ Chatbot

This project is a Streamlit application that functions as an FAQ chatbot for an e-commerce platform. It uses a Large Language Model to answer user queries based on a provided CSV file of frequently asked questions.

## Features

-   **FAQ Chatbot**: Answers user questions based on the data in `resources/faq_data.csv`.
-   **Data Ingestion**: Uses `chromadb` to store and retrieve FAQ data.
-   **LLM Integration**: Leverages the Groq API with the `llama-3.3-70b-versatile` model to generate answers.

## Environment Variables

This project requires a Groq API key. To set up your environment variables, create a `.env` file in the root of the project and add the following:

```
GROQ_API_KEY="your_groq_api_key"
GROK_MODEL=llama-3.3-70b-versatile
```

Replace `"your_groq_api_key"` with your actual Groq API key.

## Dependencies

The required Python packages are listed in the `requirements.txt` file.

-   **streamlit**: For creating the web application interface.
-   **pandas**: For data manipulation and reading the CSV file.
-   **groq**: The official Python client for the Groq API.
-   **python-dotenv**: For managing environment variables.
-   **chromadb**: For embedding storage and retrieval.
-   **sentence-transformers**: For generating sentence embeddings.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## How to Run

1.  **Ingest Data**: Before running the application for the first time, you need to ingest the FAQ data into the ChromaDB vector store. You can do this by running the `faq.py` script directly:

    ```bash
    python faq.py
    ```

2.  **Run the Application**: To run the Streamlit application, execute the following command in your terminal:

    ```bash
    streamlit run app.py
    ```

## Demo

<a href="#" target="_blank">Link to Live Demo</a>

### Screenshot

![Screenshot of the application](placeholder.png)
