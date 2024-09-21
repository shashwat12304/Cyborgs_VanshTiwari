import os
import json
import uuid
from processor import Chatting, OpenProcessor, GPTProcessor, VideoToImageConverter
from rag import RAG
import gradio as gr
import shutil

def process_image(image):
    upload_dir = r'C:\Users\Shashwat.Sharma\Documents\cyborgs\uploads'
    os.makedirs(upload_dir, exist_ok=True)
    
    # Generate a unique filename
    unique_id = str(uuid.uuid4())
    image_extension = os.path.splitext(image)[1]
    unique_filename = f"{unique_id}{image_extension}"
    
    image_path = os.path.join(upload_dir, unique_filename)
    
    # Use shutil.copy2 instead of os.rename to avoid issues with files on different devices
    shutil.copy2(image, image_path)
    
    processor = OpenProcessor()
    result = processor.process_image(image_path)
    return result

def process_video(video):
    upload_dir = r'C:\Users\Shashwat.Sharma\Documents\cyborgs\uploads'
    os.makedirs(upload_dir, exist_ok=True)
    
    # Generate a unique filename
    unique_id = str(uuid.uuid4())
    video_extension = os.path.splitext(video)[1]
    unique_filename = f"{unique_id}{video_extension}"
    
    video_path = os.path.join(upload_dir, unique_filename)
    
    # Use shutil.copy2 instead of os.rename to avoid issues with files on different devices
    shutil.copy2(video, video_path)
    
    processor = OpenProcessor()
    result = processor.process_video(video_path)
    return result

def update_invoice_details(result):
    try:
        result_dict = json.loads(result) if isinstance(result, str) else result
        amount = result_dict.get("bill_amount", "Error")
        category = result_dict.get("invoice_category", "Error")
        additional_info = result_dict.get("additional_information", {})
        
        info_str = json.dumps(additional_info, indent=2)
        
        return str(amount), category, info_str
    except Exception as e:
        return "Error", "Error", f"Error parsing result: {str(e)}"

def chat_response(message, history):
    chat = Chatting()
    ans = chat.chat(message)
    history.append((message, ans))
    return "", history

def export_data(history):
    export_dir = r'C:\Users\Shashwat.Sharma\Documents\cyborgs\exports'
    os.makedirs(export_dir, exist_ok=True)
    export_file = os.path.join(export_dir, f"chat_export_{uuid.uuid4()}.txt")
    
    with open(export_file, 'w', encoding='utf-8') as f:
        for user_msg, assistant_msg in history:
            f.write(f"User: {user_msg}\n")
            f.write(f"Assistant: {assistant_msg}\n\n")
    
    return f"Chat exported successfully to {export_file}"

def create_invoice_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# InvoiceAI Pro")
        with gr.Row():
            with gr.Column(scale=2):
                gr.Markdown("## Invoice Processing")
                with gr.Row():
                    image_input = gr.Image(label="Upload Image", type="filepath")
                    video_input = gr.Video(label="Upload Video")
                process_image_btn = gr.Button("Process Image")
                process_video_btn = gr.Button("Process Video")
                output = gr.Textbox(label="Processing Output")
                gr.Markdown("## Invoice Processing Assistant")
                chatbot = gr.Chatbot()
                msg = gr.Textbox(placeholder="Enter your message here...")
                clear = gr.Button("Clear")
                msg.submit(chat_response, [msg, chatbot], [msg, chatbot])
                clear.click(lambda: None, None, chatbot, queue=False)
                with gr.Row():
                    send_btn = gr.Button("Send")
                    clear_chat_btn = gr.Button("Clear Chat")
                    save_chat_btn = gr.Button("Save Chat")
                    send_btn.click(fn=chat_response, inputs=[msg, chatbot], outputs=[msg, chatbot])
                export_btn = gr.Button("Export Data")
                export_output = gr.Textbox(label="Export Status")
                export_btn.click(fn=export_data, inputs=chatbot, outputs=export_output)

            with gr.Column(scale=1):
                gr.Markdown("## Invoice Details")
                amount = gr.Textbox(label="Detected Amount", value="Error")
                category = gr.Textbox(label="Invoice Category", value="Error")
                information = gr.Textbox(label="Information", value="Error", lines=10)

        # Update the process_image function to also update the invoice details
        def process_and_update(img):
            result = process_image(img)
            amount, category, info = update_invoice_details(result)
            return result, amount, category, info

        def process_video_and_update(vid):
            result = process_video(vid)
            amount, category, info = update_invoice_details(result)
            return result,amount, category, info

        process_image_btn.click(
            fn=process_and_update,
            inputs=image_input,
            outputs=[output, amount, category, information]
        )

        process_video_btn.click(
            fn=process_video_and_update,
            inputs=video_input,
            outputs=[output, amount, category, information]
        )

    return demo

if __name__ == "__main__":
    demo = create_invoice_ui()
    demo.launch()
