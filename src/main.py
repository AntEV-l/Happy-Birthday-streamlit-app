# birthday_app.py
# streamlit run src/main.py


import streamlit as st
import time
import random
from datetime import datetime

# ─── Настройки страницы ───────────────────────────────────────
st.set_page_config(
    page_title="Happy Birthday 🎉",
    page_icon="🎂",
    layout="centered"
)


# ─── Стили и конфетти ─────────────────────────────────────────
def add_confetti():
    st.markdown(
        """
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
        <script>
        function shootConfetti() {
            confetti({
                particleCount: 120,
                spread: 70,
                origin: { y: 0.6 },
                colors: ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff']
            });
        }
        setTimeout(shootConfetti, 300);
        setTimeout(shootConfetti, 900);
        setTimeout(shootConfetti, 1500);
        </script>
        """,
        unsafe_allow_html=True
    )


# ─── Messages  ───────────────────────────────────
messages = [
    "Happy Birthday! I hope your special day will be funny and bring a lot of happiness and love to you! ✨",
    "You are a space! keep shining brighter  🌟",
    "I wish you money, funny, honey and a lot of awesome bunnies!",
    "May this year give you +100500 reasons for your smile! 😄",
    "You have become older. But if you see a problem in it you should open a bottle of beer and play computer games!🎮",
    "Health, love, adventures and  Wi-Fi 5G always 📶",
    "Unluck, random does not in you side, please try again.",
]


st.title("🎉 Happy Birthday 🎂")

name = st.text_input("What is you name?", placeholder="What is you name...", max_chars=30)

if st.button("Do you want a congratulation?? Just click me 🚀", type="primary", use_container_width=True):
    if not name.strip():
        name = "You have not told you name! What about have you thought?? Enter your name and try again!"
        st.title(name)
        exit(0)
    st.balloons()
    add_confetti()


    placeholder = st.empty()

    full_text = f"Dear {name.strip().title()}!"
    for i in range(len(full_text) + 1):
        placeholder.markdown(f"## {full_text[:i]}")
        time.sleep(0.08)

    time.sleep(0.6)


    wish = random.choice(messages)
    st.markdown(f"### {wish}")

    st.divider()


    cols = st.columns(3)
    with cols[0]:
        st.metric("Health", "∞")
    with cols[1]:
        st.metric("Happiness", "999+")
    with cols[2]:
        st.metric("Money", "💰" * random.randint(5, 12))

    st.markdown("---")
    st.caption(f"Congratulation have generated {datetime.now().strftime('%d.%m.%Y %H:%M')} special for you! 💙")

else:
    st.info("Enter you name - it will be funny! 🎈")