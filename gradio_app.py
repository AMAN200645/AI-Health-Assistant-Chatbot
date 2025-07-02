import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

def generate_answer(question, model):
    prompt = "Answer the following question: " + question
    tokenizer = AutoTokenizer.from_pretrained("./phi1.5")
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    input_ids = input_ids.to(model.device)  # Send to correct device
    output = model.generate(input_ids, max_length=512, do_sample=True, top_k=50, top_p=0.9)[0]
    answer = tokenizer.decode(output, skip_special_tokens=True)
    end_of_text_index = answer.find("(end of text)")
    if end_of_text_index > -1:
        answer = answer[:end_of_text_index]
    return answer

def chatbot(question):
    answer = generate_answer(question, llm_model)
    return answer

if __name__ == "__main__":
    llm_model = AutoModelForCausalLM.from_pretrained("./phi1.5", trust_remote_code=True)

    interface = gr.Interface(
        fn=chatbot,
        inputs="text",
        outputs="text",
        title="I am your AI Health Assistance 🏥",
        description="Ask general health related question to the AI Bot."
    )
    interface.launch()
