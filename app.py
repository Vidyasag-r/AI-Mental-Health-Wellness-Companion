import streamlit as st
import streamlit.components.v1 as components
from textblob import TextBlob
import google.generativeai as genai
import pandas as pd
import os
import json
from datetime import datetime
from comfort_library import comfort_library_page
from one_moment import one_moment_page

# ===== Integrated Letters Module =====
# ================= 1. STYLING =================
def load_css():
    st.markdown("""
<style>

/* ---------------- PAGE ---------------- */
.main-title{
    text-align:center;
    color:#F8F3FF;
    font-family:Georgia;
    font-size:42px;
    font-weight:bold;
    margin-bottom:8px;
}

.sub-title{
    text-align:center;
    color:#D9C6F2;
    font-size:17px;
    margin-bottom:35px;
}

/* ---------------- CARDS ---------------- */
.letter-card{
    background:rgba(255,255,255,.05);
    border:1px solid rgba(255,255,255,.10);
    border-radius:18px;
    padding:22px;
    margin-bottom:20px;
    transition:.25s;
}

.letter-card:hover{
    transform:translateY(-4px);
    border:1px solid #9D4EDD;
    box-shadow:0 0 18px rgba(157,78,221,.35);
}

.letter-title{
    color:white;
    font-family:Georgia;
    font-size:25px;
    font-weight:bold;
    margin-bottom:10px;
}

.letter-desc{
    color:#DDDDDD;
    line-height:1.7;
    font-size:15px;
}

/* ---------------- BUTTONS ---------------- */
div.stButton>button{
    width:100%;
    height:50px;
    border-radius:14px;
    border:1px solid #7B2FF7;
    background:#472466;
    color:white;
    font-size:16px;
    font-weight:600;
}

div.stButton>button:hover{
    background:#60358A;
    border:1px solid #B47CFF;
    color:white;
}

/* ---------------- JOURNAL ---------------- */
.paper-title{
    font-family:Georgia;
    color:#F4E8D6;
    font-size:40px;
    font-weight:bold;
}

.paper-date{
    text-align:right;
    color:#D9C2A3;
    margin-top:-45px;
    margin-bottom:20px;
    font-size:15px;
}

.paper-line{
    border-top:1px solid rgba(255,255,255,.20);
    margin-bottom:25px;
}

.paper-greeting{
    color:#F4E8D6;
    font-family:Georgia;
    font-size:30px;
}

.paper-note{
    color:#C8B39B;
    font-style:italic;
    margin-bottom:20px;
}

/* ---------------- TEXTAREA ---------------- */
div[data-testid="stTextArea"]{
    border:none !important;
    background:transparent !important;
}

div[data-testid="stTextArea"] textarea{
    background:#FFFDF8 !important;
    color:#4F2E18 !important;
    border-radius:18px !important;
    border:1px solid #DCC8A8 !important;
    padding:25px !important;
    font-size:18px !important;
    font-family:Georgia !important;
    line-height:2 !important;
    box-shadow:0 10px 25px rgba(0,0,0,.25) !important;
    background-image: repeating-linear-gradient(
        to bottom,
        transparent 0px,
        transparent 34px,
        rgba(160,120,70,.15) 35px
    ) !important;
}

div[data-testid="stTextArea"] textarea:focus{
    outline:none !important;
    box-shadow:0 10px 25px rgba(0,0,0,.25) !important;
}


/* ---------------- ALERTS ---------------- */
div[data-testid="stAlert"]{
    border-radius:12px;
}


/* -------------------------------------------------
   SIDEBAR VISUAL ILLUSTRATION
   Pure HTML/CSS — no external image required.
------------------------------------------------- */
.sidebar-illustration {
    position: relative;
    height: 285px;
    margin: 18px 0 8px 0;
    overflow: hidden;
    border-radius: 24px;
    background:
        radial-gradient(circle at 72% 20%, rgba(255, 214, 146, .16), transparent 18%),
        linear-gradient(180deg, #241044 0%, #160a2b 72%, #100720 100%);
    border: 1px solid rgba(210, 177, 255, .18);
    box-shadow: inset 0 0 35px rgba(145, 82, 220, .12),
                0 12px 28px rgba(0, 0, 0, .25);
}

.sky-glow {
    position: absolute;
    width: 130px;
    height: 130px;
    right: -25px;
    top: -30px;
    border-radius: 50%;
    background: rgba(180, 126, 255, .09);
    filter: blur(18px);
}

.moon {
    position: absolute;
    right: 22px;
    top: 20px;
    color: #f7dcff;
    font-size: 48px;
    line-height: 1;
    text-shadow: 0 0 18px rgba(246, 205, 255, .65);
    transform: rotate(-18deg);
}

.star {
    position: absolute;
    color: #f8d9ff;
    text-shadow: 0 0 10px rgba(255, 220, 255, .7);
}
.star1 { right: 72px; top: 17px; font-size: 13px; }
.star2 { right: 42px; top: 73px; font-size: 10px; }
.star3 { right: 112px; top: 45px; font-size: 18px; }

.window {
    position: absolute;
    left: 14px;
    top: 22px;
    width: 118px;
    height: 148px;
    border-radius: 58px 58px 8px 8px;
    background: #332052;
    border: 5px solid #53356e;
    box-shadow: 0 0 25px rgba(188, 122, 255, .12);
}

.window-sky {
    position: absolute;
    inset: 5px;
    border-radius: 50px 50px 3px 3px;
    background: linear-gradient(180deg, #18295b 0%, #6c4b91 58%, #d08491 100%);
    overflow: hidden;
}

.tiny-cloud {
    position: absolute;
    height: 8px;
    width: 34px;
    border-radius: 12px;
    background: rgba(220, 210, 238, .45);
}
.cloud1 { left: 10px; top: 55px; }
.cloud2 { right: 7px; top: 77px; width: 27px; opacity: .7; }

.window-sill {
    position: absolute;
    left: -9px;
    bottom: -10px;
    width: 136px;
    height: 12px;
    border-radius: 8px;
    background: #62436c;
}

.plant {
    position: absolute;
    left: 118px;
    bottom: 62px;
    width: 55px;
    height: 120px;
}

.stem {
    position: absolute;
    width: 3px;
    height: 92px;
    left: 27px;
    bottom: 18px;
    border-radius: 5px;
    background: #718e5e;
    transform-origin: bottom;
}
.stem1 { transform: rotate(-8deg); }

.leaf {
    position: absolute;
    width: 26px;
    height: 13px;
    border-radius: 100% 0 100% 0;
    background: #739d68;
}
.leaf1 { left: 5px; top: 36px; transform: rotate(25deg); }
.leaf2 { left: 27px; top: 48px; transform: rotate(205deg); }
.leaf3 { left: 2px; top: 63px; transform: rotate(8deg); }
.leaf4 { left: 29px; top: 77px; transform: rotate(205deg); }

.pot {
    position: absolute;
    bottom: 0;
    left: 12px;
    width: 34px;
    height: 29px;
    border-radius: 4px 4px 12px 12px;
    background: linear-gradient(90deg, #9d6171, #d48782, #8b5369);
}

.table {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    height: 74px;
    background: linear-gradient(180deg, #3c2147, #24132e);
    border-top: 3px solid #684066;
}

.lamp {
    position: absolute;
    left: 28px;
    bottom: 38px;
    width: 48px;
    height: 62px;
}
.lamp-shade {
    position: absolute;
    left: 5px;
    top: 0;
    width: 38px;
    height: 24px;
    border-radius: 50% 50% 10px 10px;
    background: #d79aa5;
    box-shadow: 0 0 22px rgba(255, 190, 160, .35);
}
.lamp-glow {
    position: absolute;
    left: 10px;
    top: 13px;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: rgba(255, 215, 156, .38);
    filter: blur(5px);
}
.lamp-stand {
    position: absolute;
    left: 23px;
    top: 23px;
    width: 3px;
    height: 30px;
    background: #b77981;
}

.book {
    position: absolute;
    bottom: 19px;
    width: 54px;
    height: 8px;
    border-radius: 3px;
    background: #8060a0;
}
.book1 { right: 18px; transform: rotate(-4deg); }
.book2 { right: 24px; bottom: 28px; width: 45px; background: #b06f87; transform: rotate(4deg); }

.cup {
    position: absolute;
    right: 22px;
    bottom: 38px;
    width: 25px;
    height: 23px;
    border-radius: 4px 4px 9px 9px;
    background: #d79aa5;
    color: #fff1f5;
    text-align: center;
    line-height: 23px;
    font-size: 12px;
}

.cat {
    position: absolute;
    left: 72px;
    bottom: 42px;
    width: 80px;
    height: 50px;
}
.cat-body {
    position: absolute;
    left: 8px;
    bottom: 0;
    width: 66px;
    height: 36px;
    border-radius: 50% 55% 42% 42%;
    background: #8f789b;
}
.cat-head {
    position: absolute;
    left: 43px;
    top: 2px;
    width: 34px;
    height: 31px;
    border-radius: 48% 48% 45% 45%;
    background: #a18baa;
}
.ear {
    position: absolute;
    top: -8px;
    width: 12px;
    height: 13px;
    background: #a18baa;
    clip-path: polygon(50% 0, 100% 100%, 0 100%);
}
.left-ear { left: 2px; transform: rotate(-10deg); }
.right-ear { right: 2px; transform: rotate(10deg); }

.cat-eye {
    position: absolute;
    top: 13px;
    width: 3px;
    height: 4px;
    border-radius: 50%;
    background: #25152f;
}
.eye1 { left: 9px; }
.eye2 { right: 9px; }

.cat-tail {
    position: absolute;
    left: 1px;
    bottom: 21px;
    width: 38px;
    height: 27px;
    border: 5px solid #8f789b;
    border-right: 0;
    border-bottom: 0;
    border-radius: 30px 0 0 0;
    transform: rotate(-18deg);
}

</style>
""", unsafe_allow_html=True)


# ================= 2. STORAGE =================
FILE_NAME = "letters.json"

def _load():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def _save(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def save_letter(letter_type, content):
    letters = _load()
    letters.append({
        "id": str(datetime.now().timestamp()),
        "type": letter_type,
        "content": content,
        "date": datetime.now().strftime("%d %B %Y")
    })
    _save(letters)

def load_letters():
    return _load()

def delete_letter(letter_id):
    letters = _load()
    letters = [x for x in letters if x["id"] != letter_id]
    _save(letters)


# ================= 3. MENU DATA =================
LETTER_TYPES = [
    {"title": "🌅 Dear Future Me", "description": "Write to the person you dream of becoming."},
    {"title": "❤️ Dear Younger Me", "description": "Comfort your younger self with kindness."},
    {"title": "🌧 Dear Me in Difficult Times", "description": "Leave yourself strength for hard days."},
    {"title": "☀ Dear Me in Happy Moments", "description": "Capture beautiful memories forever."},
    {"title": "📸 Letters I'll Never Forget", "description": "Preserve people, places and moments."},
    {"title": "🌙 Things I Never Said", "description": "Write the words you never got to speak."},
    {"title": "🙏 Thank You, Me", "description": "Celebrate your strength and growth."},
    {"title": "🎁 Open When...", "description": "A letter waiting for the perfect day."}
]


# ================= 4. UI VIEWS =================
def letter_card(letter, key):
    st.markdown(
        f"""
<div class="letter-card">
<div class="letter-title">{letter["title"]}</div>
<div class="letter-desc">{letter["description"]}</div>
</div>
""",
        unsafe_allow_html=True,
    )
    if st.button("Open Letter 💌", key=key, use_container_width=True):
        st.session_state.selected_letter = letter["title"]
        st.session_state.current_page = "write"
        st.rerun()

def show_menu():
    load_css()
    st.markdown('<h1 class="main-title">💌 Letters to Yourself</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Write what your heart cannot always say aloud.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    for i, letter in enumerate(LETTER_TYPES):
        if i % 2 == 0:
            with col1:
                letter_card(letter, f"letter_{i}")
        else:
            with col2:
                letter_card(letter, f"letter_{i}")

def write_letter():
    load_css()
    if st.button("⬅ Back"):
        st.session_state.current_page = "menu"
        st.rerun()

    selected = st.session_state.get("selected_letter", "Letter to Myself")

    st.markdown(
        f"""
<div class="paper-title">{selected}</div>
<div class="paper-date">{datetime.now().strftime("%d %B %Y")}</div>
<div class="paper-line"></div>
<div class="paper-greeting">Dear Me,</div>
<div class="paper-note">Write honestly. This space belongs only to you.</div>
""",
        unsafe_allow_html=True
    )

    content = st.text_area(
        label="Letter",
        label_visibility="collapsed",
        placeholder="Start writing your thoughts here...",
        height=500
    )

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("💌 Save Letter", use_container_width=True):
            if content.strip():
                save_letter(selected, content)
                st.success("Your letter has been saved ❤️")
            else:
                st.warning("Please write something first.")

    with col2:
        if st.button("📚 My Letters", use_container_width=True):
            st.session_state.current_page = "library"
            st.rerun()

def show_library():
    load_css()
    if st.button("⬅ Back"):
        st.session_state.current_page = "menu"
        st.rerun()

    st.markdown('<h1 class="main-title">📚 My Letters</h1>', unsafe_allow_html=True)
    letters = load_letters()

    if len(letters) == 0:
        st.info("You haven't written any letters yet.")
        return

    for letter in reversed(letters):
        with st.expander(f"{letter['type']} • {letter['date']}"):
            st.text_area(
    "Letter",
    value=letter["content"],
    height=500,
    label_visibility="collapsed",
    key=f"view_{letter['id']}"
)
            st.write("")
            if st.button("🗑 Delete Letter", key=letter["id"]):
                delete_letter(letter["id"])
                st.success("Letter deleted successfully.")
                st.rerun()


# ================= 5. MAIN EXPORT FUNCTION =================
def letters_page():
    """This function is called by app.py"""
    if "current_page" not in st.session_state:
        st.session_state.current_page = "menu"

    if st.session_state.current_page == "write":
        write_letter()
    elif st.session_state.current_page == "library":
        show_library()
    else:
        show_menu()
# ===== End Letters Module =====

REFLECTIONS = {
    "Growth": {
        "title": "🌱 Growth",
        "content": """
There is something no one tells you about growth.

It rarely announces itself. It doesn't come with applause, certainty, or a moment where everything suddenly makes sense. More often than not, growth is so quiet that you mistake it for standing still.

We spend so much of our lives believing that growth should always be visible. We expect ourselves to become stronger, wiser, and more successful in ways that others can notice. But life doesn't always work that way. Sometimes the greatest changes happen where no one can see them—not even you.

Think about a seed buried beneath the soil. If it could speak, it might wonder why nothing is happening. It cannot see the roots stretching deeper, preparing it for the day it finally reaches the sunlight. Yet that hidden work is the very reason it will one day stand tall.

Perhaps you are in that season now.

Maybe you feel left behind because someone else seems to be moving faster. Maybe you compare your journey to people who appear to have everything figured out. But every person walks a different path, and every path has its own pace. Comparing your chapter one to someone else's chapter ten only steals the peace from your own story.

The Bhagavad Gita teaches us that we have control over our actions, but not over the results they produce. There is a quiet freedom in that wisdom. Your responsibility is not to force life to unfold according to your timeline. Your responsibility is simply to show up with sincerity, to do today's work with an honest heart, and to let tomorrow arrive in its own time.

Not every day has to feel meaningful.

Some days, growth looks like learning something new.

Some days, it looks like resting without feeling guilty.

Some days, it looks like choosing kindness when frustration feels easier.

And some days, growth is simply deciding that you will try again tomorrow.

If today feels ordinary, don't mistake ordinary for meaningless. Many of life's most important transformations begin on days that seemed completely unremarkable.

Before you close this page, carry this with you:

"The version of you that survives today is quietly making tomorrow's you possible." 🌿"""
    },

    "Anxiety": {
        "title": "💙Anxiety",
        "content": """There is something no one tells you about anxiety.

It doesn't always look like panic.

Sometimes it looks like smiling while your mind is running a marathon. It looks like rereading the same message five times before sending it. It looks like imagining conversations that haven't happened yet, preparing for problems that may never exist, and carrying the weight of tomorrow before today has even ended.

Anxiety has a way of making you believe that if you think long enough, worry hard enough, or prepare enough, you can protect yourself from pain. But the truth is, anxiety doesn't predict the future—it only borrows peace from the present.

The hardest part is that people around you may not even notice. They see someone who's quiet, responsible, or careful. They don't see the storm that quietly follows you everywhere. And because no one can see it, you begin to wonder if you're simply "too sensitive" or "overreacting."

You're not.

Your mind is trying to protect you. It's just working harder than it needs to.

The Bhagavad Gita speaks of a restless mind. Arjuna admits that controlling the mind seems as difficult as controlling the wind. Krishna doesn't tell him that his struggle is foolish. Instead, he acknowledges that the mind is indeed restless, but gently teaches that with practice and detachment, it can learn to become steady.

That teaching is comforting because it reminds us of something important:

You are not your anxious thoughts.

Thoughts come and go like clouds across the sky. They can be loud, convincing, and frightening, but they are still visitors. They are not your identity.

You don't have to believe every thought just because it appears in your mind.

Sometimes the bravest thing you can do isn't solving every problem your mind creates.

Sometimes it's sitting quietly, taking one slow breath, and saying,

"Not everything my mind whispers is the truth."

Life has never asked you to know what will happen tomorrow.

It has only ever asked you to live today.

And today...

You are here.

You are breathing.

That is enough.

Before you close this page, carry this with you...

"Your mind may tell you a hundred stories about tomorrow, but your heart only has to live one day at a time." 💙"""
    },

    "Failure": {
        "title": "🌊 Failure",
        "content": """There is something no one tells you about failure.

It has a strange way of making you question everything except the thing that actually failed.

You don't just think,
"I failed."

Somehow, your mind quietly changes the sentence into,
"Maybe I am a failure."

And that is where the real pain begins.

Failure rarely hurts because of the event itself. It hurts because we begin to measure our worth by one moment, one mistake, one decision, or one chapter of our lives. We forget that a single page can never tell the story of an entire book.

There are people who never failed because they never dared to try. Their lives may look safer, but safety has never been the same as living. Every meaningful dream asks something from us. Sometimes it asks for patience. Sometimes courage. And sometimes, it asks us to fail before we are ready to succeed.

Imagine learning to walk as a child. You fell hundreds of times before you took your first confident step. Yet no one looked at you and said, "Maybe walking just isn't for you." They smiled, picked you up, and believed that falling was simply part of learning.

Somewhere along the way, we forgot to offer ourselves that same kindness.

The Bhagavad Gita reminds us that our duty is to act with sincerity, not to cling to the outcome. Success and failure are visitors—they come and go. But the courage to keep showing up, even after disappointment, is something no result can take away from you.

Perhaps failure isn't life's way of saying "Stop."

Perhaps it's life asking,
"Will you still believe in your dream when no one is clapping for you?"

The strongest people are not the ones who never fall.

They are the ones who refuse to let one fall decide the rest of their journey.

One failed exam cannot measure your intelligence.

One rejected application cannot measure your potential.

One broken relationship cannot measure your capacity to love.

And one difficult chapter cannot measure the beauty of the chapters that haven't been written yet.

If today feels heavy because something didn't go the way you hoped, allow yourself to grieve. Disappointment deserves compassion, not shame. But don't build your home there. Feel it. Learn from it. Then, when you're ready, stand up once more.

Because the road doesn't end where you stumble.

It only ends where you decide to stop walking.

Before you close this page, carry this with you...

"Failure is an event that visited your life. It was never meant to become your identity." 🌊"""
    },

    "Self-Worth": {
        "title": "🌸 Self-Worth",
        "content": """There is something no one tells you about self-worth.

The world quietly teaches you to earn it.

From the time you're young, you're praised for good grades, achievements, talents, appearance, and success. Slowly, without even realizing it, you begin to believe that your value depends on what you can offer. You start collecting reasons to feel worthy.

"Maybe I'll feel enough when I get that job."

"Maybe when I lose weight."

"Maybe when someone finally chooses me."

"Maybe when people appreciate me."

And so, your worth becomes something you chase instead of something you already possess.

The difficult part is that no achievement ever stays with you forever. A promotion becomes normal. Compliments fade. Applause grows quiet. If your worth depends on these things, you'll spend your whole life searching for something that was never lost.

The Bhagavad Gita reminds us that the true Self is untouched by praise or criticism, success or failure. The soul is not made greater by applause, nor made smaller by rejection. What changes is only the opinion of the world—not your true nature.

Think about the sun.

Clouds may hide it for days, but no one believes the sun has disappeared. It is still there, shining exactly as it always has been.

Perhaps your worth is like that.

Pain may cover it.

Failure may hide it.

Rejection may make you question it.

But none of these things have the power to take it away.

You were never born needing to prove that you deserve love, kindness, or respect. You deserved them the day you entered this world, long before you achieved anything.

So be careful how you speak to yourself.

You would never tell a child that they are worthless because they made a mistake.

Don't become the voice to yourself that you would never be to someone you love.

There will always be people who misunderstand you.

Some will leave.

Some won't appreciate your kindness.

Some will never see your value.

But someone's inability to recognise your light has never meant you were born without it.

The mirror can only show your reflection.

It can never measure your worth.

Before you close this page, carry this with you...

"Your worth was never something you had to earn. It is something you were born with, long before the world taught you to doubt it." 🌸"""
    },

    "Rest": {
        "title": "🌙 Rest",
        "content": """

**There is something no one tells you about rest.**

Rest is not something you earn after exhaustion.

Somewhere along the way, many of us began believing that we must constantly be doing something to deserve a moment of peace. If we're resting, we should feel guilty. If we're not busy, we feel like we're falling behind.

So even when our body sits still, our mind keeps working.

Thinking.

Planning.

Regretting.

Worrying.

It is possible to lie in bed all night and never truly rest.

The world celebrates people who never stop. We admire the ones who work through the night, skip meals, ignore their tiredness, and keep pushing no matter what. But even the strongest river pauses in quiet lakes before continuing its journey.

Why should human beings be expected to do less?

The Bhagavad Gita teaches the beauty of balance. Krishna does not praise extremes. Instead, he says that a life of harmony belongs to the one who is moderate in eating, sleeping, working, and recreation. Balance, not excess, is what leads to peace.

That wisdom feels surprisingly modern.

Because burnout isn't always caused by doing too much.

Sometimes it's caused by believing that you are never allowed to stop.

Your body has been carrying you since the day you were born.

It has stayed with you through every celebration, every disappointment, every sleepless night, every illness, every dream.

Perhaps it deserves your kindness more than your criticism.

Rest is not laziness.

A tree in winter isn't dead because it has no leaves.

It is gathering strength for another spring.

Maybe you are in a season like that.

A season where your soul needs silence more than productivity.

Where healing matters more than proving yourself.

Where slowing down is not giving up—it is preparing to continue.

You don't have to fill every empty moment.

You don't have to answer every message immediately.

You don't have to carry the expectation that your value depends on how busy you appear.

Sometimes the most meaningful thing you can do today is simply pause.

Not because you've earned it.

But because you're human.

**Before you close this page, carry this with you...**

**"You are not a machine created to produce. You are a human being created to live."** 🌙
"""
    },

    "Relationships": {
        "title": "❤️ Relationships",
        "content": """There is something no one tells you about relationships.

Not everyone who enters your life is meant to stay forever.

That thought can feel heartbreaking.

We meet people believing they'll be there through every chapter of our lives. We imagine futures with them, build routines around them, and slowly begin to think of them as permanent. Then one day, life changes. Someone leaves. Someone grows distant. Someone becomes a memory.

And we're left wondering what we did wrong.

But not every goodbye is a punishment.

Sometimes it's simply the way life makes room for who you're becoming.

The hardest part about losing someone isn't always their absence.

It's learning how to carry all the love you still have for them.

The conversations you'll never finish.

The jokes only the two of you understood.

The habit of reaching for your phone to tell them something before remembering that things are different now.

Some people leave without hurting us.

Others leave while breaking our hearts.

Yet every person changes us in some way.

The Bhagavad Gita reminds us that everything in this world is temporary. Every meeting has a parting, every beginning has an ending. This isn't meant to make us fearful of love—it is meant to teach us to cherish the people beside us while they are here, without trying to possess them forever.

Love has never meant ownership.

It has always meant presence.

If someone truly cares for you, don't wait for a special occasion to tell them.

If someone made your life brighter, let them know.

Kind words spoken today are worth more than regrets carried tomorrow.

And if someone has walked away...

Let yourself grieve.

Missing someone is not weakness.

It is proof that your heart had the courage to care.

Some relationships are for a lifetime.

Others are only for a season.

Neither is meaningless.

Even the people who stayed for a short while may have taught you lessons that remain for years.

One day, you'll look back and realise that every hello and every goodbye quietly shaped the person you became.

Perhaps the goal isn't to make every relationship last forever.

Perhaps the goal is to leave every relationship with more kindness than you brought into it.

Because people may forget your words.

They may forget the dates and details.

But they rarely forget how you made them feel.

Before you close this page, carry this with you...

"Some people are chapters, some are entire books—but every person who loved you honestly became a sentence in your story." ❤️"""
    },

    "Purpose": {
        "title": "🌅 Purpose",
        "content": """
**There is something no one tells you about purpose.**

You don't always find it.

Sometimes, it quietly finds you.

Many of us grow up believing that one day we'll suddenly discover our purpose—as if life will hand us a map, point to a destination, and everything will finally make sense.

But for most people, life doesn't unfold that way.

Purpose isn't usually found in a single grand moment.

It's discovered in countless ordinary ones.

A conversation that changes someone's day.

A skill you slowly become good at.

A mistake that teaches you compassion.

A dream you almost gave up on.

Piece by piece, life reveals itself.

The problem is that we often compare our beginning to someone else's destination. We see people who seem confident, successful, and certain of where they're going, and we quietly ask ourselves,

*"Why haven't I figured it out yet?"*

But no flower blooms because another flower has already blossomed.

Each one opens in its own season.

The Bhagavad Gita teaches the idea of **Svadharma**—your own path. Krishna encourages Arjuna not to abandon his own journey in favour of someone else's, reminding him that it is better to walk your own imperfect path than to perfectly imitate another person's life.

There is something deeply freeing about that.

You don't have to become someone else to live a meaningful life.

You only have to become more fully yourself.

Perhaps purpose isn't hiding somewhere far away.

Perhaps it's already growing in the things that make your heart feel alive.

The moments when time disappears because you're completely present.

The kindness you naturally offer.

The curiosity you keep returning to.

The work that feels meaningful, even when no one is watching.

Those aren't accidents.

They're quiet clues.

And if today you still don't know what your purpose is...

That's okay.

You are not behind.

You are still becoming.

No one is born with the whole story already written.

Every sunrise begins in darkness.

Every river begins as a small stream.

Every great tree was once a seed that looked insignificant.

Your life is no different.

You don't need to have every answer.

You only need enough courage to take the next honest step.

One day, you'll look back and realise that the path you were desperately trying to find...

...was the one you were creating all along.

**Before you close this page, carry this with you...**

**"Purpose is rarely discovered all at once. 
More often, it is quietly built by the choices you make every single day."** 🌅
"""
    },

    "Hope": {
        "title": "✨ Hope",
        "content": """Hope isn't always a huge feeling that suddenly makes everything okay. Sometimes it's much quieter than that.

It's waking up on a difficult day and still deciding to get through it. It's believing that today's version of your life isn't necessarily the final version. You don't need to know exactly where you're going to take the next step.

Some days, hope looks like trying again. Some days, it looks like resting without giving up. And sometimes, it simply means telling yourself, “I don't have to figure everything out today.”

You may not see the change while you're living through it. A chapter can feel endless when you're still inside it. But life has a strange way of moving, even when you feel stuck.

So don't demand certainty from yourself. Don't compare your chapter to someone else's highlight reel. Keep a little space open for things you haven't seen yet — people you haven't met, places you haven't reached, versions of yourself you haven't become.

Maybe things aren't okay yet. That's different from saying they'll never be.

The Bhagavad Gita reminds us that we have control over our actions, but not over the results. Sometimes hope begins there — not from knowing that everything will work out exactly as we want, but from trusting ourselves to keep doing what is right, one step at a time.

🌷 You are allowed to hope, even without proof."""
    }
}



# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Mental Wellness Support",
    page_icon="🧠",
    layout="wide"
)

# ---------------- GEMINI ----------------
genai.configure(api_key=os.getenv("PUBIC KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------- CREATE HISTORY FILE ----------------
if not os.path.exists("history.csv"):
    df = pd.DataFrame(
        columns=[
            "Date",
            "User Input",
            "Mood",
            "Sentiment Score"
        ]
    )
    df.to_csv("history.csv", index=False)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp{
background:radial-gradient(circle at top,#35104d,#12061d,#090312);
color:#c7b8dd;
}

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.main-title{
text-align:center;
font-size:58px;
font-weight:700;
color:#d8b4fe;
text-shadow:0 0 10px rgba(184,76,255,.4);
}

.sub-title{
text-align:center;
font-size:22px;
color:#e5d9ff;
margin-bottom:30px;
}

.glass{
background:#21152d;
backdrop-filter:blur(18px);
border:1px solid rgba(255,255,255,.15);
border-radius:20px;
padding:18px;
box-shadow:0 0 25px rgba(168,85,247,.4);
margin-bottom:20px;
}

[data-testid="stTextArea"] textarea{
background:#2b1d3a !important;
color:white !important;
caret-color:white !important;
border:1px solid #9d4edd !important;
border-radius:15px !important;
font-size:18px !important;
}

[data-testid="stTextArea"] textarea::placeholder{
color:#b8a7d9 !important;
}

/* ================= HOME CARDS ================= */

.stButton > button {
    width: 100%;
    height: 145px;
    background: rgba(255, 130, 190, 0.025);
    border: 1px solid rgba(232, 170, 210, 0.38);
    border-radius: 14px;
    color: #F8EFFF;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 19px !important;
    font-weight: 600 !important;
    line-height: 1.55 !important;
    box-shadow:
        0 0 8px rgba(235, 150, 200, 0.07),
        inset 0 0 10px rgba(235, 150, 200, 0.025);
    transition: all 0.25s ease;
}

.stButton > button p {
    font-family: Georgia, "Times New Roman", serif !important;
    font-size: 19px !important;
    font-weight: 600 !important;
    line-height: 1.55 !important;
    color: #F8EFFF !important;
    white-space: normal;
}

.stButton > button:hover {
    background: rgba(255, 130, 190, 0.045);
    border-color: rgba(245, 185, 220, 0.65);
    box-shadow:
        0 0 10px rgba(235, 150, 200, 0.14),
        0 0 20px rgba(235, 150, 200, 0.06),
        inset 0 0 12px rgba(235, 150, 200, 0.035);
    transform: translateY(-2px);
}


/* click */

.stButton > button:active {
    background: rgba(255, 130, 190, 0.025);
    transform: translateY(1px);
}


/* text */

.stButton > button p {
    line-height: 1.6;
    white-space: normal;
}

[data-testid="stSidebar"]{
background:#12061d;
border-right:1px solid #5b21b6;
}

[data-testid="stSidebar"] *{
color:white;
}

[data-testid="metric-container"]{
background:rgba(255,255,255,.06);
border-radius:18px;
padding:18px;
box-shadow:0 0 20px rgba(168,85,247,.4);
}

.stSuccess{
background:rgba(16,185,129,.2);
border-radius:15px;
}

.stInfo{
background:rgba(59,130,246,.2);
border-radius:15px;
}

.stWarning{
background:rgba(234,179,8,.2);
border-radius:15px;
}
.feature-card{
padding:25px;
border-radius:20px;
margin-bottom:20px;
color:white;
box-shadow:0 8px 20px rgba(0,0,0,0.25);
transition:0.3s;
}

.feature-card:hover{
transform:translateY(-6px);
box-shadow:0 0 25px rgba(255,255,255,.35);
}

.feature-card{
background:rgba(255,255,255,0.06);
border:1px solid rgba(255,255,255,.12);
border-radius:18px;
padding:22px;
margin-bottom:18px;
transition:0.3s;
cursor:pointer;
}

.feature-card:hover{
background:rgba(123,47,247,.18);
border:1px solid #9d4edd;
transform:translateY(-4px);
box-shadow:0 0 18px rgba(157,78,221,.35);
}

.feature-card h2{
margin-bottom:10px;
color:white;
font-size:30px;
}

.feature-card p{
color:#d8d8d8;
font-size:17px;
}

/* Keep the sidebar permanently visible */
[data-testid="stSidebarCollapseButton"] {
    display: none !important;
}

[data-testid="collapsedControl"] {
    display: none !important;
}

</style>

""", unsafe_allow_html=True)

# ---------------- NAVIGATION CALLBACK ----------------
def go_home():
    st.session_state.menu = "🏠 Home"


def navigate(page):
    st.session_state.menu = page

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("Mental Wellness")

    menu = st.radio(
    "Navigation",
    [
        "🏠 Home",
        "💭 Express Yourself",
        "🧠 Untangle My Mind",
        "🔎 Reality vs Thoughts",
        "❤️ Reflections",
        "💌 Letters to Yourself",
        "📚 Comfort Library",
        "🌿 One Moment",
        "👤 Profile"
    ],
    key="menu"
)
    st.markdown("---")

    st.markdown("---")

    # Visual illustration is rendered in an isolated HTML component,
    # so Streamlit cannot display the HTML source code.
    components.html("""
<style>
html, body {
    margin: 0;
    padding: 0;
    background: transparent;
    overflow: hidden;
}

.scene {
    position: relative;
    width: 100%;
    height: 280px;
    background: transparent;
}

/* soft glow at the top */
.glow {
    position: absolute;
    left: 40%;
    top: 55px;
    transform: translate(-50%, -50%);
    width: 150px;
    height: 110px;
    border-radius: 50%;
    background: rgba(190, 125, 255, 0.08);
    filter: blur(25px);
}

/* ---------------- HEARTS ---------------- */

.heart {
    position: absolute;
    color: #e99ab8;
    text-shadow: 0 0 12px rgba(240, 160, 210, .45);
    z-index: 5;
}

.h1 {
    left: 21%;
    top: 28px;
    font-size: 16px;
    transform: rotate(-15deg);
}

.h2 {
    left: 68%;
    top: 20px;
    font-size: 19px;
    transform: rotate(14deg);
}

.h3 {
    left: 76%;
    top: 78px;
    font-size: 13px;
    transform: rotate(-8deg);
}

.h4 {
    left: 17%;
    top: 82px;
    font-size: 13px;
    transform: rotate(12deg);
}

.h5 {
    left: 58%;
    top: 55px;
    font-size: 12px;
}

/* ---------------- SPARKLES ---------------- */

.spark {
    position: absolute;
    color: #e7c8ff;
    text-shadow: 0 0 10px rgba(230,190,255,.7);
    z-index: 4;
}

.s1 {
    left: 29%;
    top: 18px;
    font-size: 13px;
}

.s2 {
    right: 22%;
    top: 57px;
    font-size: 10px;
}

.s3 {
    left: 27%;
    top: 69px;
    font-size: 9px;
}

/* ---------------- ENVELOPE ---------------- */

.envelope {
    position: absolute;
    left: 40%;
    top: 82px;
    transform: translateX(-50%);
    width: 165px;
    height: 105px;
}

/* envelope body */
.envelope-back {
    position: absolute;
    left: 0;
    top: 20px;
    width: 165px;
    height: 85px;

    background: rgba(83, 50, 105, .68);

    border: 2px solid rgba(215, 165, 230, .68);
    border-radius: 5px;

    box-shadow:
        0 8px 22px rgba(40,15,55,.20),
        0 0 18px rgba(190,130,230,.08);
}

/* open flap */
.flap {
    position: absolute;
    left: 1px;
    top: 20px;

    width: 161px;
    height: 70px;

    background: rgba(105, 65, 128, .72);

    border: 2px solid rgba(215, 165, 230, .68);

    clip-path: polygon(
        0 0,
        50% 82%,
        100% 0
    );

    z-index: 3;
}

/* heart sitting inside the envelope */
.main-heart {
    position: absolute;
    left: 50%;
    top: 52px;

    transform: translateX(-50%);

    color: #ee9ab7;
    font-size: 27px;

    text-shadow:
        0 0 12px rgba(245,150,190,.45),
        0 0 25px rgba(220,150,255,.20);

    z-index: 6;
}

/* subtle envelope bottom line */
.envelope::after {
    content: "";
    position: absolute;

    left: 8px;
    right: 8px;
    bottom: -3px;

    height: 1px;

    background: rgba(215,165,230,.35);
    border-radius: 50%;
}

/* ---------------- SMALL FLOATING HEARTS ---------------- */

.floating-heart {
    position: absolute;
    color: #d989a9;
    font-size: 11px;
    opacity: .8;
}

.fh1 {
    left: 30%;
    top: 106px;
}

.fh2 {
    left: 57%;
    top: 92px;
}

.fh3 {
    left: 70%;
    top: 125px;
}
</style>

<div class="scene">

    <div class="glow"></div>

    <!-- floating hearts -->
    <div class="heart h1">♥</div>
    <div class="heart h2">♥</div>
    <div class="heart h3">♥</div>
    <div class="heart h4">♥</div>
    <div class="heart h5">♡</div>

    <!-- sparkles -->
    <div class="spark s1">✦</div>
    <div class="spark s2">✧</div>
    <div class="spark s3">·</div>

    <!-- envelope -->
    <div class="envelope">

        <div class="envelope-back"></div>

        <div class="flap"></div>

        <div class="main-heart">♥</div>

    </div>

    <!-- tiny hearts around envelope -->
    <div class="floating-heart fh1">♡</div>
    <div class="floating-heart fh2">♥</div>
    <div class="floating-heart fh3">♡</div>

</div>
""", height=290, scrolling=False)

# ---------------- HEADER ----------------



# ---------------- INPUT ----------------
# ---------------- HOME ----------------
if menu == "🏠 Home":

    st.markdown("""
    <h1 class="main-title">🧠 Mental Wellness Support</h1>
    <p class="sub-title">Understand. Reflect. Heal. Grow.</p>
    """, unsafe_allow_html=True)

        # Arrange the home features in balanced rows.

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "💭 Express Yourself\n\nTalk.",
            key="home_express",
            use_container_width=True,
            on_click=navigate,
            args=("💭 Express Yourself",)
        ):
            st.rerun()

    with col2:
        if st.button(
            "💌 Letters to Yourself\n\nWrite.",
            key="home_letters",
            use_container_width=True,
            on_click=navigate,
            args=("💌 Letters to Yourself",)
        ):
            st.rerun()

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "🧠 Untangle My Mind\n\nClear.",
            key="home_untangle",
            use_container_width=True,
            on_click=navigate,
            args=("🧠 Untangle My Mind",)
        ):
            st.rerun()

    with col2:
        if st.button(
            "🌿 One Moment\n\nAttention.",
            key="home_one_moment",
            use_container_width=True,
            on_click=navigate,
            args=("🌿 One Moment",)
        ):
            st.rerun()

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "🔎 Reality vs Thoughts\n\nCheck.",
            key="home_reality",
            use_container_width=True,
            on_click=navigate,
            args=("🔎 Reality vs Thoughts",)
        ):
            st.rerun()

    with col2:
        if st.button(
            "📚 Comfort Library\n\nBreathe.",
            key="home_library",
            use_container_width=True,
            on_click=navigate,
            args=("📚 Comfort Library",)
        ):
            st.rerun()

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "❤️ Reflections\n\nRead.",
            key="home_reflections",
            use_container_width=True,
            on_click=navigate,
            args=("❤️ Reflections",)
        ):
            st.rerun()

    with col2:
        if st.button(
            "👤 Profile\n\nYour space.",
            key="home_profile",
            use_container_width=True,
            on_click=navigate,
            args=("👤 Profile",)
        ):
            st.rerun()

        # Quote
    st.markdown("""
<div style="
text-align:center;
margin-top:25px;
padding:15px;
color:#b89ce5;
font-size:18px;
font-style:italic;
">
🌸 Be as kind to yourself as you are to others.
</div>
""", unsafe_allow_html=True)

    st.stop()
# ---------------- UNTANGLE MY MIND ----------------
# ---------------- UNTANGLE MY MIND ----------------
if menu == "🧠 Untangle My Mind":

    # ---------- PAGE STYLING ----------
    st.markdown("""
    <style>

    /* Page spacing */
    .untangle-page {
        max-width: 900px;
        margin: 0 auto;
        padding: 10px 25px 50px 25px;
    }

    /* Header */
    .untangle-title {
        text-align: center;
        margin-top: 5px;
        margin-bottom: 6px;
    }

    .untangle-title h1 {
        font-family: Georgia, serif;
        font-size: 42px;
        margin: 0;
        color: #f4dfff;
        text-shadow: 0 0 18px rgba(238, 151, 205, 0.18);
    }

    .untangle-subtitle {
        text-align: center;
        color: #cdb8dc;
        font-size: 15px;
        margin: 8px auto 28px auto;
        max-width: 650px;
        line-height: 1.6;
    }

    /* Small hint */
    .untangle-hint {
        text-align: center;
        color: #e7b8d5;
        font-size: 13px;
        margin-bottom: 10px;
        opacity: 0.9;
    }

    /* Text area */
   /* Text area */
div[data-testid="stTextArea"] textarea {
    background: #12091d !important;
    color: #f8efff !important;
    border: 1px solid rgba(225, 135, 195, 0.45) !important;
    border-radius: 16px !important;
    padding: 17px !important;
    font-size: 16px !important;
    line-height: 1.6 !important;

    box-shadow:
        inset 0 0 18px rgba(0, 0, 0, 0.22),
        0 0 10px rgba(225, 135, 195, 0.05) !important;
}

/* Placeholder text */
div[data-testid="stTextArea"] textarea::placeholder {
    color: #b9a5c5 !important;
    opacity: 1 !important;
}

/* When clicked */
div[data-testid="stTextArea"] textarea:focus {
    background: #12091d !important;
    border: 1px solid rgba(239, 151, 205, 0.65) !important;

    box-shadow:
        0 0 14px rgba(225, 135, 195, 0.10),
        inset 0 0 18px rgba(0, 0, 0, 0.22) !important;
}

    div[data-testid="stTextArea"] textarea:focus {
        border: 1px solid rgba(239, 157, 205, 0.75) !important;
        box-shadow:
            0 0 18px rgba(232, 133, 194, 0.13) !important;
    }

    /* Main button */
    .untangle-button button {
        border-radius: 14px !important;
        border: 1px solid rgba(238, 158, 211, 0.5) !important;
        background: linear-gradient(
            135deg,
            rgba(96, 43, 126, 0.75),
            rgba(67, 30, 91, 0.75)
        ) !important;
        color: #fff5ff !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        padding: 12px 20px !important;
        transition: all 0.25s ease !important;
        box-shadow: 0 0 12px rgba(225, 137, 199, 0.08) !important;
    }

    .untangle-button button:hover {
        border-color: rgba(247, 174, 218, 0.85) !important;
        box-shadow: 0 0 20px rgba(229, 135, 198, 0.18) !important;
        transform: translateY(-1px);
    }

    /* Result cards */
    .mind-card {
        background: rgba(25, 10, 39, 0.58);
        border: 1px solid rgba(224, 143, 198, 0.28);
        border-radius: 18px;
        padding: 22px 24px;
        min-height: 145px;
        margin-top: 16px;
        box-shadow:
            0 0 18px rgba(212, 115, 183, 0.055),
            inset 0 0 18px rgba(255,255,255,0.012);
    }

    .mind-card:hover {
        border-color: rgba(238, 159, 210, 0.48);
    }

    .mind-card-title {
        font-size: 18px;
        font-weight: 600;
        color: #f1c9e3;
        margin-bottom: 10px;
    }

    .mind-card-text {
        color: #ddd0e7;
        font-size: 15px;
        line-height: 1.65;
    }

    /* Small divider */
    .soft-divider {
        width: 70px;
        height: 2px;
        margin: 22px auto;
        background: rgba(232, 150, 203, 0.45);
        border-radius: 10px;
    }

    </style>
    """, unsafe_allow_html=True)


    # ---------- PAGE ----------
    st.markdown('<div class="untangle-page">', unsafe_allow_html=True)

    # Back button
    if st.button(
    "← Back to Home",
    key="untangle_back",
    on_click=go_home
):
       st.rerun()

    # Header
    st.markdown("""
    <div class="untangle-title">
        <h1>🧠 Untangle My Mind</h1>
    </div>

    

    <div class="untangle-hint">
        ✨ Don't organize your thoughts first. Just write them exactly as they come.
    </div>
    """, unsafe_allow_html=True)


    # Input
    untangle_input = st.text_area(

    "💭 What's on your mind?",

    height=180,

    placeholder=(
        "Write everything on your mind in one messy paragraph...\n\n"
        "We'll untangle it into 3 parts — what you're feeling, "
        "what's really happening, and what you can do next."
    ),

    key="untangle_input"
)


    # Button
    st.markdown('<div class="untangle-button">', unsafe_allow_html=True)

    analyze_clicked = st.button(
        "🧠 Untangle My Thoughts",
        use_container_width=True,
        key="untangle_button"
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # ---------- AI PROCESSING ----------
    if analyze_clicked:

        if not untangle_input.strip():
            st.warning("Write a few thoughts first — messy is completely okay. 🌱")
            st.stop()

        with st.spinner("Making sense of your thoughts..."):

            untangle_response = model.generate_content(f"""
You are a warm and practical mental-wellness companion.

The user wrote:
{untangle_input}

Gently organize their thoughts into exactly these four sections:

### 💭 What's on your mind
Briefly identify the main worries, feelings, or thoughts you understood.
Keep it to 1–2 short sentences.

### 🎯 What you can control
Give 1–2 things they can realistically influence.
Be specific to their situation.

### ☁️ What you don't need to carry right now
Point out worries, assumptions, or outcomes that are outside their control.
Be gentle and do not dismiss real problems.

### 🌱 One tiny next step
Give EXACTLY ONE practical action they can do in 5–15 minutes.
It must directly relate to what they wrote.

IMPORTANT:
- Keep every section short.
- Do NOT give generic advice such as "stay positive", "believe in yourself",
  "everything will be okay", "drink water", or "take deep breaths".
- Make the advice specific and useful.
- Do not diagnose.
- Do not ask questions.
""")


        # ---------- PARSE RESPONSE ----------
        response_text = untangle_response.text

        sections = {
            "💭 What's on your mind": "",
            "🎯 What you can control": "",
            "☁️ What you don't need to carry right now": "",
            "🌱 One tiny next step": ""
        }

        current_section = None

        for line in response_text.splitlines():

            clean_line = line.strip()

            if clean_line.startswith("###"):
                heading = clean_line.replace("###", "").strip()

                for key in sections:
                    if key in heading:
                        current_section = key
                        break

            elif current_section and clean_line:
                sections[current_section] += clean_line + " "


        # ---------- RESULTS ----------
        st.markdown("""
        <div style="
            text-align:center;
            margin-top:30px;
            margin-bottom:5px;
        ">
            <div style="
                color:#f0c9e3;
                font-size:24px;
                font-family:Georgia, serif;
            ">
                Your thoughts, a little clearer 🌿
            </div>

            <div style="
                color:#bca9c8;
                font-size:13px;
                margin-top:5px;
            ">
                You don't have to solve everything at once.
            </div>
        </div>
        """, unsafe_allow_html=True)


        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"""
            <div class="mind-card">
                <div class="mind-card-title">
                    💭 What's on your mind
                </div>
                <div class="mind-card-text">
                    {sections["💭 What's on your mind"].strip()}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="mind-card">
                <div class="mind-card-title">
                    🎯 What you can control
                </div>
                <div class="mind-card-text">
                    {sections["🎯 What you can control"].strip()}
                </div>
            </div>
            """, unsafe_allow_html=True)


        col3, col4 = st.columns(2)

        with col3:
            st.markdown(f"""
            <div class="mind-card">
                <div class="mind-card-title">
                    ☁️ What you don't need to carry
                </div>
                <div class="mind-card-text">
                    {sections["☁️ What you don't need to carry right now"].strip()}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
            <div class="mind-card">
                <div class="mind-card-title">
                    🌱 One tiny next step
                </div>
                <div class="mind-card-text">
                    {sections["🌱 One tiny next step"].strip()}
                </div>
            </div>
            """, unsafe_allow_html=True)


    st.markdown('</div>', unsafe_allow_html=True)

    st.stop()

# ---------------- REALITY VS THOUGHTS ----------------
if menu == "🔎 Reality vs Thoughts":

    st.markdown("""
    <style>
    .reality-page {
        max-width: 920px;
        margin: 0 auto;
        padding: 8px 25px 50px 25px;
    }

    .reality-title {
        text-align: center;
        margin: 4px 0 4px 0;
    }

    .reality-title h1 {
        font-family: Georgia, serif;
        font-size: 42px;
        margin: 0;
        color: #f4dfff;
        text-shadow: 0 0 18px rgba(238,151,205,.18);
    }

    .reality-subtitle {
        text-align: center;
        color: #cdb8dc;
        font-size: 15px;
        line-height: 1.55;
        max-width: 680px;
        margin: 8px auto 24px auto;
    }

    .reality-card {
        background: #12091d;
        border: 1px solid rgba(225,135,195,.28);
        border-radius: 18px;
        padding: 22px 24px;
        margin: 14px 0;
        box-shadow: 0 0 16px rgba(225,135,195,.045);
    }

    .reality-card:hover {
        border-color: rgba(239,151,205,.60);
        box-shadow: 0 0 20px rgba(225,135,195,.09);
    }

    .thought-label {
        color: #c9b4d4;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin-bottom: 7px;
    }

    .thought-text {
        color: #f7effb;
        font-size: 18px;
        line-height: 1.5;
        margin-bottom: 16px;
    }

    .reality-label {
        color: #f0a6ca;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin-bottom: 7px;
    }

    .reality-text {
        color: #e2d5e9;
        font-size: 16px;
        line-height: 1.6;
    }

    .reality-tag {
        display: inline-block;
        margin-top: 15px;
        padding: 5px 10px;
        border-radius: 20px;
        background: rgba(225,135,195,.08);
        border: 1px solid rgba(225,135,195,.18);
        color: #d7b9d4;
        font-size: 11px;
        letter-spacing: .7px;
    }

    .reality-intro {
        text-align: center;
        color: #e7b8d5;
        font-size: 14px;
        margin: 10px 0 20px 0;
    }

    .reality-filter button {
        border-radius: 12px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="reality-page">', unsafe_allow_html=True)

    if st.button("← Back to Home", key="reality_back", on_click=navigate, args=("🏠 Home",)):
        st.rerun()

    st.markdown("""
    <div class="reality-title">
        <h1>🔎 Reality Check</h1>
    </div>
    <div class="reality-subtitle">
        Your mind said it. That doesn't automatically make it true.
        Here are the everyday thoughts that deserve a second look.
    </div>
    <div class="reality-intro">
        🔥 No sugar-coating. No fake positivity. Just a stronger way to look at it.
    </div>
    """, unsafe_allow_html=True)

    reality_items = [
        (
            "“Everyone is ahead of me.”",
            "And? Their timeline isn't your assignment. Stop using someone else's progress as evidence against yourself.",
            "COMPARISON TRAP"
        ),
        (
            "“Everyone is judging me.”",
            "Let them. You're not running your life by committee.",
            "APPROVAL TRAP"
        ),
        (
            "“They haven't replied, so they're angry with me.”",
            "You know they haven't replied. Everything after that is a story your brain wrote.",
            "MIND-READING"
        ),
        (
            "“I embarrassed myself.”",
            "You survived. Nobody is holding a three-hour meeting about your awkward moment. Move on.",
            "SPOTLIGHT EFFECT"
        ),
        (
            "“I'm not good enough.”",
            "That's not a fact. That's an exhausted brain making a dramatic announcement.",
            "FEELING ≠ FACT"
        ),
        (
            "“I wasted too much time.”",
            "Maybe you did. So what? You can't edit yesterday. You can stop wasting today.",
            "PAST TRAP"
        ),
        (
            "“I have to make everyone happy.”",
            "Absolutely not. You're a person, not a customer-service department.",
            "PEOPLE-PLEASING"
        ),
        (
            "“If I fail, I've ruined everything.”",
            "You may have messed up one attempt. Your mind doesn't get to upgrade one event into your entire identity.",
            "CATASTROPHIZING"
        ),
        (
            "“I need to have my whole future figured out.”",
            "No. You need enough clarity for the next decision. The rest can reveal itself while you move.",
            "FUTURE TRAP"
        ),
        (
            "“If I can't do it perfectly, I shouldn't start.”",
            "Perfectionism loves a delayed start. A messy beginning is still a beginning.",
            "PERFECTIONISM"
        ),
        (
            "“I should be over this by now.”",
            "Who gave your healing a deadline? You don't need to rush just because your calendar says you should.",
            "HEALING DEADLINE"
        ),
        (
            "“They don't like me, so something is wrong with me.”",
            "Someone's opinion is information about their preference—not a final verdict on your worth.",
            "PERSONALIZATION"
        ),
        (
            "“If I feel it strongly, it must be true.”",
            "The feeling is real. The conclusion still needs evidence.",
            "FEELING ≠ FACT"
        ),
        (
            "“I missed my chance.”",
            "Maybe that particular chance passed. That doesn't mean your only path passed with it.",
            "ALL-OR-NOTHING"
        ),
        (
            "“I need motivation before I start.”",
            "Sometimes motivation shows up after you begin. Stop waiting for the feeling and make the first move.",
            "ACTION FIRST"
        ),
    ]

        # Show every thought together — no filters, no choosing.
    visible_items = reality_items

    for thought, reality, tag in visible_items:

        card_html = f"""<div class="reality-card">
<div class="thought-label">🧠 YOUR MIND SAYS</div>
<div class="thought-text">{thought}</div>

<div class="reality-label">🔥 REALITY CHECK</div>
<div class="reality-text">{reality}</div>

<div class="reality-tag">{tag}</div>
</div>"""

        # Render each card INSIDE the loop so every reality check appears.
        st.markdown(card_html.strip(), unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

if menu == "❤️ Reflections":

    if "reflection" not in st.session_state:
        st.session_state.reflection = None

    # Back button changes depending on where you are
    if st.session_state.reflection is not None:

        if st.button("⬅ Back to Reflections"):
            st.session_state.reflection = None
            st.rerun()

    else:

        if st.button("⬅ Back to Home", on_click=go_home):
            st.rerun()

    st.title("❤️ Reflections")

    if "reflection" not in st.session_state:
        st.session_state.reflection = None

    topics = [
        ("🌱 Growth", "Growth"),
        ("💙 Anxiety", "Anxiety"),
        ("🌊 Failure", "Failure"),
        ("🌸 Self-Worth", "Self-Worth"),
        ("🌙 Rest", "Rest"),
        ("❤️ Relationships", "Relationships"),
        ("🌅 Purpose", "Purpose"),
        ("✨ Hope", "Hope")
    ]

    if st.session_state.reflection is None:

        col1, col2 = st.columns(2)

        for i, (label, key) in enumerate(topics):

            with (col1 if i % 2 == 0 else col2):

                if st.button(label, use_container_width=True):
                    st.session_state.reflection = key
                    st.rerun()

    else:

        data = REFLECTIONS[st.session_state.reflection]


        st.subheader(data["title"])
        st.markdown(data["content"])

    st.stop()
if menu == "📚 Comfort Library":
    if st.button("⬅ Back to Home", on_click=go_home):
        st.rerun()

    comfort_library_page()
    st.stop()   
if menu == "💌 Letters to Yourself":
    if st.button("⬅ Back to Home", on_click=go_home):
        st.rerun()

    letters_page()
    st.stop()
if menu == "🌿 One Moment":
    if st.button("⬅ Back to Home", on_click=go_home):
        st.rerun()

    one_moment_page()
    st.stop()

if menu == "👤 Profile":
    if st.button("⬅ Back to Home", on_click=go_home):
        st.rerun()

    st.title("👤 Profile")
    st.markdown("""
    <div class="glass">
        <h2>🌿 Your Space</h2>
        <p>
            This space is for you. Your wellness journey is personal,
            and there is no need to have everything figured out.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ---------------- EXPRESS YOURSELF ----------------
if menu == "💭 Express Yourself":
    st.button("⬅ Back to Home", on_click=go_home)
    # Continue into the existing Express Yourself UI below.

user_input = st.text_area(
    "💬 How are you feeling today?",
    height=180,
    placeholder="Example: I feel stressed because of exams..."
)


# ---------------- BUTTON ----------------

if st.button("🧠 Analyze My Mood", use_container_width=True):

    if user_input.strip() == "":
        st.error("Please enter something first.")
        st.stop()

    analysis = TextBlob(user_input)

    polarity = analysis.sentiment.polarity

    text = user_input.lower()

    response = model.generate_content(f"""
User Message:
{user_input}

Sentiment Score:
{round(polarity,2)}

You are a warm and empathetic wellness companion.

Respond like a caring friend.

Acknowledge the user's feelings.

Give comforting words.

Suggest ONE practical activity.

Do not ask follow-up questions.

Keep the response under 120 words.
""")
        # ---------------- RESPONSE SECTION ----------------

    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:

        st.markdown(
            f"""
<div class="glass">

<h2>💙 AI Wellness Response</h2>

{response.text}

</div>
""",
            unsafe_allow_html=True,
        )

    with col2:

        st.metric("📊 Sentiment Score", round(polarity, 2))

        mood = "Neutral"

        stress_words = [
            "stress", "stressed", "exam", "pressure",
            "overwhelmed", "anxious", "worried", "tension"
        ]

        lonely_words = [
            "lonely", "alone", "isolated",
            "ignored", "left out"
        ]

        happy_words = [
            "happy", "joy", "joyful", "great",
            "awesome", "fantastic", "wonderful",
            "grateful", "cheerful", "excited"
        ]

        sad_words = [
            "sad", "cry", "crying",
            "heartbroken", "upset",
            "depressed", "miserable",
            "hopeless"
        ]

        if any(word in text for word in stress_words):

            mood = "Stress"

            st.warning("### 😟 Stress")

            tips = [
                "🧘 Take a 10-minute break",
                "💧 Drink some water",
                "🎯 Focus on one task at a time"
            ]

        elif any(word in text for word in lonely_words):

            mood = "Loneliness"

            st.warning("### 😔 Loneliness")

            tips = [
                "📞 Talk to a friend or family member",
                "📖 Write your thoughts in a journal",
                "🎨 Spend time on a hobby"
            ]

        elif any(word in text for word in happy_words) or polarity > 0.4:

            mood = "Happiness"

            st.success("### 😊 Happiness")

            tips = [
                "🎉 Celebrate your progress",
                "💜 Share your happiness",
                "🌟 Keep doing what makes you smile"
            ]

        elif any(word in text for word in sad_words) or polarity < -0.4:

            mood = "Sadness"

            st.warning("### 😢 Sadness")

            tips = [
                "🎵 Listen to calming music",
                "🚶 Take a short walk",
                "🤝 Reach out to someone you trust"
            ]

        else:

            mood = "Neutral"

            st.info("### 😐 Neutral")

            tips = [
                "💧 Stay hydrated",
                "🌱 Maintain a balanced routine",
                "☕ Take regular breaks"
            ]

    # ---------------- SUGGESTIONS CARD ----------------

    st.markdown(
        """
<div class="glass">

<h2>💡 Personalized Suggestions</h2>
""",
        unsafe_allow_html=True,
    )

    for tip in tips:
        st.markdown(f"- {tip}")

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- SAVE HISTORY ----------------

    new_record = pd.DataFrame({

        "Date": [
            datetime.now().strftime("%d-%m-%Y %H:%M")
        ],

        "User Input": [
            user_input
        ],

        "Mood": [
            mood
        ],

        "Sentiment Score": [
            round(polarity, 2)
        ]

    })

    history = pd.read_csv("history.csv")

    history = pd.concat(
        [history, new_record],
        ignore_index=True
    )

    history.to_csv(
        "history.csv",
        index=False
    )
        # ---------------- LOAD HISTORY ----------------

    history = pd.read_csv("history.csv")

    if not history.empty:

        history["Date"] = pd.to_datetime(
            history["Date"],
            dayfirst=True
        )

        history = history.sort_values("Date")

        st.markdown("---")

        st.markdown(
            """
<div class="glass">

<h2>📜 Mood History</h2>

</div>
""",
            unsafe_allow_html=True
        )

        st.dataframe(
            history,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("## 📈 Sentiment Trend")

            st.line_chart(
                history.set_index("Date")["Sentiment Score"]
            )

        with col2:

            st.markdown("## 😊 Mood Distribution")

            mood_count = history["Mood"].value_counts()

            st.bar_chart(mood_count)

    # ---------------- CLEAR HISTORY ----------------

    st.markdown("")

    if st.button(
        "🗑️ Clear Mood History",
        use_container_width=True
    ):

        empty_df = pd.DataFrame(
            columns=[
                "Date",
                "User Input",
                "Mood",
                "Sentiment Score"
            ]
        )

        empty_df.to_csv(
            "history.csv",
            index=False
        )

        st.success("Mood history cleared successfully!")

        st.rerun()

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
    """
<div style="text-align:center;
padding:20px;
color:#d8b4fe;
font-size:16px;">

🧠 <b>AI Mental Wellness Support Assistant</b><br><br>

Made with ❤️ using
<b>Streamlit</b> •
<b>Gemini AI</b> •
<b>TextBlob</b>

</div>
""",
    unsafe_allow_html=True
)