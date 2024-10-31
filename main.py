import boto3
from botocore.exceptions import ClientError

# Define the required variables
region_name = 'us-east-1'  # AWS Region where Bedrock is accessible
model_id = 'meta.llama3-8b-instruct-v1:0'  # Model ID for Meta Llama 3 8B Instruct
transcription = "Hello, my name is Carlos Biagolini"  # Text to be processed by the model

# Load the content of the prompt template from the file and replace {TRANSCRIPTION} with the actual text
with open("prompt.txt", "r", encoding="utf-8") as file:
    prompt_template = file.read()
prompt_text = prompt_template.format(TRANSCRIPTION=transcription)

# Create the Boto3 client for Bedrock Runtime
client = boto3.client('bedrock-runtime', region_name=region_name)

# Initiate the conversation with the processed prompt content
conversation = [
    {
        "role": "user",
        "content": [{"text": prompt_text}],
    }
]

try:
    # Send the message to the model with basic inference configuration
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={"maxTokens": 20, "temperature": 0.05, "topP": 0.9},
    )

    # Extract and print the text of the response
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Could not invoke '{model_id}'. Reason: {e}")
    exit(1)
