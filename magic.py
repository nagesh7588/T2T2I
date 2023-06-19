import streamlit as st
import openai

# Set up OpenAI API

openai.api_key = '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'
# Define text-to-text generation function using OpenAI API
def generate_text(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

# Define text-to-image generation function using OpenAI API
def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
    )
    return response["data"][0]["url"]

# Set up Streamlit interface
def main():
    st.title("Text Generation with OpenAI")

    option = st.sidebar.selectbox("Select a mode:", ("Text-to-Text Generation", "Text-to-Image Generation"))

    if option == "Text-to-Text Generation":
        st.subheader("Text-to-Text Generation")
        text_prompt = st.text_area("Enter a text prompt", height=100)
        if st.button("Generate"):
            output = generate_text(text_prompt)
            st.write(output)

    elif option == "Text-to-Image Generation":
        st.subheader("Text-to-Image Generation")
        text_prompt = st.text_area("Enter a text prompt", height=100)
        if st.button("Generate"):
            image_url = generate_image(text_prompt)
            st.image(image_url)

if __name__ == "__main__":
    main()
