# chatbot-project

# AI-Powered Chatbot with Arxiv and Wikipedia

This project is a web-based chatbot application that integrates language models and real-time data retrieval from Arxiv and Wikipedia.

## Features
- **AI-Powered Responses**: The chatbot uses large language models (LLMs) to generate intelligent responses.
- **Real-Time Knowledge Retrieval**: The bot can query Arxiv and Wikipedia to fetch relevant research papers and general information.
- **Web Interface**: The application is served via Streamlit, making it easy to interact with the chatbot in a web browser.

## Tech Stack
- **Streamlit**: For the web interface.
- **Langgraph**: To manage the chatbot's state machine.
- **Langchain**: To integrate the LLM and tools.
- **Groq API**: Large language model used for generating responses.
- **Arxiv & Wikipedia APIs**: Used for fetching real-time data.

## Setup Instructions

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/chatbot-project.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit server:
    ```bash
    streamlit run app.py
    ```

4. Open the provided URL in your browser to interact with the chatbot!

## License
This project is open-source and available under the [MIT License](LICENSE).

4. Optional: Create .gitignore
You can use a .gitignore file to exclude unnecessary files from Git. Here’s a sample .gitignore:

markdown
Copy code
__pycache__/
*.pyc
*.pyo
*.pyd
.env
.DS_Store
5. Push to GitHub
Now that you have all the necessary files, follow these steps to upload the project to GitHub:

Initialize Git in your project folder:

bash
Copy code
git init
Add all files to the repository:

bash
Copy code
git add .
Commit the changes:

bash
Copy code
git commit -m "Initial commit with chatbot project"
Create a new repository on GitHub (you can do this from GitHub's web interface).

Link your local repository to GitHub:

bash
Copy code
git remote add origin https://github.com/your-username/chatbot-project.git
Push the files to GitHub:

bash
Copy code
git push -u origin main
Once you follow these steps, your project will be uploaded to GitHub and available for others to see and contribute.
