import streamlit as st
import random
from pathlib import Path

DRAWINGS_FOLDER = Path(__file__).parent / "assets" / "one_moment"

# ---------------------------------------------------------
# DRAWINGS — KEPT EXACTLY AS THEY ARE
# ---------------------------------------------------------

DRAWINGS = [
    "drawing_1.jpg",
    "drawing_2.jpg",
    "drawing_3.jpg",
    "drawing_4.jpg",
    "drawing_5.jpg",
    "drawing_6.jpg",
]

# ---------------------------------------------------------
# ONE MOMENT ACTIVITIES
# ---------------------------------------------------------

ACTIVITIES = [
    {
        "type": "drawing",
        "title": "🎨 Create",
        "instruction": "Take a paper and pencil. Look at the picture and draw it.",
        "focus": "Don't worry about making it perfect. Just follow the picture slowly."
    },

    {
        "title": "🧘 60-Second Body Reset",
        "instruction": "Sit or stand comfortably. Drop your shoulders, unclench your jaw, relax your hands, and take five slow, comfortable breaths.",
        "focus": "Notice how your body feels before and after the minute."
    },
    {
        "title": "🧘 Shoulder Release",
        "instruction": "Roll your shoulders slowly backwards 5 times and forwards 5 times. Then gently stretch your arms overhead and relax them.",
        "focus": "Pay attention to the movement instead of thinking about what comes next."
    },
    {
        "title": "🧘 Gentle Stretch Chain",
        "instruction": "Do these slowly: neck stretch → shoulder rolls → side stretch → gentle forward stretch → ankle rotations. Spend about 20 seconds on each.",
        "focus": "There is no need to stretch deeply. Comfortable and slow is enough."
    },
    {
        "title": "🌿 Ground Your Feet",
        "instruction": "Place both feet firmly on the floor. Notice the pressure under your feet, your balance, and the surface supporting you for one minute.",
        "focus": "Keep bringing your attention back to the feeling of your feet touching the ground."
    },

    {
        "title": "👁️ The 5-4-3-2-1 Moment",
        "instruction": "Notice 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste.",
        "focus": "Move slowly from one sense to the next. There is nothing to finish quickly."
    },
    {
        "title": "👁️ One Object, One Minute",
        "instruction": "Choose one ordinary object near you. Look at it for one full minute. Notice its shape, edges, texture, shadows, and tiny details.",
        "focus": "Try to notice three things about it that you had never noticed before."
    },
    {
        "title": "🎨 Find a Color",
        "instruction": "Choose one color. Find five objects around you that contain that color. Look at each one carefully.",
        "focus": "Notice how the same color looks different on different objects."
    },
    {
        "title": "👂 Sound Detective",
        "instruction": "Close your eyes comfortably for 30 seconds. Find the nearest sound, the farthest sound, and one sound you almost didn't notice.",
        "focus": "You don't have to judge the sounds. Just notice them."
    },
    {
        "title": "🪟 Window Moment",
        "instruction": "Stand or sit near a window. Look outside for two minutes. Notice movement, light, clouds, people, trees, or anything changing.",
        "focus": "Watch without taking a photo or checking your phone."
    },
    {
        "title": "🔎 Tiny Detail Hunt",
        "instruction": "Choose something you see every day. Look closely and find five tiny details you normally ignore.",
        "focus": "Let curiosity replace rushing for just a minute."
    },

    {
        "title": "✋ Five-Object Sort",
        "instruction": "Pick five objects near you. Arrange them from smallest to largest, lightest to heaviest, or darkest to lightest.",
        "focus": "Give your full attention to the order you are creating."
    },
    {
        "title": "✋ Make One Small Space Better",
        "instruction": "Choose only one tiny area: one corner of your desk, one shelf, or one small section of a table. Improve it for three minutes.",
        "focus": "Stop when the three minutes are over. You don't need to clean everything."
    },
    {
        "title": "🌱 Care for Something",
        "instruction": "Find a plant or another small thing that needs care. Water it, clean it, straighten it, or simply spend a moment looking after it.",
        "focus": "Notice the feeling of doing one small caring action."
    },
    {
        "title": "📄 Slow Paper Fold",
        "instruction": "Take one sheet of paper. Fold it slowly into any simple shape. Pay attention to every edge, crease, and movement.",
        "focus": "Let your hands set the pace."
    },
    {
        "title": "🖐️ Texture Hunt",
        "instruction": "Find three safe objects with different textures: smooth, rough, soft, hard, warm, or cool. Touch each one slowly.",
        "focus": "Describe the texture silently in your mind."
    },

    {
        "title": "🫁 Counted Breathing",
        "instruction": "Breathe in gently while counting 1-2-3. Breathe out comfortably while counting 1-2-3-4. Repeat for five rounds.",
        "focus": "Keep the breathing natural. Stop if it feels uncomfortable."
    },
    {
        "title": "🕯️ Watch One Thing",
        "instruction": "Choose something gently moving around you—a curtain, a tree, a fan, clouds, or light and shadow. Watch it for one minute.",
        "focus": "Notice the movement without trying to control it."
    },
    {
        "title": "🧠 One Thought, Then Return",
        "instruction": "Sit quietly for one minute. When a thought appears, notice it and gently bring your attention back to your breathing or the feeling of your feet.",
        "focus": "The goal isn't to stop thinking. It's simply to return."
    },
    {
        "title": "🌤️ Sky Check",
        "instruction": "Look at the sky for one minute. Notice its color, brightness, clouds, movement, and the way the light looks.",
        "focus": "You don't need to name everything. Just observe."
    },
    {
        "title": "💧 Water Moment",
        "instruction": "Take a glass of water and drink it slowly. Notice its temperature, taste, and the feeling as you swallow.",
        "focus": "For this glass of water, do nothing else."
    },

    {
        "title": "🧩 Memory Snapshot",
        "instruction": "Look around you for 20 seconds. Then look away and try to remember five things you saw.",
        "focus": "Check afterward how many details you remembered."
    },
    {
        "title": "🔢 Count What You See",
        "instruction": "Choose one simple thing around you—windows, books, plants, chairs, or lights. Count how many you can find.",
        "focus": "Keep counting slowly until you have checked the whole space."
    },
    {
        "title": "🚶 Mindful Ten Steps",
        "instruction": "Walk ten slow steps. Notice each foot touching the floor, your balance, and the movement of your legs.",
        "focus": "For ten steps, walking is the only thing you need to think about."
    },
    {
        "title": "🤲 Hands at Work",
        "instruction": "Choose a simple task such as folding clothes, arranging books, or sharpening a pencil. Do it slowly for two minutes.",
        "focus": "Notice each movement instead of trying to finish quickly."
    },
    {
        "title": "🌼 Notice Something Beautiful",
        "instruction": "Find one small thing you genuinely like looking at—a flower, object, color, pattern, or view. Spend one quiet minute with it.",
        "focus": "Notice why your attention naturally goes toward it."
    },
]


# ---------------------------------------------------------
# PAGE
# ---------------------------------------------------------

def one_moment_page():

    st.html("""
    <div style="text-align:center; padding:10px 0 25px 0;">
        <h1 style="color:#F4EFFF; font-size:38px; margin-bottom:8px;">
            🌿 One Moment
        </h1>
        <p style="color:#C7B6F5; font-size:18px;">
            You don't have to solve everything right now.<br>
            Just give this moment your attention.
        </p>
    </div>
    """)

    if "one_moment_activity" not in st.session_state:

        # Drawing appears about 35% of the time.
        if random.random() < 0.35:
            st.session_state.one_moment_activity = {
                "type": "drawing",
                "title": "🎨 Create",
                "instruction": "Take a paper and pencil. Look at the picture and draw it.",
                "focus": "Don't worry about making it perfect. Just follow the picture slowly."
            }
        else:
            st.session_state.one_moment_activity = random.choice(
                [a for a in ACTIVITIES if a.get("type") != "drawing"]
            )

    activity = st.session_state.one_moment_activity

    st.html(f"""
    <div style="text-align:center; padding:10px 0 15px 0;">
        <h2 style="color:#F4EFFF; font-size:28px; margin-bottom:12px;">
            {activity["title"]}
        </h2>
        <p style="
            color:#D7B8FF;
            font-size:17px;
            line-height:1.7;
            max-width:700px;
            margin:0 auto;
        ">
            {activity["instruction"]}
        </p>
    </div>
    """)

    if activity.get("type") == "drawing":

        if "one_moment_drawing" not in st.session_state:
            st.session_state.one_moment_drawing = random.choice(DRAWINGS)

        image_path = DRAWINGS_FOLDER / st.session_state.one_moment_drawing

        if image_path.exists():
            left, center, right = st.columns([1, 1, 1])
            with center:
                st.image(str(image_path), width=220)
        else:
            st.error(
                f"Could not find {st.session_state.one_moment_drawing}. "
                "Please check the assets/one_moment folder."
            )

    st.html(f"""
    <div style="
        max-width:650px;
        margin:15px auto 25px auto;
        padding:14px 20px;
        border-radius:14px;
        background:rgba(125,82,180,0.10);
        text-align:center;
        color:#D7B8FF;
        font-size:15px;
    ">
        🌱 <b>Focus:</b> {activity["focus"]}
    </div>
    """)

    left, center, right = st.columns([1, 2, 1])

    with center:
        if st.button(
            "✨ Give me another",
            use_container_width=True
        ):
            # Drawing appears about 35% of the time.
            if random.random() < 0.35:
                st.session_state.one_moment_activity = {
                    "type": "drawing",
                    "title": "🎨 Create",
                    "instruction": "Take a paper and pencil. Look at the picture and draw it.",
                    "focus": "Don't worry about making it perfect. Just follow the picture slowly."
                }
            else:
                st.session_state.one_moment_activity = random.choice(
                    [a for a in ACTIVITIES if a.get("type") != "drawing"]
                )

            st.session_state.pop("one_moment_drawing", None)
            st.rerun()