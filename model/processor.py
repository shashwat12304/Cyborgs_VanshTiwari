import base64
import os
import cv2
import requests
import json
from dotenv import load_dotenv
load_dotenv()
import requests
import json
import base64
from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage
import re
from rag import RAG
chat = RAG().getcollection("invoice2")

class VideoToImageConverter:
    def __init__(self, video_path, output_dir):
        self.video_path = video_path
        self.output_dir = output_dir

    def extract_images(self):
        cap = cv2.VideoCapture(self.video_path)

        if not cap.isOpened():
            print(f"Error: Unable to open video file {self.video_path}")
            return

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f"Total frames in the video: {total_frames}")

        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            image_filename = os.path.join(self.output_dir, f"frame_{frame_count}.jpg")
            cv2.imwrite(image_filename, frame)
            print(f"Saved {image_filename}")
            frame_count += 1

        cap.release()
        print(f"Finished extracting frames. Total frames extracted: {frame_count}")

class GPTProcessor:
    def __init__(self):
        openai_api_key = os.getenv("OPENAI_API_KEY")
        self.sysprompt = '''
        You are an advanced OCR and image analysis system designed to process invoices. Your task is to:
        Detect and extract the total bill amount from invoice images or video frames.
        Categorize invoices based on their content and return the following in JSON format.
        - BILL AMOUNT
        - INVOICE CATEGORY
        - FURTHER INFORMATION
        - ANALYSIS
        '''
    
    def convert_nested_json_string_to_json(self, json_string):
        try:
            json_object = json.loads(json_string)
            if "output" in json_object:
                json_object["output"] = json.loads(json_object["output"])
            return json_object
        except json.JSONDecodeError as e:
            print("Invalid JSON string:", e)
            return None

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
                "response_format":{ "type": "json_object" },
                "max_tokens": 300
            }
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            return response.json()
        except Exception as e:
            print(f"Error during OCR: {e}")
    def save_output_to_file(self, output, file_path):
        try:
            content = output['choices'][0]['message']['content']
            content = self.convert_nested_json_string_to_json(content)
            with open(file_path, 'w') as f:
                json.dump(content, f, indent=4)
            print(f"Output saved to {file_path}")
        except Exception as e:
            print(f"Error saving output to file: {e}")

    def main(self, image_path, output_file_path):
        data = self.get_base64(image_path)
        output = self.ocr(data)
        print(output)
        self.save_output_to_file(output, output_file_path)

    def process_videos(self,video_folder, output_folder, resultants_folder):
        video_files = [f for f in os.listdir(video_folder) if f.endswith('.mp4')]

        for video_file in video_files:
            video_path = os.path.join(video_folder, video_file)
            video_name = os.path.splitext(video_file)[0]
            print(f"Processing video {video_name}")
            video_output_dir = os.path.join(output_folder, video_name)
            os.makedirs(video_output_dir, exist_ok=True)
            converter = VideoToImageConverter(video_path, video_output_dir)
            converter.extract_images()
            images = [f for f in os.listdir(video_output_dir) if f.endswith('.jpg')]
            if images:
                try:
                    selected_image = os.path.join(video_output_dir, images[0])
                except Exception as e:
                    print("Error getting the video frame")
                try:
                    result_file = os.path.join(resultants_folder, f"{video_name}_result.json")
                    self.main(selected_image, result_file)
                except Exception as e:
                    print("Error processing the frames")
    
    def runner(self,video_folder,resultant_folder):
        output_folder = r"C:\Users\Shashwat.Sharma\Documents\cyborgs\VideoFrames" 
        video_folder = r"C:\Users\Shashwat.Sharma\Documents\cyborgs\Videos" 
        resultants_folder = r"C:\Users\Shashwat.Sharma\Documents\cyborgs\Results"  
        os.makedirs(output_folder, exist_ok=True)
        os.makedirs(resultants_folder, exist_ok=True)
        self.process_videos(video_folder, output_folder, resultants_folder)
    
class OpenProcessor:
    def __init__(self):
        self.url = "https://api.veryfi.com/api/v8/partner/documents"

    def extract_json(self, content):
        content = content.strip()
        if content.startswith("{") and content.endswith("}"):
            try:
                parsed_json = json.loads(content)
                return parsed_json
            except json.JSONDecodeError:
                print("Invalid JSON structure in the entire content.")
        json_block = re.search(r'```json(.*?)```', content, re.DOTALL)
        if json_block:
            json_str = json_block.group(1).strip()
            try:
                parsed_json = json.loads(json_str)
                return parsed_json
            except json.JSONDecodeError:
                print("Invalid JSON within the block.")
        return None
    def convert_nested_json_string_to_json(self,json_string):
        try:
            json_object = json.loads(json_string)
            if "output" in json_object:
                json_object["output"] = json.loads(json_object["output"])
            return json_object
        except json.JSONDecodeError as e:
            print("Invalid JSON string:", e)
            return None
    def llm(self,data):
        llm = ChatOllama(
            model="llava:13b",
            temperature=0
        )
        messages = [
            (
                "system",
                '''
                You are a helpful assistant that processes bill invoices and returns a JSON having - bill amount, invoice category and additional information.
                #Instructions:
                - If there is amount such that 165 00 than it is 165, there is a decimal in between.
                -Return JSON only, no explanation, nothing.
                - Output the JSON in the above format mentioned
                ''',
            ),
            ("human", f"{data}"),
        ]
        ai_msg = llm.invoke(messages,response_format="json")
        print(ai_msg.content)
        return ai_msg.content
    def processor(self,image_path):
        try:
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

        except Exception as e:
            print(f"{e}")
        payload = json.dumps({
        "file_data": encoded_string,
        "categories": [
            "string"
        ],
        "tags": [
            "string"
        ],
        "country": "IR"
        })
        headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'CLIENT-ID': 'vrfTeKjlAJcKszu5LkMe46nFoXjFrabzVhCAAXk',
        'AUTHORIZATION': 'apikey shashwatsharma12304:b47770c75d26a5904a2cb00a76a193c0'
        }
        response = requests.request("POST", self.url, headers=headers, data=payload)
        print(response.text)
        fop = self.convert_nested_json_string_to_json(response.text)
        return fop["ocr_text"]
    def save_output_to_file(self, output, file_path):
        try:
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Directory {directory} created.")
            with open(file_path, 'w') as f:
                json.dump(output, f, indent=4)
            print(f"Output saved to {file_path}")
        except Exception as e:
            print(f"Error saving output to file: {e}")

    def main(self, image_path, output_file_path):
        output = self.processor(image_path)
        text = output
        output =self.extract_json(self.llm(output))
        print(output)
        self.save_output_to_file(output, output_file_path)
        return text

    def process_videos(self,video_folder,resultants_folder):
        output_folder=r'C:\Users\Shashwat.Sharma\Documents\cyborgs\VideoFrames'
        video_files = [f for f in os.listdir(video_folder) if f.endswith('.mp4')]
        chunks = []
        for video_file in video_files:
            video_path = os.path.join(video_folder, video_file)
            video_name = os.path.splitext(video_file)[0]
            print(f"Processing video {video_name}")
            video_output_dir = os.path.join(output_folder, video_name)
            os.makedirs(video_output_dir, exist_ok=True)
            converter = VideoToImageConverter(video_path, video_output_dir)
            converter.extract_images()
            images = [f for f in os.listdir(video_output_dir) if f.endswith('.jpg')]
            if images:
                try:
                    selected_image = os.path.join(video_output_dir, images[0])
                except Exception as e:
                    print("Error getting the video frame")
                try: 
                    result_file = os.path.join(resultants_folder, f"{video_name}_result.json")
                    text = self.main(selected_image, result_file)
                    chunks.append(text)
                except Exception as e:
                    print("Error processing the frames")
        return chunks
class Chatting:
    def __init__(self):
        pass
    def upsert(self,doc):
        chat.add(doc)
    def chat(self,user_query):
        contexts = chat.get_contexts(user_query)
        ans = chat.llm(user_query,contexts)
        return ans
if __name__ == '__main__':
    mode = input("Enter mode: chat OR upload")
    if mode=='chat':
        query = input("Let's chat!\n Please enter your user query!\n")
        chate = Chatting()
        ans = chate.chat(query)
        print(ans)
    if mode=='upload':
        collection = input("Please enter the collection name")
        chat.getcollection(collection)
        videos_path=r'C:\Users\Shashwat.Sharma\Documents\cyborgs\Videos'
        results_path = r'C:\Users\Shashwat.Sharma\Documents\cyborgs\results2'
        x = OpenProcessor().process_videos(videos_path,results_path)
        chat.add(x)

        



