import streamlit as st
import random
import streamlit.components.v1 as components
from books import books_page
from one_moment import one_moment_page




# =======================
# A GENTLE REMINDER
# =======================

AFFIRMATIONS = [

    # 🌱 Growth
    "🌱 You don't have to become someone else to become better.",
    "🌱 Tiny steps taken consistently can move mountains.",
    "🌱 Every season teaches you something valuable.",
    "🌱 You are allowed to outgrow people, places, and old versions of yourself.",
    "🌱 Your progress isn't measured by speed but by courage.",
    "🌱 Every mistake is proof that you're trying.",
    "🌱 The strongest trees were once fragile saplings.",
    "🌱 You are becoming the person your younger self needed.",
    "🌱 Growth often feels uncomfortable before it feels rewarding.",
    "🌱 Trust that every small effort is shaping your future.",

    # ☀ Hope
    "☀ The sunrise never asks permission to shine, and neither should you.",
    "☀ Difficult chapters are not the end of your story.",
    "☀ One day you'll look back and realize this moment made you stronger.",
    "☀ Even the longest night ends with morning.",
    "☀ Hope whispers when fear tries to shout.",
    "☀ Better days often arrive quietly.",
    "☀ There is still beauty waiting for you.",
    "☀ Keep walking. The path becomes clearer with every step.",
    "☀ Life has a beautiful way of surprising those who don't give up.",
    "☀ Tomorrow holds possibilities you can't yet imagine.",

    # ❤️ Self-Love
    "❤️ You deserve kindness from yourself first.",
    "❤️ Stop measuring your worth against someone else's journey.",
    "❤️ You are more than your achievements and failures.",
    "❤️ You don't need to earn the right to love yourself.",
    "❤️ Your imperfections make you beautifully human.",
    "❤️ Speak to yourself as you would to your closest friend.",
    "❤️ Celebrate your small victories—they matter.",
    "❤️ Your value doesn't decrease because someone failed to see it.",
    "❤️ It's okay to choose yourself sometimes.",
    "❤️ Loving yourself is a lifelong friendship.",

    # 🌙 Rest
    "🌙 You are allowed to pause without feeling guilty.",
    "🌙 Rest is part of the journey, not a detour.",
    "🌙 Healing also happens while you're resting.",
    "🌙 You don't have to solve everything today.",
    "🌙 Slow days still count.",
    "🌙 Breathe deeply. You don't have to rush through life.",
    "🌙 Even the moon has phases—it never shines at full brightness every night.",
    "🌙 Your body deserves care, not criticism.",
    "🌙 Peace begins when you stop fighting yourself.",
    "🌙 Rest is productive when it restores your soul.",

    # 💙 Anxiety & Strength
    "💙 Your thoughts are visitors, not permanent residents.",
    "💙 You have survived every difficult day you've faced.",
    "💙 One deep breath can be the beginning of calm.",
    "💙 It's okay not to have all the answers today.",
    "💙 You are stronger than the worries trying to convince you otherwise.",
    "💙 Let today be enough.",
    "💙 Not everything needs to be figured out immediately.",
    "💙 You don't have to carry every burden alone.",
    "💙 Your heart has overcome hard days before, and it will again.",
    "💙 Right now, in this moment, you are safe."
]

def gentle_reminder():

    if "daily_affirmation" not in st.session_state:
        st.session_state.daily_affirmation = random.choice(AFFIRMATIONS)

    st.markdown(
        "<h3 style='text-align:center;'>🌸 A Gentle Reminder</h3>",
        unsafe_allow_html=True
    )

    st.markdown("")

    st.markdown(
        f"""
<div style="text-align:center;">
<span style="font-size:26px; font-style:italic; color:white;">
❝ {st.session_state.daily_affirmation} ❞
</span>
</div>
""",
        unsafe_allow_html=True,
    )


# =======================
# MUSIC THERAPY
# =======================

PLAYLISTS = {

    "😔 Feeling Low": {
        "message": "When your heart feels heavy, let music remind you that brighter days are ahead. 🤍",
        "link": "https://open.spotify.com/playlist/6L6nb7fCgHpdq9ypQ3Gq3I?si=O5LaswIvTOWYKsFRFHGrAQ&utm_source=native-share-menu&pi=wOQCnssWRsqal"
    },

    "😣 Feeling Overwhelmed": {
        "message": "Take a deep breath. You don't have to solve everything today. 🌿",
        "link": "https://open.spotify.com/playlist/7o55SZuh4QpIMQOGv2oJdL?si=P64v0gIURD259ZmgyF2Tlw&utm_source=native-share-menu&pi=5HCLGSaWQXeKg"
    },

    "😌 Peace & Calm": {
        "message": "Slow down. Let your thoughts settle and your heart find peace. 🍃",
        "link": "https://open.spotify.com/playlist/472BIUHfjBFvN7n4ZvQ6qx?si=ELFSc0acT-isjqEUIVr12Q&utm_source=native-share-menu&pi=YuH5n0M8RXeH1"
    },

    "💪 Motivation & Confidence": {
        "message": "Believe in yourself. Every small step counts. 💪",
        "link": "https://open.spotify.com/playlist/2POLTxukQT7He263YHNKnc?si=73WbbGOvSyuoD30ISbuWcQ&utm_source=native-share-menu&pi=rKU1yWR-QgWbz"
    },

    "😊 Happy Mood": {
        "message": "Smile a little. Celebrate the little moments. ☀️",
        "link": "https://open.spotify.com/playlist/2dPtk6cbQiLE7tSOB6cW1J?si=FyRdx2QGR2S1OMI-K-9T4g&utm_source=native-share-menu&pi=dO4mXreTSyKWg"
    }

}

def music_therapy():
    st.subheader("🎵 Music for Every Mood")
    st.write("Choose a playlist based on how you're feeling today.")
    mood=st.selectbox("Choose your mood",list(PLAYLISTS.keys()))
    st.info(PLAYLISTS[mood]["message"])
    url=PLAYLISTS[mood]["link"]
    playlist_id=url.split("/")[-1].split("?")[0]
    components.html(
    f"""
    <iframe
        style="border-radius:12px"
        src="https://open.spotify.com/embed/playlist/{playlist_id}"
        width="100%"
        height="500"
        frameborder="0"
        allowfullscreen=""
        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture">
    </iframe>
    """,
    height=520,
)

STORIES = [



{
    "title":"🌿 The Little Squirrel's Gift",

    "subtitle":"No act of kindness is ever too small.",

    "story":"""
The sun had just begun to rise over the shores of the great ocean. Gentle waves rolled toward the land as thousands of vanaras worked with great determination. Lord Rama's army was building a bridge across the sea to reach Lanka, where Sita was being held captive.

Everywhere, there was movement.

Some carried enormous boulders upon their shoulders. Others lifted mighty trees to strengthen the bridge. The air echoed with the sounds of teamwork, faith, and hope. Every person wanted to offer their strength for a cause greater than themselves.

Among all this stood a tiny squirrel.

It watched the mighty warriors with wonder.

Then it looked down at its own little body.

It could not lift heavy rocks.

It could not carry giant trees.

For a brief moment, the little squirrel wondered if there was any place for someone so small in such an important task.

But instead of walking away, it chose to help in the only way it could.

The squirrel ran to the edge of the sea and rolled gently in the soft sand until tiny grains clung to its fur. It hurried to the bridge and shook the sand into the small spaces between the large stones. Then it ran back to gather more.

Again.

And again.

And again.

Its work was slow.

Its contribution seemed almost invisible.

Some of the vanaras noticed the little squirrel and laughed.

"What difference will a few grains of sand make?" they asked.

"This bridge is built with mountains, not handfuls of sand."

The squirrel heard their words.

It did not argue.

It did not become angry.

It simply continued doing what it believed was right.

Lord Rama had been watching quietly.

He walked toward the tiny squirrel and gently lifted it into His hands.

Looking at the little creature with great affection, He smiled.

"You may be small, but your heart is full of devotion. You are giving everything you have. No offering made with love is ever insignificant."

With great tenderness, Lord Rama gently stroked the squirrel's back with three fingers.

It is said that from that day onward, squirrels have carried three stripes upon their backs as a reminder of His loving touch.

The laughter stopped.

Everyone understood that day that greatness is not measured by strength alone.

Sometimes it is measured by sincerity.

Even the smallest grain of sand has its place in building a bridge.
""",

    "reflection":"""
There are moments when we feel too ordinary to make a difference. We compare ourselves with people who seem more talented, more successful, or more capable, and we begin to believe that our own efforts are too small to matter.

The little squirrel reminds us that life does not ask us to do everything.

It simply asks us to do what we can, with honesty, kindness, and a willing heart.

A kind word.

A helping hand.

A few minutes spent listening to someone.

One small step toward a dream.

These may seem like grains of sand, yet they often become the quiet foundation for something much greater.

Never underestimate the value of a sincere heart.

Because in the eyes of Dharma, no act of goodness is ever too small.
"""
}

,
{
    "title": "🔥 Nachiketa and Yama",

    "subtitle": "The Boy Who Chose Truth.",

    "story": """
Long ago, there lived a young boy named Nachiketa. Though he was young, his heart was filled with honesty, and his mind was always searching for the truth. While others admired grand ceremonies and rich offerings, Nachiketa believed that what mattered most was the sincerity behind every action.

One day, his father, Sage Vajashrava, performed a sacred yajna. According to tradition, a person performing such a sacrifice should give away their best possessions with a pure and generous heart.

As people gathered to witness the ceremony, Nachiketa quietly stood beside his father. He watched carefully as old and weak cows were being donated. They could no longer give milk or work in the fields.

The ceremony looked grand, but something did not feel right.

A gentle question arose in Nachiketa's heart.

"If a gift is given without sincerity, can it truly be called an offering?"

He softly asked his father,

"Father, to whom will you give me?"

His father remained silent.

Nachiketa asked again.

Still there was no answer.

When he asked a third time, his father, overcome by anger, said,

"I give you to Yama, the Lord of Death!"

Though spoken in anger, Nachiketa believed that a promise should never be taken lightly.

Without fear, he journeyed to Yama's abode.

Yama was away, so Nachiketa waited there patiently for three days without food or water.

When Yama returned, he was deeply moved.

"You have waited here with great patience. I shall grant you three wishes."

For his first wish, Nachiketa asked that his father should welcome him home with love.

For his second wish, he asked to learn the sacred fire sacrifice.

Then came his third wish.

"What happens after death?" he asked.

"What is the truth about the Ātman?"

Yama first tried to distract him.

He offered wealth.

Palaces.

Long life.

Power.

Anything a human could desire.

But Nachiketa quietly replied,

"All these things will one day disappear. I seek only the truth."

Yama smiled.

He realised the young boy had chosen wisdom over temporary pleasures.

Then Yama taught him about the Ātman.

"The body is born and one day dies.

But the Ātman is never born and never dies.

It cannot be destroyed.

It is eternal."

Nachiketa returned home carrying no treasure.

He returned with wisdom that continues to inspire people even today.
""",

    "reflection": """
Life often offers us two paths.

One is filled with comfort, wealth, and things that last only for a short time.

The other asks us to seek truth, wisdom, and lasting peace.

Nachiketa reminds us that real happiness is not found in everything we own.

It is found in understanding ourselves.

When we begin to know the Ātman, fear slowly loses its hold over us.

True wisdom is choosing what is eternal over what is temporary.
"""
}

,
{
    "title": "🕊️ King Shibi",

    "subtitle": "A King Who Saw Every Life as Precious.",

    "story": """
Long ago, there lived a king named Shibi. He was loved by his people not because of his wealth or his powerful army, but because he ruled with compassion. Everyone knew that if they came to King Shibi seeking help, they would never leave disappointed.

One day, while the king was sitting in his royal court, a frightened dove suddenly flew into the palace. Its tiny wings trembled with fear as it landed in the king's lap, seeking protection.

A few moments later, a mighty hawk entered the court.

Looking at the king, the hawk said,

"That dove is my food. Please return it to me."

The court became silent.

King Shibi looked at the little dove resting safely in his hands.

Then he looked at the hawk.

He understood that both had a rightful place in nature.

The dove wished to live.

The hawk needed food to survive.

Neither was wrong.

The king gently replied,

"I cannot hand over someone who has come to me for protection. A king's duty is to protect those who seek refuge."

The hawk answered,

"If you save the dove, what about me? If I cannot eat, I too will suffer. Is my life worth less than the dove's?"

The king thought carefully before answering.

"You are right," he said.

"Your hunger is real. I will not save one life by ignoring another."

Then King Shibi made an extraordinary decision.

"I will give you flesh from my own body equal to the weight of this dove."

A balance was brought before the court.

The dove was placed on one side.

The king placed a piece of his own flesh on the other.

But the dove remained heavier.

He offered another piece.

Still the balance did not move.

Again and again, he continued.

Finally, the king stepped onto the balance himself.

"If my whole life is needed to protect another," he said quietly, "then let it be so."

At that very moment, the dove and the hawk revealed their true forms.

They were Agni, the god of fire, and Indra, the king of the devas.

They had come to test the king's compassion.

Indra smiled and said,

"You have shown that true Dharma is not spoken with words. It is lived through compassion."

The king's wounds disappeared, and he was blessed for his kindness.

His story has been remembered ever since as a symbol of selfless compassion.
""",

    "reflection": """
It is easy to be kind when kindness costs us nothing.

The real test comes when doing the right thing asks us to give up our comfort, our time, or something we value.

Most of us may never face a test like King Shibi's.

But every day we can choose compassion.

A helping hand.

A kind word.

Standing beside someone who feels alone.

These simple acts may seem small, but they can make someone feel safe and valued.

True strength is not found in power.

It is found in a heart that chooses kindness.
"""
}

,
{
    "title": "🌼 Shabari's Berries",

    "subtitle": "Love Is Measured by the Heart, Not by Perfection.",

    "story": """
Deep within a peaceful forest lived an elderly woman named Shabari. She was neither rich nor famous. She lived a simple life, but her heart held one beautiful dream—to one day welcome Lord Rama into her humble home.

Many years earlier, her guru, Sage Matanga, had blessed her with these words:

"One day, Lord Rama will come to you."

From that day onward, Shabari waited with complete faith.

Every morning before sunrise, she cleaned the path leading to her small hut. She swept away the fallen leaves and decorated the path with flowers, believing that if Rama arrived that day, she wanted His journey to be beautiful.

One day became another.

Months turned into years.

Her hair turned grey.

Her hands became weak.

But her faith never faded.

Many people laughed at her.

"Why would Lord Rama ever come to your little hut?" they asked.

Shabari never became angry.

She simply smiled and continued waiting.

Every morning she walked into the forest and collected fresh berries.

Before placing each berry into her basket, she tasted a tiny piece of it.

If it was sour, she set it aside.

If it was sweet, she carefully kept it for Rama.

She wanted to offer Him only the sweetest fruits.

Then one beautiful morning, her long wait came to an end.

Lord Rama and Lakshmana arrived at her little hut while searching for Sita.

Shabari's eyes filled with tears.

The moment she had prayed for all her life had finally arrived.

She welcomed them with folded hands and offered the berries she had collected with so much love.

Some traditions say Lakshmana noticed that the berries had already been tasted.

But Lord Rama understood the love behind the offering.

He happily accepted every berry.

To Him, they were sweeter than any feast prepared in a royal palace.

Because they had been offered with pure devotion.

That day, Shabari realised that true love is never ignored by the Divine.

Years of waiting had not been wasted.

Faith had quietly blossomed into fulfilment.
""",

    "reflection": """
We often worry that we are not good enough.

We compare ourselves with others.

We think our homes are too small, our talents too ordinary, or our prayers too imperfect.

Shabari reminds us that love does not need to be perfect.

It only needs to be sincere.

Whether we are helping someone, caring for our family, or offering our prayers, it is the love behind our actions that truly matters.

The sweetest gift is not always the most expensive one.

Sometimes, it is simply the one given with all our heart.
"""
}

,
{
    "title": "🌳 King Rantideva",

    "subtitle": "The King Who Chose Compassion Over Hunger.",

    "story": """
Long ago, there lived a noble king named Rantideva. Though he ruled a prosperous kingdom, he never considered wealth to be his greatest treasure. He believed that everything he possessed was a gift from God and should be shared with those in need.

No one who came to his palace hungry was ever turned away.

No one who sought help was ever refused.

As the years passed, Rantideva gave away more and more of his wealth. Slowly, he was left with almost nothing. Yet his heart remained as generous as ever.

One day, after many days without food, Rantideva and his family finally received a simple meal and a small pot of water. Just as they were about to eat, a weary traveller arrived at their door.

The king welcomed him warmly and offered him part of the meal.

The traveller left with gratitude.

As Rantideva prepared to eat what remained, another hungry visitor arrived.

Without hesitation, he shared his food once again.

Soon after, a third guest appeared.

The king gave away the little food that was still left.

Now only a small pot of water remained.

His throat was dry.

His body had become weak from hunger.

As he lifted the pot to drink, another traveller approached, exhausted and thirsty.

"Please," the man said softly, "may I have a little water?"

For a brief moment, Rantideva looked at the pot in his hands.

It was the last thing he possessed.

Then he smiled gently.

Without a second thought, he offered the water to the thirsty man.

As the traveller drank, Rantideva quietly prayed,

"I do not seek wealth, power, or even liberation for myself. My only wish is that I may help remove the suffering of others."

At that very moment, the visitors revealed their true forms.

They were divine beings who had come to test the king's compassion.

Rantideva had passed every test.

Even when he had almost nothing, he chose kindness over comfort.

The gods blessed him, not because he had given away great riches, but because his heart remained free from selfishness.

His story has been remembered for generations as a beautiful example of selfless compassion.
""",

    "reflection": """
Kindness is easy when we have plenty.

The real test comes when giving asks something of us.

Rantideva reminds us that generosity is not measured by how much we give, but by the love with which we give it.

Most of us may never be asked to give away our last meal.

But every day, we are given smaller opportunities.

A few minutes of our time.

A listening ear.

A comforting word.

A helping hand.

These simple acts may seem small, yet they can become a source of hope for someone who needs them.

True compassion begins when we stop asking,

'How much do I have?'

and begin asking,

'How much kindness can I share?'
"""
}

,
{
    "title": "🪔 Sage Dadhichi",

    "subtitle": "The Greatest Gift Is Sometimes Ourselves.",

    "story": """
Long ago, the devas faced a terrible challenge. A powerful asura named Vritra had become so strong that no weapon on Earth or in heaven could defeat him. Fear spread across the three worlds, and even the devas began to lose hope.

Seeking guidance, they went to Lord Brahma.

Brahma told them,

"There is only one weapon powerful enough to defeat Vritra. It must be made from the bones of the great sage Dadhichi."

The devas were shocked.

How could they ask such a sacrifice from a sage who had spent his life in prayer, wisdom, and service?

Yet, with heavy hearts, they went to Dadhichi's ashram.

The sage welcomed them warmly and noticed the sadness on their faces.

When they explained the danger facing the world and the sacrifice that was needed, Dadhichi listened quietly.

After a few moments of silence, he smiled.

"If this body can protect countless lives," he said gently, "then what greater purpose could it serve?"

He reminded them that the body is temporary.

One day, every person must leave it behind.

But if it could become the reason others lived in peace, then it had fulfilled its highest purpose.

With complete peace in his heart, Sage Dadhichi entered deep meditation.

His mind became still.

His heart rested in the Divine.

When the time came, he willingly gave up his mortal body.

The devas bowed before him with deep respect.

From his sacred bones, Vishwakarma, the divine architect, created the mighty Vajra, the thunderbolt weapon.

Holding the Vajra, Indra faced Vritra once again.

This time, the battle ended.

Peace returned to the worlds.

The devas celebrated their victory, but they never forgot that it had been made possible not by power alone, but by the selfless sacrifice of one humble sage.

Even today, Sage Dadhichi is remembered not for what he possessed, but for what he was willing to give.
""",

    "reflection": """
We often think of sacrifice as losing something.

But Dadhichi's story teaches us that sometimes the greatest gift we can offer is ourselves.

Not through grand acts, but through simple everyday choices.

Sharing our time.

Helping someone learn.

Standing beside a friend during difficult days.

Speaking words of kindness.

These moments may seem ordinary, but they can change another person's life.

True greatness is not measured by what we keep for ourselves.

It is measured by how much good we leave behind for others.

When we use our strengths to help those around us, we continue the spirit of Sage Dadhichi—a life lived with courage, compassion, and selfless purpose.
"""
}

,
{
    "title": "🦢 Ashtavakra",

    "subtitle": "The Wisdom That Saw Beyond the Body.",

    "story": """
Long ago, there lived a boy named Ashtavakra. Even before he was born, he showed an extraordinary gift for wisdom.

It is said that while he was still in his mother's womb, he heard his father reciting the Vedas. When his father made a mistake, the unborn child gently corrected him.

His father became angry and cursed the child.

When Ashtavakra was born, his body was bent in eight places. Because of this, he came to be known as Ashtavakra, meaning "the one with eight bends."

As he grew older, people often judged him by his appearance.

Some stared.

Some laughed.

Others believed that someone with such a body could never possess great wisdom.

But Ashtavakra never allowed their opinions to disturb his peace.

He spent his days learning, reflecting, and seeking the truth about the Ātman.

One day, he travelled to the court of King Janaka, who was famous for welcoming the wisest scholars in the kingdom.

As Ashtavakra entered the royal court, many scholars looked at him and laughed because of his appearance.

To everyone's surprise, Ashtavakra laughed too.

The court fell silent.

King Janaka gently asked,

"Everyone laughed at you because of your body. Why are you laughing?"

Ashtavakra smiled peacefully.

"I believed this was a gathering of wise people," he replied.

"But I see many here judge only the body."

"They look at skin, bones, and appearance."

"True wisdom sees far beyond that."

His words filled the court with silence.

King Janaka immediately recognised the greatness of the young sage and welcomed him with deep respect.

The conversation between them later became the famous Ashtavakra Gita.

Ashtavakra taught that our true identity is not the body or even the mind.

It is the Ātman.

The body grows older.

Thoughts change.

Emotions come and go.

But the Ātman remains pure, peaceful, and untouched by time.

Because Ashtavakra understood this truth, he never allowed the opinions of others to define who he was.

His wisdom has continued to inspire seekers for thousands of years.
""",

    "reflection": """
We live in a world where people are often judged by their appearance, success, or achievements.

Sometimes we even judge ourselves the same way.

Ashtavakra reminds us that our greatest value is not found in the way we look.

It is found in our kindness.

Our wisdom.

Our character.

Our compassion.

When we begin to recognise the Ātman within ourselves, we stop comparing and start accepting ourselves with peace.

True confidence does not come from changing who we are.

It comes from understanding who we truly are.

The body may change with time.

But the light of the Ātman always remains.
"""
}

,
{
    "title": "🌸 Savitri and Satyavan",

    "subtitle": "The Love That Spoke Without Fear.",

    "story": """
Long ago, there lived a wise and kind princess named Savitri. She was admired not only for her beauty but also for her gentle heart and clear wisdom.

When it was time for her to choose a husband, she travelled across many kingdoms. During her journey, she met a noble young man named Satyavan, who lived a simple life in the forest while caring lovingly for his parents.

The moment Savitri met him, she knew he was the one she wished to spend her life with.

When she returned home, the great sage Narada visited the palace.

He said,

"Satyavan is noble, truthful, and kind. But there is one sorrowful truth. Exactly one year from today, his life will come to an end."

The king pleaded with Savitri to choose someone else.

But she answered calmly,

"A choice made with truth cannot be changed because of fear. Once I have given my heart, I cannot give it again."

She married Satyavan and began her peaceful life in the forest.

She never counted the days with sadness.

Instead, she filled every day with gratitude, kindness, and love.

As the final day approached, Savitri observed a sacred fast and spent her time in prayer.

On the destined morning, Satyavan went into the forest to gather wood.

Savitri asked to accompany him.

As they walked beneath the tall trees, Satyavan suddenly felt weak.

He rested his head upon Savitri's lap.

Within moments, his breathing became still.

Soon, Yama, the Lord of Death, appeared and gently took Satyavan's soul.

As Yama walked away, Savitri quietly followed Him.

After some distance, Yama turned and said,

"You have fulfilled your duty. You should now return."

But Savitri continued walking beside Him.

She did not argue.

She did not beg.

She simply spoke with wisdom, kindness, and respect.

Impressed by her words, Yama offered her a boon.

She first asked that her blind father-in-law should regain his eyesight.

Yama granted the wish.

She continued walking.

He offered another boon.

She asked that her father-in-law's lost kingdom be restored.

Again, Yama agreed.

Still she walked beside Him.

Moved by her devotion, Yama offered one final boon.

Savitri gently said,

"May I be blessed with many children."

Yama smiled and granted the wish.

Only then did He realise what those words meant.

Without Satyavan, the blessing could never come true.

Bound by His promise and touched by Savitri's wisdom, Yama restored Satyavan's life.

The couple returned home together, and every blessing Yama had granted came true.

Savitri's courage had not defeated death through force.

It had touched it through wisdom, patience, and unwavering love.
""",

    "reflection": """
When life becomes uncertain, fear often speaks the loudest.

Savitri teaches us that courage does not always mean fighting.

Sometimes courage means remaining calm when everything around us feels uncertain.

Her story reminds us that wisdom, patience, and kindness are often stronger than anger or force.

True love is not possessive.

It is patient.

It is selfless.

It remains steady even during life's greatest challenges.

A calm heart guided by truth can overcome even the darkest moments.
"""
}

,
{
    "title": "🌧️ Markandeya",

    "subtitle": "The Boy Who Chose Faith Over Fear.",

    "story": """
Long ago, there lived a wise sage named Mrikandu and his wife, Marudvati. For many years, they prayed to Lord Shiva for a child.

Pleased by their devotion, Lord Shiva appeared before them and offered a choice.

"You may have a son who is wise and devoted but will live only for a short time, or a son who will live a long life without wisdom."

The couple chose the first blessing.

Soon, a son was born, and they named him Markandeya.

From childhood, Markandeya loved Lord Shiva with all his heart. While other children spent their days playing, he found joy in prayer, meditation, and chanting the Lord's name.

As the years passed, his parents carried a quiet sadness. They knew that according to destiny, their son would leave the world on his sixteenth birthday.

When Markandeya learned the truth, he did not become afraid.

Instead, his devotion became even stronger.

"If every moment of life is a gift," he thought, "I will spend every moment remembering the Divine."

On the morning of his sixteenth birthday, Markandeya went to a temple of Lord Shiva.

He embraced the Shiva Linga and closed his eyes in deep prayer.

His heart was filled with faith.

Soon, Yama, the Lord of Death, arrived.

The time fixed by destiny had come.

Yama asked the young sage to come with him.

But Markandeya continued praying without fear.

When Yama threw his noose, it accidentally fell around both Markandeya and the Shiva Linga.

In that very moment, the temple shook.

A brilliant light filled the air.

Lord Shiva appeared from the Shiva Linga with great power.

Seeing His devoted child seeking refuge in Him, Lord Shiva stood before Yama.

He declared,

"One who has surrendered with such pure devotion shall not be taken before his time."

By His grace, Markandeya was blessed with a long life.

More importantly, he became a symbol of fearless faith.

His story reminds people that true devotion is not born from fear of death.

It is born from love for the Divine.
""",

    "reflection": """
Life often brings moments that we cannot control.

We worry about tomorrow.

We fear losing the people we love.

We become anxious about what the future holds.

Markandeya reminds us that faith does not remove every difficulty.

Instead, it gives us the strength to face those difficulties with a peaceful heart.

Whether through prayer, meditation, or quiet trust, faith helps us remain steady even when life feels uncertain.

Sometimes courage is not the absence of fear.

It is choosing hope while fear stands beside us.
"""
}

,
{
    "title": "🌺 Upamanyu",

    "subtitle": "The Boy Who Never Lost Faith.",

    "story": """
Long ago, there lived a young boy named Upamanyu. He belonged to a humble family and lived a simple life with his mother. Though they had very little, Upamanyu's heart was always cheerful.

One day, he visited a wealthy relative's home and tasted fresh cow's milk for the very first time.

When he returned home, he happily asked his mother,

"Mother, may I also have some milk?"

His mother looked at him with loving eyes, but her heart grew heavy. They were too poor to own a cow.

Not wanting to disappoint her son, she mixed flour with water and gave it to him.

Upamanyu took a sip.

He quietly looked at his mother.

"This isn't milk, is it?" he asked.

Unable to hide the truth any longer, tears filled her eyes.

"My child," she said softly, "if I had milk, I would gladly give it to you. We simply do not have enough."

Then she gently placed her hand on his head.

"If there is anyone who listens to the prayers of sincere hearts, it is Lord Shiva."

Those words remained in Upamanyu's heart.

The very next morning, he left for the forest to pray to Lord Shiva.

Days passed.

Then weeks.

He faced hunger.

Cold nights.

Loneliness.

Yet he never complained.

His devotion only grew stronger.

Seeing the boy's unwavering faith, Lord Shiva decided to test him.

Disguised as a wandering sage, He approached Upamanyu and asked,

"Why do you worship Shiva? There are many other gods who can give you wealth and comfort."

Upamanyu smiled and replied,

"I do not pray because I seek riches."

"I pray because my heart belongs to Lord Shiva."

The sage continued to speak lightly of Shiva.

For the first time, Upamanyu became firm.

He folded his hands and respectfully said,

"Please forgive me, but I cannot listen to anyone speak disrespectfully about the One I love."

At that very moment, the sage smiled.

His disguise disappeared.

Before the young boy stood Lord Shiva Himself, shining with divine light.

Shiva looked at Upamanyu with great affection.

"My child," He said,

"I did not come to test your knowledge."

"I came to see whether your devotion would remain steady even when your faith was questioned."

"You have shown that true devotion never changes with circumstances."

Lord Shiva blessed Upamanyu with wisdom, prosperity, and spiritual knowledge.

More importantly, He blessed him with a heart that would always remain connected to the Divine.
""",

    "reflection": """
Life does not always give us everything we ask for.

Sometimes our prayers seem unanswered.

Sometimes we wonder whether our efforts are being noticed.

Upamanyu reminds us that faith is not loving God only when life is easy.

True faith remains steady through both joy and hardship.

Whether we place our faith in God, goodness, or a higher purpose, this story teaches us to remain patient and sincere.

The strongest faith is often the quietest.

It continues to shine even when no one else can see it.
"""
}

,
{
    "title": "🌾 Sudama and Lord Krishna",

    "subtitle": "A Friendship That Time Could Never Change.",

    "story": """
Long ago, in the peaceful ashram of Sage Sandipani, two young boys studied together.

One was Krishna, who would one day become the king of Dwaraka.

The other was Sudama, the son of a poor Brahmin.

Although their lives were very different, their friendship knew no difference. They learned together, shared simple meals, and helped one another through the joys and challenges of student life.

Years passed.

Life took them on different paths.

Krishna became the beloved king of Dwaraka.

Sudama remained a humble Brahmin, living in a small hut with his wife and children.

His family often struggled to find enough food.

Their clothes were worn.

Many days passed without a proper meal.

Yet Sudama never complained.

His greatest treasure was not wealth.

It was the memory of his dear friend.

One day, seeing their hardships, Sudama's wife gently said,

"Why don't you visit your childhood friend Krishna? I know you would never ask Him for anything, but perhaps meeting Him will bring you peace."

After much thought, Sudama agreed.

Before he left, his wife searched the house for a gift.

There was almost nothing.

At last, she found a small handful of flattened rice and tied it carefully in a simple cloth.

It was all they could offer.

Holding the little bundle close to his heart, Sudama began the long journey to Dwaraka.

When he reached the magnificent palace, he felt small.

Golden halls surrounded him.

Kings and warriors filled the royal court.

He wondered whether Krishna would even remember a poor friend from so many years ago.

Before anyone could announce his arrival, Krishna saw him from a distance.

Without hesitation, the Lord of Dwaraka ran towards Sudama.

With tears of joy, He embraced His childhood friend.

Years disappeared in a single moment.

Krishna welcomed Sudama with the affection of a true friend, not the formality of a king.

He washed Sudama's tired feet with His own hands.

Everyone in the palace watched in silence.

Soon, Krishna noticed the small bundle hidden beneath Sudama's arm.

Smiling warmly, He asked,

"My dear friend, what have you brought for Me?"

Sudama felt embarrassed.

How could such a simple gift be offered in such a grand palace?

Before he could answer, Krishna gently took the bundle Himself.

When He saw the flattened rice, His face filled with joy.

He ate it happily, as though it were the finest feast in the world.

To Krishna, it was precious because it had been offered with love.

The two friends spent hours remembering their childhood.

Not once did Sudama ask for wealth.

Not once did Krishna ask why he had come.

Their friendship needed no explanation.

The next morning, Sudama quietly returned home.

As he walked, he wondered for a moment if he should have asked for help.

Then he smiled.

"My heart is full," he thought.

"Meeting my friend was enough."

When he reached his village, he stopped in amazement.

His small hut had become a beautiful home.

His family welcomed him with joy.

By Krishna's grace, everything they needed had been provided.

Krishna had understood His friend's needs without being asked.

For true friendship listens even to the words that are never spoken.
""",

    "reflection": """
We often think that the value of a gift depends on how expensive it is.

Sudama's story reminds us that love can never be measured by wealth.

A handwritten letter.

A warm smile.

A few moments spent listening.

A simple meal shared with someone who is lonely.

These may seem like small things, yet they often become the greatest gifts we can offer.

True friendship never counts what is given.

It treasures the love behind every gesture.

Perhaps that is why Krishna accepted a handful of flattened rice with greater joy than all the riches of a kingdom.

Because a heart filled with love is the most precious gift anyone can receive.
"""
}

,
{
    "title": "🌟 Dhruva",

    "subtitle": "The Child Who Found His Place Among the Stars.",

    "story": """
Long ago, there lived a young prince named Dhruva. Although he was born into a royal family, he often felt lonely.

His father, King Uttanapada, loved him, but showed greater affection to his younger son. One day, Dhruva saw his younger brother sitting happily on their father's lap.

Filled with innocent joy, Dhruva ran towards his father, hoping to sit beside him.

Before he could reach the king, his stepmother stopped him.

Her words deeply hurt the little boy.

"You do not deserve that place. If you wish to sit on the king's lap, you must first be born as my son."

Dhruva stood silently.

He was too young to understand why love could be divided.

With tears in his eyes, he ran to his mother.

His mother gently hugged him and said,

"My child, people may not always give us the love we hope for. But there is One who never turns away anyone who comes with a sincere heart."

She spoke about Lord Vishnu.

Those words gave Dhruva hope.

Although he was only a child, he decided to leave the palace and go into the forest to pray to Lord Vishnu.

The journey was difficult.

He faced hunger.

Cold nights.

Loneliness.

Wild animals.

Yet every challenge only made his determination stronger.

One day, the great sage Narada met the young prince.

Seeing his sincere devotion, Narada taught him the sacred mantra,

"Om Namo Bhagavate Vasudevaya."

Day after day...

Week after week...

Month after month...

Dhruva repeated the mantra with complete faith.

Slowly, his mind became calm.

His heart became peaceful.

He was no longer searching for a place on his father's lap.

He had begun discovering the strength within himself.

Pleased by such pure devotion, Lord Vishnu appeared before Dhruva in His divine form.

The young prince stood speechless.

All the pain he had carried quietly disappeared.

Lord Vishnu smiled and asked,

"My child, what do you wish for?"

Dhruva bowed with folded hands.

He no longer desired revenge.

He no longer wished to prove himself.

He simply wished to live a life guided by truth, devotion, and Dharma.

Lord Vishnu blessed him with everlasting honour.

After his life on Earth, Dhruva became the Dhruva Nakshatra—the Pole Star.

Even today, while countless stars appear to move across the night sky, the Pole Star remains steady, guiding travellers through the darkness.

Just as Dhruva found peace within himself, his star continues to guide others.
""",

    "reflection": """
Many of us know what it feels like to be left out.

To feel unnoticed.

To wonder why someone else's approval seems easier to earn than our own.

Dhruva reminds us that our worth does not depend on whether others choose us.

Real confidence grows when we stop chasing acceptance and begin discovering the strength already present within us.

Like the Pole Star, life may become stormy.

People may come and go.

Circumstances may change.

But when we stay connected to our values, our faith, and our Ātman, we remain steady even when everything around us feels uncertain.

Sometimes the greatest journey is not finding our place in someone else's heart.

It is finding peace within our own.
"""
}

]



def inspirational_stories():

    st.markdown("""
    <style>

    .story-title{
        text-align:center;
        font-size:42px;
        font-weight:bold;
        color:#F4EDFF;
        margin-bottom:5px;
    }

    .story-subtitle{
        text-align:center;
        color:#CBB9F5;
        font-size:18px;
        margin-bottom:25px;
    }

    .story-heading{
        color:#E9DDFF;
        font-size:26px;
    }

    .story-text{
        color:#F5F2FF;
        font-size:17px;
        line-height:1.9;
        text-align:justify;
    }

    .reflect-box{
        background:#25193D;
        padding:18px;
        border-radius:15px;
        border-left:5px solid #9B7BFF;
        margin-top:15px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="story-title">
    🪔 Ancient Stories, Timeless Lessons
    </div>

    <div class="story-subtitle">
    The world changes, but wisdom doesn't.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="reflect-box">

    These lesser-known stories from Hindu tradition have quietly inspired generations.

    They are not simply stories to be read, but moments to pause, reflect, and carry into everyday life.

    🌸 Read slowly. Reflect deeply.

    </div>
    """, unsafe_allow_html=True)


    

    stories = STORIES

    for s in stories:

        with st.expander(s["title"], expanded=False):

            st.markdown(
                f"<h3 class='story-heading'>{s['subtitle']}</h3>",
                unsafe_allow_html=True
            )

            st.markdown("### 📖 The Story")

            st.markdown(
                f"<div class='story-text'>{s['story']}</div>",
                unsafe_allow_html=True
            )

            st.markdown("---")

            st.markdown("### 🌸 A Moment to Reflect")

            st.markdown(
                f"""
                <div class="reflect-box">
                {s['reflection']}
                
                """,
                unsafe_allow_html=True
            )
        

def quotes_collection():
    st.info("Coming Soon 🌸")

MOVIES = {

    "😔 When You Feel Low": [

        ("The Secret Life of Walter Mitty","It's never too late to start living the life you've imagined."),
        ("Good Will Hunting","Healing begins when someone truly believes in you."),
        ("The Pursuit of Happyness","Hope survives even in the hardest moments."),
        ("About Time","Appreciate ordinary days—they become extraordinary memories."),
        ("Little Miss Sunshine","Life doesn't have to be perfect to be beautiful."),
        ("Dead Poets Society","Live with courage, purpose, and authenticity."),
        ("Soul","Joy often hides in life's smallest moments."),
        ("Her","A quiet story about loneliness, love, and letting go."),
        ("It's Kind of a Funny Story","Sometimes asking for help is the bravest step."),
        ("A Beautiful Mind","Resilience can coexist with vulnerability."),
        ("The King's Speech","Growth begins when fear is faced."),
        ("Life of Pi","Hope can carry us through life's storms."),
        ("Dear Zindagi","Healing starts with understanding yourself."),
        ("Chhichhore","Failure is never the end of your story."),
        ("12th Fail","Perseverance changes destinies."),
        ("Karwaan","Sometimes getting lost helps you find yourself."),
        ("Lootera","A bittersweet reminder to cherish love."),
        ("The Sky Is Pink","Celebrate every precious moment."),
        ("Udaan","Choose your own path despite the odds."),
        ("Tamasha","Rediscover the person you were meant to be."),
        ("Lakshya","Purpose gives direction to life."),
        ("Taare Zameen Par","Everyone blooms in their own time."),
        ("Jersey","Dreams are always worth chasing."),
        ("Vedam","Humanity is our greatest strength."),
        ("C/o Kancharapalem","Love exists in many beautiful forms."),
        ("Godavari","Peace is found in life's simple moments."),
        ("Oopiri","Friendship has the power to heal."),
        ("96","Some memories stay forever."),
        ("Charlie","Kindness changes lives.")
    ],

    "😊 Need a Smile": [

        ("Paddington","Kindness makes the world brighter."),
        ("Paddington 2","A warm hug in the form of a movie."),
        ("Gifted","A heartwarming story about family and love."),
        ("To All the Boys I've Loved Before","Sweet, lighthearted, and comforting."),
        ("Voicemails for Isabelle","A gentle reminder to treasure relationships."),
        ("Jerry Maguire","Sometimes love and honesty are all we need."),
        ("The Intern","Wisdom, friendship, and second chances."),
        ("Chef","A joyful journey of food, family, and fresh starts."),
        ("Sing Street","Follow your dreams and enjoy the ride."),
        ("The Fundamentals of Caring","Healing often begins with laughter."),
        ("The Way Way Back","Finding confidence one summer at a time."),
        ("Hunt for the Wilderpeople","Adventure, humor, and unexpected family."),
        ("Instant Family","Love grows in unexpected ways."),
        ("Begin Again","Every ending can become a new beginning."),
        ("The Hundred-Foot Journey","Food has a beautiful way of bringing people together."),
        ("Mrs. Harris Goes to Paris","Dreams are worth chasing at any age."),
        ("About a Boy","Sometimes we grow because of others."),
        ("The Map of Tiny Perfect Things","Find joy in life's little moments."),
        ("We Bought a Zoo","Sometimes the biggest leap brings the greatest happiness."),
        ("Flipped","An innocent story about growing up and love."),

        ("Queen","Finding yourself is the greatest adventure."),
        ("English Vinglish","Confidence begins from within."),
        ("Wake Up Sid","Growing up can be beautiful."),
        ("Piku","Family, laughter, and everyday life."),
        ("Qarib Qarib Singlle","Love can arrive unexpectedly."),
        ("Bareilly Ki Barfi","Lighthearted romance with plenty of smiles."),
        ("Zindagi Na Milegi Dobara","Live fully. Laugh often."),
        ("Dil Chahta Hai","Friendship never goes out of style."),
        ("Jab We Met","A reminder to choose happiness."),
        ("Yeh Jawaani Hai Deewani","Celebrate friendships and life's adventures."),
        ("Laapataa Ladies","A delightful story with heart and humor."),
        ("Nil Battey Sannata","Hope and education can change lives."),
        ("Stanley Ka Dabba","Simple joys leave lasting memories."),
        ("Uunchai","It's never too late to chase dreams."),
        ("Do Dooni Chaar","Family love makes everything worthwhile."),
        ("Mimi","Unexpected journeys can be beautiful."),
        ("Badhaai Ho","Celebrate life's surprises."),
        ("Chup Chup Ke","Comedy that never gets old."),
        ("Munna Bhai M.B.B.S.","Kindness heals more than medicine."),
        ("Lage Raho Munna Bhai","Truth and compassion always matter."),

        ("Anand","Gentle, timeless comfort."),
        ("Pelli Choopulu","Love, dreams, and delicious food."),
        ("Sammohanam","A charming romance."),
        ("Oohalu Gusagusalade","Sweet conversations and sweeter moments."),
        ("Chi La Sow","Unexpected love feels wonderful."),
        ("Brochevarevarura","Friendship mixed with laughter."),
        ("Ashta Chamma","A feel-good classic."),
        ("Miss Shetty Mr. Polishetty","Funny, emotional, and heartwarming."),
        ("Ala Modalaindi","Love begins unexpectedly."),
        ("Ee Nagaraniki Emaindi","Friendship goals."),
        ("Fidaa","A refreshing love story."),
        ("MAD","College fun at its best."),
        ("Happy Days","Youth, dreams, and friendship."),
        ("Mallesham","Inspiration through simplicity."),
        ("Malliswari","Classic family entertainer."),
        ("Nuvvu Naaku Nachav","One of Telugu cinema's greatest comfort movies."),
        ("Manmadhudu","Charming romance and comedy."),
        ("Nuvve Kavali","Simple love story that still feels fresh."),
        ("Ante Sundaraniki","A quirky romantic entertainer."),
        ("Ami Thumi","Comedy with lovable characters."),
        ("Krishna and His Leela","Modern relationships explored lightly."),
        ("Seethamma Vakitlo Sirimalle Chettu","Family warmth you'll want to revisit."),

        ("Oh My Kadavule","A magical second chance."),
        ("Thiruchitrambalam","Comfort found in ordinary life."),
        ("OK Kanmani","Modern love done right."),
        ("Rhythm","A gentle and soothing romance."),
        ("Abhiyum Naanum","A father's unconditional love."),
        ("Mozhi","Kindness and understanding."),
        ("Kandukondain Kandukondain","Love, family, and hope."),
        ("Sillunu Oru Kaadhal","A memorable emotional romance."),
        ("Boss Engira Bhaskaran","Comedy that never disappoints."),
        ("Panchathanthiram","Classic laughs."),
        ("Nanban","Friendship and inspiration."),
        ("Kalyana Samayal Saadham","A fun romantic comedy."),
        ("Pasanga","Childhood innocence."),
        ("Good Night","Simple, relatable, and wholesome."),
        ("Ayothi","Compassion changes lives."),
        ("Dum Dum Dum","A delightful family entertainer."),

        ("#Home","One of the warmest family films ever made."),
        ("Bangalore Days","Friendship, family, and unforgettable memories."),
        ("Premam","A nostalgic coming-of-age romance."),
        ("Ohm Shanthi Oshaana","Sweet, funny, and heartwarming."),
        ("Ustad Hotel","Food, family, and finding purpose."),
        ("Hridayam","Youth and beautiful memories."),
        ("Kumbalangi Nights","Healing through love and family."),
        ("Jacobinte Swargarajyam","Optimism through adversity."),
        ("Maheshinte Prathikaaram","Gentle humor and humanity."),
        ("Android Kunjappan Version 5.25","Technology meets heart."),
        ("Guppy","An inspiring coming-of-age story."),
        ("Thinkalazhcha Nishchayam","Simple village joy."),
        ("Jo and Jo","Sibling fun and laughter."),
        ("Falimy","A family trip full of smiles."),
        ("Salt N' Pepper","Food and romance."),
        ("Philips and the Monkey Pen","A magical childhood adventure."),
        ("Rakshadhikari Baiju Oppu","Celebrate ordinary heroes."),
        ("Vikruthi","Kindness in unexpected places."),
        ("Sudani from Nigeria","Friendship beyond borders.")
    ],
    
"😂 Laugh It Out": [

    # 🌍 English
    ("The Hangover", "Chaos has never been this funny."),
    ("The Hangover Part II", "More madness, more laughter."),
    ("We're the Millers", "A fake family with real comedy."),
    ("Game Night", "A hilarious night gone completely wrong."),
    ("21 Jump Street", "Buddy comedy at its finest."),
    ("22 Jump Street", "Even funnier than the first."),
    ("The Nice Guys", "Action and comedy in perfect balance."),
    ("Free Guy", "A cheerful adventure with plenty of laughs."),
    ("Central Intelligence", "Unexpected friendship and comedy."),
    ("Spy", "One of the funniest spy movies ever."),
    ("Horrible Bosses", "Dark humor done right."),
    ("The Heat", "An unforgettable comedy duo."),
    ("Bruce Almighty", "Jim Carrey at his best."),
    ("Yes Man", "Say yes to laughter."),
    ("The Proposal", "Romance mixed with hilarious moments."),
    ("Crazy, Stupid, Love", "Heartwarming, romantic and genuinely funny."),
    ("Johnny English", "The world's most lovable spy."),
    ("Johnny English Reborn", "More spy disasters, more laughs."),
    ("Mr. Bean's Holiday", "Pure family-friendly comedy."),
    ("Rush Hour", "Jackie Chan and Chris Tucker never fail."),

    # 🇮🇳 Hindi
    ("Hera Pheri", "A comedy classic everyone should watch."),
    ("Phir Hera Pheri", "Twice the madness."),
    ("Munna Bhai M.B.B.S.", "Kindness wrapped in comedy."),
    ("Lage Raho Munna Bhai", "Laugh while learning life lessons."),
    ("Chup Chup Ke", "Comedy from start to finish."),
    ("Bhool Bhulaiyaa", "Horror meets hilarious comedy."),
    ("Hulchul", "Family chaos at its funniest."),
    ("Garam Masala", "Classic Akshay Kumar comedy."),
    ("Dhamaal", "Pure entertainment."),
    ("Golmaal: Fun Unlimited", "Friendship and endless laughs."),
    ("Welcome", "Iconic comedy performances."),
    ("Bhagam Bhag", "Non-stop confusion and comedy."),
    ("Malamaal Weekly", "Simple village humor."),
    ("Khosla Ka Ghosla", "A clever family comedy."),
    ("Fukrey", "Friendship and crazy adventures."),
    ("Fukrey Returns", "Even crazier than before."),
    ("Dream Girl", "A unique comedy."),
    ("OMG: Oh My God!", "Humor with a meaningful message."),
    ("Vicky Donor", "Fresh, funny and heartwarming."),
    ("Badhaai Ho", "Comedy rooted in family life."),

    # 🎬 Telugu
    ("Jathi Ratnalu", "One of Telugu cinema's funniest films."),
    ("MAD", "College comedy at its best."),
    ("Brochevarevarura", "Friendship, crime and hilarious moments."),
    ("Agent Sai Srinivasa Athreya", "Comedy mixed with mystery."),
    ("Mathu Vadalara", "Dark comedy done brilliantly."),
    ("Mathu Vadalara 2", "More laughs and craziness."),
    ("DJ Tillu", "Siddu's comedy is unforgettable."),
    ("Tillu Square", "Crazy fun continues."),
    ("Ami Thumi", "Feel-good comedy."),
    ("Ashta Chamma", "Simple and lovable humor."),
    ("Nuvvu Naaku Nachav", "Timeless comedy with heart."),
    ("Manmadhudu", "Nagarjuna's iconic entertainer."),
    ("Malliswari", "Family comedy everyone enjoys."),
    ("Venky", "Comedy gold."),
    ("Dhee", "One of the funniest Telugu entertainers."),
    ("Ready", "Comedy packed with romance."),
    ("King", "Nagarjuna's stylish comedy."),
    ("Ee Nagaraniki Emaindi", "Friendship and endless fun."),
    ("Happy", "Feel-good entertainer."),
    ("Adhurs", "Jr. NTR's comic timing shines."),

    # 🎼 Tamil
    ("Boss Engira Bhaskaran", "Santhanam's comedy is unforgettable."),
    ("Panchathanthiram", "Classic Kamal Haasan comedy."),
    ("Soodhu Kavvum", "Unique black comedy."),
    ("Kalakalappu", "Fun from beginning to end."),
    ("OK OK", "Romantic comedy done right."),
    ("Oru Kal Oru Kannadi", "Simple, enjoyable humor."),
    ("Nanban", "Friendship and comedy."),
    ("Doctor", "Dark comedy with action."),
    ("Mandela", "Satirical humor."),
    ("Vasool Raja MBBS", "Comedy with heart."),
    ("Michael Madana Kama Rajan", "A timeless classic."),
    ("Avvai Shanmugi", "Comedy masterpiece."),
    ("Thillu Mullu", "Legendary Tamil comedy."),
    ("Kanna Laddu Thinna Aasaiya", "Fun family entertainer."),
    ("SMS (Siva Manasula Sakthi)", "Romantic comedy favorite."),

    # 🎵 Malayalam
    ("Aadu", "Cult comedy."),
    ("Aadu 2", "Even crazier sequel."),
    ("Jan.E.Man", "Unexpectedly hilarious."),
    ("Romancham", "Comedy with horror elements."),
    ("Falimy", "Family comedy that feels real."),
    ("Jo and Jo", "Sibling rivalry and laughter."),
    ("Jaya Jaya Jaya Jaya Hey", "Empowering and funny."),
    ("Thinkalazhcha Nishchayam", "Village comedy at its finest."),
    ("Android Kunjappan Version 5.25", "Humor with emotion."),
    ("Kunjiramayanam", "Feel-good rural comedy."),
    ("Godha", "Sports, romance and comedy."),
    ("Minnal Murali", "Superhero fun with humor."),
    ("CID Moosa", "A Malayalam comedy legend."),
    ("Punjabi House", "One of the funniest Malayalam films."),
    ("Kilukkam", "A true comedy classic.")
]
,
"🌱 Hope & Healing": [

    # 🌍 English
    ("The Shawshank Redemption", "Hope is a powerful thing that no prison can take away."),
    ("Wonder", "Choose kindness whenever possible."),
    ("The Blind Side", "One act of kindness can change a life."),
    ("The Intouchables", "Friendship can heal even the deepest wounds."),
    ("October Sky", "Dreams grow stronger when you refuse to give up."),
    ("The Theory of Everything", "Love and determination overcome impossible odds."),
    ("Freedom Writers", "Education and compassion can transform lives."),
    ("The Boy Who Harnessed the Wind", "Never underestimate the power of hope."),
    ("Hidden Figures", "Talent and courage deserve to be seen."),
    ("The Bucket List", "It's never too late to truly live."),
    ("Lion", "Sometimes home is a journey."),
    ("Gifted Hands", "Persistence creates miracles."),
    ("Green Book", "Humanity is greater than our differences."),
    ("Remember the Titans", "Unity makes us stronger."),
    ("The Ultimate Gift", "Life's greatest treasures aren't money."),

    # 🇮🇳 Hindi
    ("Swades", "True change begins when we care for others."),
    ("Iqbal", "Dream big, no matter where you come from."),
    ("Super 30", "Knowledge changes lives."),
    ("Hichki", "Turn your weaknesses into strengths."),
    ("Rocket Singh", "Integrity is always worth it."),
    ("Bhaag Milkha Bhaag", "Keep running towards your dreams."),
    ("Chak De! India", "Together we achieve more."),
    ("Neerja", "Courage lives in ordinary people."),
    ("Maidaan", "Great leaders lift others."),
    ("Paan Singh Tomar", "A life shaped by choices."),
    ("Anand", "Live every moment with joy."),
    ("Nil Battey Sannata", "Education breaks barriers."),
    ("Taare Zameen Par", "Every child shines differently."),
    ("Lakshya", "Purpose changes everything."),
    ("Dangal", "Believe beyond limitations."),

    # 🎬 Telugu
    ("Major", "True heroes inspire generations."),
    ("Mallesham", "Innovation begins with determination."),
    ("Leader", "Leadership is about service."),
    ("Kanche", "Humanity is greater than war."),
    ("Ghazi", "Courage beneath the surface."),
    ("Oopiri", "Friendship heals broken hearts."),
    ("Godavari", "Sometimes peace is all we need."),
    ("Vedam", "Every life has value."),
    ("Jersey", "It's never too late to chase a dream."),
    ("C/o Kancharapalem", "Love exists everywhere."),

    # 🎼 Tamil
    ("Anbe Sivam", "Love is the greatest religion."),
    ("Soorarai Pottru", "Dreams belong to everyone."),
    ("Jai Bhim", "Justice begins with courage."),
    ("Mozhi", "Understanding is a form of love."),
    ("Abhiyum Naanum", "A parent's love lasts forever."),
    ("Deiva Thirumagal", "Love doesn't need perfection."),
    ("Peranbu", "Acceptance is powerful."),
    ("Ayothi", "Compassion changes lives."),
    ("Vaagai Sooda Vaa", "Education creates hope."),
    ("Kadaisi Vivasayi", "A simple life can be extraordinary."),

    # 🎵 Malayalam
    ("Uyare", "Rise above every setback."),
    ("#Home", "Family is our greatest comfort."),
    ("Ustad Hotel", "Purpose is found in serving others."),
    ("The Great Indian Kitchen", "Every voice deserves to be heard."),
    ("Jacobinte Swargarajyam", "Optimism wins."),
    ("Sudani from Nigeria", "Kindness has no borders."),
    ("Maheshinte Prathikaaram", "Healing comes with time."),
    ("Android Kunjappan Version 5.25", "Technology can never replace love."),
    ("Charlie", "Kindness is contagious."),
    ("Ayalum Njanum Thammil", "Growth comes through compassion.")
]

}

def movie_card(title, note):

    st.markdown("""
    <style>
    .movie-card{
    background:linear-gradient(145deg,#24153d,#1b1230);
    padding:22px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,.08);
    margin-bottom:22px;
    transition:0.3s;
    min-height:360px;      /* Make all cards the same height */
    display:flex;
    flex-direction:column;
    justify-content:space-between;
}

    .movie-card:hover{
        transform:translateY(-4px);
        box-shadow:0 12px 25px rgba(170,120,255,.25);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="movie-card">

        <h3 style="color:white;">
        🎬 {title}
        </h3>

        <div style="text-align:center; margin:10px 0 18px 0; font-size:26px;">
        💜
        </div>

        <p style="
        color:#ECE7FF;
        font-size:16px;
        line-height:1.8;
        text-align:justify;
        ">
       {note}
        </p>


        <hr style="
        border:none;
        border-top:1px solid rgba(255,255,255,.08);
        margin:20px 0;
        ">

        <p style="
        text-align:center;
        color:#C8B7F7;
        ">
        💜 I hope this story finds you at the right time.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


def comfort_movies():

    st.markdown("""
    <h1 style='text-align:center;'>
    🎬 Comfort on Screen
    </h1>

    <p style='text-align:center;
    color:#C7B6F5;
    font-size:18px;'>
    Movies that feel like a warm hug.
    </p>
    """, unsafe_allow_html=True)

    st.info(
        "💜 Every movie in this collection was chosen because it comforted, inspired, or reminded me that difficult days don't last forever. I hope one of these stories becomes your comfort too."
    )

    st.markdown("### 🌸 Choose a Collection")
    genre = st.selectbox(
    "",
    list(MOVIES.keys()),
    label_visibility="collapsed"
)
    search = st.text_input("🔍 Search Movies")

    movies = MOVIES[genre]

    if search:

        movies = [

            movie

            for movie in movies

            if search.lower() in movie[0].lower()

        ]

    st.markdown(
f"""
<div style="
background:#2B1D45;
padding:10px;
border-radius:12px;
text-align:center;
margin-bottom:25px;
color:#D9CCFF;
">

🎬 {len(movies)} Handpicked Movies

</div>
""",
unsafe_allow_html=True
)

    col1, col2 = st.columns(2)

    for i, (title, note) in enumerate(movies):

        if i % 2 == 0:

            with col1:

                movie_card(title, note)

        else:

            with col2:

                movie_card(title, note)
    st.markdown("---")




    st.markdown(
       """
       <div style='text-align:center;
       color:#C9B8F5;
       font-size:16px;
       padding-bottom:20px;'>

       🌸

      Every recommendation here was chosen
      with the hope that it brings someone
      comfort, hope, or simply a smile.

      Thank you for visiting the Comfort Library.

       </div>
       """,
       unsafe_allow_html=True
)
    

def comfort_library_page():

    gentle_reminder()

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<h1 style='text-align:center;
margin-top:10px;'>
📚 Explore the Comfort Library
</h1>

<p style='text-align:center;
color:#C7B6F5;
font-size:18px;
margin-top:-5px;
margin-bottom:25px;'>

Choose what your heart needs today. 💜
</p>
""", unsafe_allow_html=True)

    option = st.selectbox(
        "",
        [
            "🎵 Music Therapy",
            "🎬 Comfort Movies & Series",
            "📖 Wisdom Stories",
            "📚 Books for the Mind"
        ],
        index=None,
        placeholder="Choose a section..."
    )

    if option == "🎵 Music Therapy":
        music_therapy()

    elif option == "🎬 Comfort Movies & Series":
         comfort_movies()

    elif option == "📖 Wisdom Stories":
        inspirational_stories()

    elif option == "📚 Books for the Mind":
        books_page()