import streamlit as st
from streamlit.testing.v1 import AppTest


def test_download_button_interaction():
    def script():
        import streamlit as st
        st.download_button("dl", data="hello")

    at = AppTest.from_function(script).run()
    widget = at.download_button[0]
    at = widget.click().run()
    assert at.download_button
    assert at.download_button[0].url
