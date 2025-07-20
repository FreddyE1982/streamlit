import streamlit as st
from streamlit.testing.v1 import AppTest


def test_audio_input_interaction():
    def script():
        import streamlit as st
        st.audio_input("record")

    at = AppTest.from_function(script).run()
    widget = at.audio_input[0]
    assert widget.value is None

    at = widget.record_from_bytes("sound.wav", b"123").run()
    assert at.audio_input[0].value.getvalue() == b"123"


def test_camera_input_interaction():
    def script():
        import streamlit as st
        st.camera_input("picture")

    at = AppTest.from_function(script).run()
    widget = at.camera_input[0]
    assert widget.value is None

    at = widget.capture_from_bytes("img.jpg", b"abc").run()
    assert at.camera_input[0].value.getvalue() == b"abc"
