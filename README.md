# AWS Bedrock Model Invocation for Preferred User Alias Extraction

This repository provides a simple demonstration of integrating Python with AWS Bedrock to invoke foundation models, specifically leveraging the Meta Llama 3 8B Instruct model. The project showcases how to use AWS Bedrock's conversational AI API in Python, processing text transcripts to extract the user’s preferred alias or nickname. This serves as an example of how to access Bedrock's capabilities programmatically through the `boto3` SDK and configure an intelligent assistant application.
## Prerequisites

To run this project, you’ll need:
- An AWS account with access to Bedrock services.
- AWS credentials configured with access to the Bedrock service.
- Python 3, and the `boto3` and `botocore` libraries installed.

### References

This project was developed based on the following resources:
- [AWS Boto3 Documentation for Bedrock Invoke Model API](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/invoke_model.html)
- [AWS Code Library Bedrock Runtime Python Examples](https://docs.aws.amazon.com/code-library/latest/ug/python_3_bedrock-runtime_code_examples.html)

## Usage

### Step 1: List Available Models

To see the foundation models available in your AWS Bedrock environment, use the following command. This saves the list to a `bedrock_models.json` file, which is more readable than outputting directly to the console:

```bash
aws bedrock list-foundation-models | jq > bedrock_models.json
```

### Step 2: Configure the Prompt Template

The project uses a prompt template stored in a `prompt.txt` file located in the root of this project. This file provides specific structure and guidance for the model on how to interpret the input and output. 

#### Key Points:
- **Document Tags**: The tags `<DOCUMENT>` and `<TRANSCRIPTION>` structure the input as a formatted document and transcription. These tags help the model interpret that it’s working within a document-based structure, guiding it to "read" and analyze sections in a detailed, organized way.
  
- **Output Format**: The prompt includes a predefined output format with `"PREFERRED_USER_ALIAS = ..."`. This output structure instructs the model to follow a consistent format in the response, ensuring that results are presented accurately.

Please refer to `prompt.txt` for the complete content of this template.

### Step 3: Update the Script Variables

In `main.py`, update the following variables:

- `region_name`: The AWS region where Bedrock is accessible.
- `model_id`: The model ID of the specific Meta Llama version you intend to use.
- `transcription`: Replace this with the text you want to analyze.

### Step 4: Execute the Script

Run the script to invoke the Bedrock model and receive the preferred name or nickname in the output.

```bash
python main.py
```

### Expected Output

The script will print the user's preferred name or nickname based on the transcription provided. The expected output format is:

```plaintext
PREFERRED_USER_ALIAS = {DETECTED_NAME}
```

## Error Handling

If any errors occur during the invocation, the script provides clear error messages for troubleshooting. Special conditions, such as offensive names or users declining to provide a preferred alias, are handled as per the prompt template.

## Limitations

This project is intended for educational purposes only and should not be used in other context (such as production environments).

## Contributing

Your contributions are welcome! If you have suggestions for improvements, encounter any issues, or would like to contribute to the development of this project, please feel free to submit pull requests or report issues via the GitHub issue tracker.

## License and Disclaimer

This project is open-source and available under [MIT License](https://opensource.org/licenses/MIT). You are free to copy, modify, and use the project as you wish. However, any responsibility for the use of the code is solely yours. Please use it at your own risk and discretion.
