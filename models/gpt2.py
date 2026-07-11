from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

def generate_text(prompt):
    result = generator(
        prompt,
        max_new_tokens=40,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.8,
        top_k=50,
        top_p=0.9,
        repetition_penalty=1.5,
        pad_token_id=50256
    )

    text = result[0]["generated_text"]

    if text.startswith(prompt):
        text = text[len(prompt):].strip()

    return text