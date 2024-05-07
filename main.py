import streamlit as st
import replicate

st.markdown("# :blue[AI Генератор изображений]")
REPLICATE_API_TOKEN = st.secrets["REPLICATE_API_TOKEN"]


def configure_sidebar():
    with st.sidebar:
        with st.form("my_form"):
            width = st.number_input("Ширина картинки", min_value=256, max_value=2560, value=1920, step=16)
            height = st.number_input("Высота картинки", min_value=256, max_value=1400, value=1080, step=16)
            prompt = st.text_area("Введите промпт")
            submitted = st.form_submit_button("Сгенерировать", type="primary")

        return {
            "width": width,
            "height": height,
            "prompt": prompt,
            "submitted": submitted,
        }


def main_sector(
    width: int,
    height: int,
    prompt: str,
    submitted: bool,
):
    if submitted:
        with st.spinner("Генерируется..."):
            result = replicate.run(
                "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
                input={
                    "width": width,
                    "height": height,
                    "prompt": prompt,
                }
            )
            image = result[0]
            with st.container():
                st.image(image)


def main():
    params = configure_sidebar()
    main_sector(**params)


if __name__ == "__main__":
    main()
