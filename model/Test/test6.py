import requests
import json
import base64
url = "https://api.veryfi.com/api/v8/partner/documents"
def convert_nested_json_string_to_json(json_string):
    try:
        json_object = json.loads(json_string)
        if "output" in json_object:
            json_object["output"] = json.loads(json_object["output"])
        return json_object
    except json.JSONDecodeError as e:
        print("Invalid JSON string:", e)
        return None
def get_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return encoded_string
    except Exception as e:
        print(f"{e}")
def send_request(data):
    payload = json.dumps({
    "file_data": data,
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

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return response.text
if __name__=="__main__":
    data = get_base64(r"C:\Users\Shashwat.Sharma\Documents\cyborgs\VideoFrames\video1\frame_0.jpg")
    op = send_request(data)
    fop = convert_nested_json_string_to_json(op)
    print(fop["ocr_text"])
