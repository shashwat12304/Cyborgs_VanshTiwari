from processor import Chatting, OpenProcessor,GPTProcessor,VideoToImageConverter
from rag import RAG
import gradio as gr

def process_image(image):
    chat = RAG().getcollection("invoicefinal")
    collection = "invoicefinal"
    chat.getcollection(collection)
    videos_path=r'C:\Users\Shashwat.Sharma\Documents\cyborgs\Videos'
    results_path = r'C:\Users\Shashwat.Sharma\Documents\cyborgs\results2'
    x = OpenProcessor().process_video(videos_path)
    chat.add(x)
    return "Image processed successfully"

def chat_response(message):
    chat=Chatting()
    ans = chat.chat(message)
    return f"You said: {ans}"

def export_data():
    # Placeholder function for data export
    return "Data exported successfully"

def create_invoice_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# InvoiceAI Pro")
        
        with gr.Row():
            with gr.Column(scale=2):
                gr.Markdown("## Invoice Processing")
                
                with gr.Row():
                    image_input = gr.Image(label="Upload Image", type="filepath")
                    video_input = gr.Video(label="Upload Video")
                
                process_btn = gr.Button("Process Image/Video")
                output = gr.Textbox(label="Processing Output")
                process_btn.click(fn=process_image, inputs=image_input, outputs=output)
                image_input.upload(fn=process_image, inputs=image_input, outputs=output)
                gr.Markdown("## Invoice Processing Assistant")
                
                chatbot = gr.Chatbot()
                msg = gr.Textbox()
                clear = gr.Button("Clear")

                msg.submit(chat_response, msg, chatbot)
                clear.click(lambda: None, None, chatbot, queue=False)
        
                with gr.Row():
                    send_btn = gr.Button("Send")
                    clear_chat_btn = gr.Button("Clear Chat")
                    save_chat_btn = gr.Button("Save Chat")
                
                # Add functionality to the Send button to trigger chat_response
                send_btn.click(fn=chat_response, inputs=msg, outputs=chatbot)
                export_btn = gr.Button("Export Data")
                export_output = gr.Textbox(label="Export Status")
                
                export_btn.click(fn=export_data, outputs=export_output)
            
            with gr.Column(scale=1):
                gr.Markdown("## Invoice Details")
                amount = gr.Textbox(label="Detected Amount", value="Error")
                category = gr.Textbox(label="Invoice Category", value="Error")
                date = gr.Textbox(label="Date", value="Error")
                vendor = gr.Textbox(label="Vendor", value="Error")
                status = gr.Textbox(label="Status", value="Error")

    return demo

if __name__ == "__main__":
    demo = create_invoice_ui()
    demo.launch()