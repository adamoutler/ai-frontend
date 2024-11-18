import gradio as gr
import os
import requests
import json

# Get environmental variables for API key and BOT ID
APIKEY = os.getenv('APIKEY')
BOTID = os.getenv('BOTID')
COMPLETIONSURL = os.getenv('COMPLETIONSURL')
SYSTEMPROMPT= os.getenv('SYSTEMPROMPT')

# Load custom CSS for the interface
script_dir = os.path.dirname(os.path.realpath(__file__))
css_path = os.path.join(script_dir, 'css/custom_styles.css')
with open(css_path, 'r') as css_file:
    css = css_file.read()

#Headers for the API request
HEADERS = {
    "Authorization": f"Bearer {APIKEY}",
    "Content-Type": "application/json"
}

# Prepare data in OpenAI-compatible format
PAYLOAD = {
    "model": BOTID,
    "messages": []
}

def chatbot_fn(messages, user_input):
    """ Function to handle chatbot conversation """
    if messages is None:
        PAYLOAD["messages"]=[{"role": "System", "content": SYSTEMPROMPT}]
    else:
        PAYLOAD["messages"]=messages
    
    PAYLOAD["messages"].append({"role": "user", "content": user_input})

    try:
        response = requests.post(COMPLETIONSURL, headers=HEADERS, data=json.dumps(PAYLOAD))
        response.raise_for_status()
        bot_response = response.json().get("choices")[0].get("message").get("content")
    except requests.RequestException as e:
        bot_response = f"Error communicating with the API: {str(e)}"
    PAYLOAD["messages"].append({"role": "assistant", "content": bot_response})

    return PAYLOAD["messages"], PAYLOAD["messages"]

def initialize():
    """ Initialize the chatbot interface"""
    with gr.Blocks(css=css) as frontend:
        chatbot = gr.Chatbot(type="messages", label="Chatbot Conversation")
        state = gr.State()

        # Group to contain the input text box and send button neatly
        with gr.Group(elem_id="input-group", elem_classes=["compact-group"]):
            with gr.Row(elem_id="input-container"):
                user_input = gr.Textbox(
                    show_label=False,
                    placeholder="Type your message here...",
                    container=False,
                    elem_classes=["text-area"]
                )
                send_button = gr.Button("Send", elem_id="send_button", elem_classes=["send-button"])


        # Define actions when the send button is clicked or enter is pressed in the input box
        send_button.click(fn=chatbot_fn, inputs=[state, user_input], outputs=[state, chatbot])
        user_input.submit(fn=chatbot_fn, inputs=[state, user_input], outputs=[state, chatbot])
    
# Launch the customized interface
    frontend.launch(server_name="0.0.0.0")


if __name__ == "__main__":
    initialize()