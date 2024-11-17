# AI Frontend

Welcome to **AI Frontend**, an interface built with Gradio that provides an interactive chatbot experience. This project utilizes API-driven responses for conversational AI using an easy-to-launch frontend. The project is configurable with a set of environment variables to allow customization of the AI model being used.

## Features
- **Customizable Interface**: Tailored UI using Gradio with custom CSS for styling.
- **Configurable API Integration**: Connects with any conversational model using environmental settings for dynamic configuration.
- **Simple Deployment**: Easily launch the chatbot interface in a local or production environment.

## Prerequisites
To run the AI Frontend, you need to have the following installed:

- **Python 3.7+**
- **Gradio** (`pip install gradio`)
- **Requests** (`pip install requests`)

You will also need an API endpoint that supports OpenAI-style completions to connect to the chatbot.

## Environment Variables
The application uses the following environment variables to set up the integration:

1. **APIKEY**: The API key for authenticating with the API.
2. **BOTID**: The model ID to use for generating responses.
3. **COMPLETIONSURL**: The URL of the API endpoint for text completion.
4. **SYSTEMPROMPT**: The system prompt that sets the initial tone or guidelines for the AI model.

Set these variables in your environment to ensure the application connects correctly to your API backend.

### Example `.env` File
Below is an example of how you can set up these variables in an `.env` file:

#### Open WebUI example
``` bash
APIKEY=sk-***your_api_key_here***
BOTID=granite3-dense:2b 
COMPLETIONSURL=https://ai.your.site/api/chat/completions
SYSTEMPROMPT="You are a helpful bot."
```

#### OpenAI example
``` bash
APIKEY=sk-***your_api_key_here***
BOTID=gpt-4o-mini 
COMPLETIONSURL=https://api.openai.com/v1/chat/completions
SYSTEMPROMPT="You are a helpful bot."
```

## Running the Project
Follow these steps to run the AI Frontend:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/ai-frontend.git
    cd ai-frontend
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set environment variables** (or use an `.env` file).

4. **Run the application**:
    ```bash
    python ai-frontend.py
    ```

Once the script is executed, the application will start a local server, and you can interact with the chatbot via your browser.

## File Structure
- **main.py**: Entry point for running the application.
- **css/custom_styles.css**: Custom CSS for styling the Gradio interface.

## Notes
- Ensure that your API endpoint is correctly set up and accessible.
- You may want to update the CSS file (`css/custom_styles.css`) to further customize the look and feel of the frontend.

## License
This project is open-source and available under the MIT License.

## Contributing
Feel free to fork this project, open an issue, or submit pull requests to contribute to AI Frontend. We welcome any enhancements or bug fixes.

## Contact
For more information, feel free to reach out to the maintainer via [ai-frontend@hackedyour.info].

