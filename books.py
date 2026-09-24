import streamlit as st
from pathlib import Path
import base64
import mimetypes


# ---------------------------------------------------------
# BOOK COVER FOLDER
# ---------------------------------------------------------

BOOK_COVERS = Path(__file__).parent / "book_covers"


# ---------------------------------------------------------
# FIND COVER EVEN IF EXTENSION / CAPITALIZATION IS DIFFERENT
# ---------------------------------------------------------

def find_cover(*keywords):
    """
    Finds a book cover by looking for the given words
    in the filename. This means you don't need to rename
    your existing poster files.
    """

    if not BOOK_COVERS.exists():
        return None

    files = list(BOOK_COVERS.iterdir())

    for file in files:
        filename = file.stem.lower().replace(" ", "").replace("_", "").replace("-", "")

        if all(
            keyword.lower().replace(" ", "").replace("_", "").replace("-", "")
            in filename
            for keyword in keywords
        ):
            return str(file)

    return None


# ---------------------------------------------------------
# BOOK DATA
# ---------------------------------------------------------

BOOKS = [

    {
        "title": "Samsara: Enter the Valley of the Gods",
        "author": "Saksham Garg",
        "cover": find_cover("samsara"),
        "quote": "Our souls are made up of the choices in our lives.",
        "why": (
            "I chose this book because it brings Indian mythology into a "
            "modern fantasy world. It explores choices, identity, spirituality, "
            "and the search for something deeper than the ordinary."
        )
    },

    {
        "title": "The Guide",
        "author": "R. K. Narayan",
        "cover": find_cover("guide"),
        "quote": "We generally do not have a correct measure of our own wisdom.",
        "why": (
            "I chose this book because it is a beautiful story about mistakes, "
            "transformation, and unexpectedly finding a new direction in life."
        )
    },

    {
        "title": "The Blue Umbrella",
        "author": "Ruskin Bond",
        "cover": find_cover("ruskinbond"),
        "quote": "She was always ready with her smile.",
        "why": (
            "I chose this book because it is simple, gentle, and warm. "
            "It reminds us that happiness can be found in ordinary things "
            "and that kindness can make a simple life beautiful."
        )
    },

    {
        "title": "The Palace of Illusions",
        "author": "Chitra Banerjee Divakaruni",
        "cover": find_cover("palace", "illusions"),
        "quote": "A situation in itself is neither happy nor unhappy.",
        "why": (
            "I chose this book because it gives a different perspective on "
            "the Mahabharata while exploring identity, emotions, choices, "
            "relationships, and resilience."
        )
    },

    {
        "title": "A Fine Balance",
        "author": "Rohinton Mistry",
        "cover": find_cover("fine", "balance"),
        "quote": "You have to use your failures as stepping stones to success.",
        "why": (
            "I chose this book because it shows how friendship and humanity "
            "can survive even when life becomes extremely difficult."
        )
    },

    {
        "title": "Swami and Friends",
        "author": "R. K. Narayan",
        "cover": find_cover("swami", "friends"),
        "quote": "Life is full of surprises.",
        "why": (
            "I chose this book because it reminds us of childhood, friendship, "
            "and the simple happiness hidden in ordinary days."
        )
    },

    {
        "title": "The Little Prince",
        "author": "Antoine de Saint-Exupéry",
        "cover": find_cover("little", "prince"),
        "quote": "It is only with the heart that one can see rightly.",
        "why": (
            "I chose this book because beneath its simple story are beautiful "
            "ideas about love, loneliness, friendship, and what truly matters."
        )
    },

    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "cover": find_cover("alchemist"),
        "quote": "The possibility of having a dream come true makes life interesting.",
        "why": (
            "I chose this book because it gently reminds us to follow meaningful "
            "dreams and trust the journey, even when we don't know where it will lead."
        )
    },

    {
        "title": "Man's Search for Meaning",
        "author": "Viktor E. Frankl",
        "cover": find_cover("search", "meaning"),
        "quote": "He who has a why to live can bear almost any how.",
        "why": (
            "I chose this book because it explores one of life's deepest questions: "
            "how we can find meaning even during painful and difficult times."
        )
    },

    {
        "title": "Ikigai",
        "author": "Héctor García & Francesc Miralles",
        "cover": find_cover("ikigai"),
        "quote": "Only staying active will make you want to live a hundred years.",
        "why": (
            "I chose this book because it encourages us to notice the small things "
            "that give everyday life meaning instead of always chasing something bigger."
        )
    },

    {
        "title": "Tuesdays with Morrie",
        "author": "Mitch Albom",
        "cover": find_cover("tuesday", "morrie"),
        "quote": "Love always wins.",
        "why": (
            "I chose this book because it beautifully explores love, relationships, "
            "forgiveness, and appreciating the people who make our lives meaningful."
        )
    },

    {
        "title": "The Midnight Library",
        "author": "Matt Haig",
        "cover": find_cover("midnight", "library"),
        "quote": "You don't have to understand life. You just have to live it.",
        "why": (
            "I chose this book because it speaks to people who constantly wonder "
            "'what if?' and reminds us that our present life can still hold possibilities."
        )
    },

    {
        "title": "A Man Called Ove",
        "author": "Fredrik Backman",
        "cover": find_cover("man", "called", "ove"),
        "quote": "Being alone doesn't make you lonely.",
        "why": (
            "I chose this book because beneath its humor is a touching story about "
            "grief, loneliness, friendship, and finding reasons to care again."
        )
    },

    {
        "title": "The Power of Your Subconscious Mind",
        "author": "Joseph Murphy",
        "cover": find_cover("power", "subconscious"),
        "quote": "Keep your conscious mind busy with expectation of the best.",
        "why": (
            "I chose this book because it encourages us to become more aware of "
            "our repeated thoughts and beliefs and how they influence our mindset."
        )
    },

    {
        "title": "The Courage to Be Disliked",
        "author": "Ichiro Kishimi & Fumitake Koga",
        "cover": find_cover("courage", "disliked"),
        "quote": "Freedom is being disliked by other people.",
        "why": (
            "I chose this book because many people spend too much energy worrying "
            "about how they are seen by others. It encourages a more independent way of living."
        )
    },

    {
        "title": "Siddhartha",
        "author": "Hermann Hesse",
        "cover": find_cover("siddhartha"),
        "quote": "Wisdom cannot be imparted.",
        "why": (
            "I chose this book because it is a quiet journey of self-discovery "
            "and reminds us that some truths have to be experienced for ourselves."
        )
    },

    {
        "title": "The Boy, the Mole, the Fox and the Horse",
        "author": "Charlie Mackesy",
        "cover": find_cover("boy", "mole"),
        "quote": "Asking for help isn't giving up.",
        "why": (
            "I chose this book because its simple words offer comfort during difficult "
            "days and remind us that vulnerability is not weakness."
        )
    },

    {
        "title": "The Travelling Cat Chronicles",
        "author": "Hiro Arikawa",
        "cover": find_cover("travelling", "cat"),
        "quote": "The memories we make with the people we love stay with us.",
        "why": (
            "I chose this book because it gently explores friendship, love, loss, "
            "gratitude, and the beauty of the time we get with those we love."
        )
    },

    {
        "title": "The Namesake",
        "author": "Jhumpa Lahiri",
        "cover": find_cover("jhumpalhiri"),
        "quote": "They let you travel without moving your feet.",
        "why": (
            "I chose this book because it explores identity, family, belonging, "
            "and the slow process of understanding who we really are."
        )
    },

    {
        "title": "The Book of Joy",
        "author": "Dalai Lama, Desmond Tutu & Douglas Abrams",
        "cover": find_cover("book", "joy"),
        "quote": "The purpose of life is to find happiness.",
        "why": (
            "I chose this book because it explores joy without pretending that life "
            "is always easy. It brings together compassion, gratitude, forgiveness, and hope."
        )
    }
]


# ---------------------------------------------------------
# BOOK CARD
# ---------------------------------------------------------

def display_book(book):

    st.markdown(
        """
        <style>
        .book-card {
            background: linear-gradient(145deg, rgba(39, 25, 67, 0.98), rgba(28, 18, 48, 0.98));
            border: 1px solid rgba(190, 145, 255, 0.20);
            border-radius: 22px;
            padding: 22px;
            min-height: 760px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);
            margin-bottom: 25px;
            text-align: center;
        }
        .book-poster {
            width: 210px; height: 300px; object-fit: cover; border-radius: 10px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.40); margin-bottom: 18px;
        }
        .book-title { color:#F4EFFF; font-size:23px; font-weight:700; margin-bottom:5px; }
        .book-author { color:#C7B6F5; font-size:16px; margin-bottom:20px; }
        .book-label { color:#D7B8FF; font-size:16px; font-weight:700; text-align:left; margin-top:12px; }
        .book-quote { color:#F4EFFF; font-size:16px; font-style:italic; line-height:1.6; text-align:left; background:rgba(125,82,180,0.12); border-left:3px solid #A978FF; padding:12px 14px; border-radius:8px; margin-top:6px; }
        .book-why { color:#D8CCF0; font-size:15px; line-height:1.6; text-align:left; margin-top:6px; }
        </style>
        """, unsafe_allow_html=True
    )

    if book["cover"]:
        with open(book["cover"], "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode("utf-8")
        mime_type = mimetypes.guess_type(book["cover"])[0] or "image/jpeg"

        st.markdown(
            f"""
            <div class="book-card">
                <img src="data:{mime_type};base64,{image_data}" class="book-poster">
                <div class="book-title">📖 {book["title"]}</div>
                <div class="book-author">{book["author"]}</div>
                <div class="book-label">💬 A line to remember</div>
                <div class="book-quote">"{book["quote"]}"</div>
                <div class="book-label">💜 Why I chose this book</div>
                <div class="book-why">{book["why"]}</div>
            </div>
            """, unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="book-card">
                <div style="height:300px;display:flex;align-items:center;justify-content:center;font-size:60px;">📖</div>
                <div class="book-title">📖 {book["title"]}</div>
                <div class="book-author">{book["author"]}</div>
                <div class="book-label">💬 A line to remember</div>
                <div class="book-quote">"{book["quote"]}"</div>
                <div class="book-label">💜 Why I chose this book</div>
                <div class="book-why">{book["why"]}</div>
            </div>
            """, unsafe_allow_html=True
        )


# ---------------------------------------------------------
# MAIN BOOKS PAGE
# ---------------------------------------------------------

def books_page():

    st.markdown(
        """
        <h1 style="
            text-align:center;
            color:#F4EFFF;
            margin-bottom:5px;
        ">
            📚 Books for the Mind
        </h1>

        <p style="
            text-align:center;
            color:#C7B6F5;
            font-size:18px;
            margin-bottom:35px;
        ">
            Books that might meet you where you are.
        </p>
        """,
        unsafe_allow_html=True
    )

    for i in range(0, len(BOOKS), 2):

        col1, col2 = st.columns(2, gap="large")

        with col1:
            display_book(BOOKS[i])

        if i + 1 < len(BOOKS):
            with col2:
                display_book(BOOKS[i + 1])