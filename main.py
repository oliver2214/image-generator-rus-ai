import streamlit as st

st.markdown("# :blue[AI Генератор изображений]")


def configure_sidebar():
    with st.sidebar:
        with st.form("my_form"):
            width = st.number_input("Ширина картинки", min_value=256, max_value=2048, value=1024, step=16)
            height = st.number_input("Высота картинки", min_value=256, max_value=2048, value=1024, step=16)
            prompt = st.text_area("Введите промпт")
            submitted = st.form_submit_button("Сгенерировать", type="primary")


def main():
    configure_sidebar()


if __name__ == "__main__":
    main()
