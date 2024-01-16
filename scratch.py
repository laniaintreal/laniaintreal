import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="laniaintreal", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/3b5f3975-b094-418d-9632-a2f819cbc9ed/rF2u5O5aKG.json")

# ---- HEADER SECTION ----
st.subheader("Hi, I am Al Ain :wave:")
st.title("A University Student from Phoenix")
st.write("I am passionate about learning ways to utilize Python and other coding languages to "
         "aid me in my academic and professional career.")
st.write("[Learn More >](https://www.tiktok.com/@laniaintreal?_t+8j4AQTxrDXK&_r=1)")

# ---- WHAT I DO ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my Tiktok page I post videos of me trying to learn and improve on certain skills
            These range from singing, dancing, drawing, playing the guitar, and many more.
            
            If any of this sounds interesting to you, consider supporting my page by following my instagram 
            where I post updates and stories on whereabouts almost daily!""")

        st.write("[Instagram >](https://www.instagram.com/laniaintreal?igsh=aDBrbW1tMzM4MG9j)")
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")
