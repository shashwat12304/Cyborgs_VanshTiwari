import base64
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
import requests
import json

class Processor:
    def __init__(self):
        openai_api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=openai_api_key)
        self.sysprompt = '''
        You are an advanced OCR and image analysis system designed to process invoices. Your task is to:
        Detect and extract the total bill amount from invoice images or video frames.
        Categorize invoices based on their content.
        #RETURNS:
        - BILL AMOUNT
        - INVOICE CATEGORY
        - FURTHER INFORMATION
        - ANALYSIS
        '''

    def get_base64(self, image_path):
        try:
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return encoded_string
        except Exception as e:
            print(f"{e}")

    def ocr(self, image_data):
        try:
            api_key = os.getenv("OPENAI_API_KEY")
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            payload = {
                "model": "gpt-4o-mini",
                "messages": [
                    {
                        "role": "system",
                        "content": self.sysprompt
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "What’s in this image?"
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image_data}"
                                }
                            }
                        ]
                    }
                ],
                "max_tokens": 300
            }
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            return response.json()
        except Exception as e:
            print(f"Getting error {e}")

    def save_output_to_file(self, output, file_path):
        try:
            with open(file_path, 'w') as f:
                # Extract the text content from the output and write to the file
                content = output['choices'][0]['message']['content']
                f.write(content)
                print(f"Output successfully saved to {file_path}")
        except Exception as e:
            print(f"Error saving output to file: {e}")

    def main(self, image_path, output_file_path):
        data = self.get_base64(image_path)
        output = self.ocr(data)
        # Save the output to a text file
        self.save_output_to_file(output, output_file_path)

if __name__ == '__main__':
    image_path = r"C:\Users\Shashwat.Sharma\Documents\cyborgs\Images\sample1.png"
    output_file_path = r"C:\Users\Shashwat.Sharma\Documents\cyborgs\Images\invoice_output.txt"
    
    processor = Processor()
    processor.main(image_path, output_file_path)
