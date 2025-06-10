import random
import streamlit as st
from textblob import TextBlob

COLOR_COMBINATIONS = {
    "black": ["white", "gold", "red", "grey", "silver"],
    "white": ["blue", "black", "pastel shades", "olive green", "lavender"],
    "beige": ["pastel pink", "brown", "rust", "white"],
    "navy blue": ["mustard yellow", "white", "grey", "light grey"],
    "lavender": ["mint green", "grey", "white", "pastel pink"],
    "red": ["denim blue", "black", "cream", "white", "gold"],
    "olive green": ["cream", "rust", "white", "brown"],
    "grey": ["black", "red", "navy blue", "pastel pink"],
    "brown": ["beige", "cream", "mustard", "rust"],
    "pastel pink": ["white", "beige", "light grey", "lavender"],
    "mustard yellow": ["navy blue", "brown", "white", "olive green"],
    "mint green": ["lavender", "white", "peach", "pink"],
    "peach": ["mint green", "cream", "light brown"],
    "denim blue": ["white", "red", "grey", "mustard"],
    "rust": ["cream", "olive green", "brown", "beige"],
    "cream": ["brown", "olive green", "pastel pink", "mint green"],
    "light grey": ["navy blue", "white", "pastel tones", "black"],
    "yellow": ["white", "blue", "black", "grey"],
    "orange": ["white", "brown", "beige", "green"],
    "green": ["white", "black", "peach", "yellow", "denim blue"],
    "blue": ["white", "yellow", "grey", "pink"],
    "purple": ["white", "pink", "grey", "black"],
    "pink": ["white", "light grey", "beige", "lavender"],
    "gold": ["black", "emerald green", "white", "red"],
    "silver": ["black", "navy blue", "white"]
}

FASHION_TRENDS = [
    "Y2K aesthetic",
    "Oversized blazers",
    "Baggy jeans & crop tops",
    "Statement belts",
    "Chunky sneakers",
    "Matching coords",
    "Minimalist neutral tones",
    "Sporty streetwear",
    "Utility fashion with pockets",
    "Denim on denim",
    "Sheer fabrics & mesh tops",
    "Corset tops",
    "Platform boots",
    "Graphic tees with vintage vibes",
    "Layered necklaces & stacked rings",
    "Maxi skirts with slits",
    "Satin slip dresses",
    "Balaclavas & funky headwear",
    "Tote bags with quotes",
    "Monochrome outfits",
    "Retro sunglasses",
    "Cargo pants",
    "Puffy jackets & bomber styles",
    "Lace & leather mix",
    "Asymmetrical cuts"
]

OOTD_SUGGESTIONS = [
    "High-waist jeans + relaxed tee + sneakers",
    "Oversized shirt + straight pants + crossbody bag",
    "Flared trousers + plain tee + boots",
    "Denim jacket + cargo pants + basic tee",
    "Co-ord set + minimal accessories",
    "Satin shirt + wide-leg jeans + heels",
    "Crop top + midi skirt + sandals",
    "Slip dress + denim jacket + ankle boots",
    "Graphic tee + pleated skirt + chunky sneakers",
    "Corset top + ripped jeans + strappy heels",
    "Turtleneck + mini skirt + knee-high boots",
    "Off-shoulder top + mom jeans + platform sneakers",
    "Basic tank + palazzo pants + statement earrings",
    "Blazer dress + belt + thigh-high boots",
    "Baggy hoodie + biker shorts + dad sneakers",
    "Mesh top + bralette + wide-leg trousers",
    "Oversized sweater + skater skirt + ankle boots",
    "Crop hoodie + joggers + high-top sneakers",
    "Lace top + leather pants + kitten heels",
    "Asymmetrical top + culottes + mules"
]

STYLE_TIPS = [
    "Add a belt to instantly elevate a simple dress.",
    "Layering is key for a stylish and dynamic outfit.",
    "Mix textures like denim, leather, and cotton for contrast.",
    "Always balance oversized and fitted pieces.",
    "Accessories can change the entire vibe of your outfit.",
    "Tuck in your top to define your waist and elongate your legs.",
    "Statement earrings can glam up even the most basic look.",
    "Play with proportions to add dimension and interest.",
    "Use a pop of color in your bag or shoes for bold impact.",
    "Monochrome outfits always look effortlessly chic.",
    "Don’t be afraid to mix prints—stripes and florals can totally work.",
    "Neutral tones are timeless and easy to style.",
    "A good pair of sunglasses adds instant edge.",
    "Sneakers go with more than just casual outfits—rock them with dresses too.",
    "Roll up your sleeves or pants slightly to show off bracelets or shoes.",
    "Confidence is your best accessory—wear it loud!",
    "Invest in quality basics—they’re your everyday fashion foundation.",
    "Know your body type and dress to highlight your best features.",
    "Don’t follow trends blindly—make them work for *your* vibe.",
    "Add one standout piece to every outfit for a signature slay."
]

UNDERTONE_RECOMMENDATIONS = {
    "cool": "Cool undertones look great in jewel tones like emerald, sapphire, and amethyst. Silver jewelry enhances the look.",
    "warm": "Warm undertones shine in earthy tones like orange, brown, yellow, and gold. Gold jewelry complements this the best.",
    "neutral": "Neutral undertones can pull off a wide range of colors, including both cool and warm shades, like muted greens, blush, and navy."
}

BODY_TYPE_RECOMMENDATIONS = {
    "hourglass": "Try fitted tops and pencil skirts or high-waisted pants to accentuate your curves. Avoid overly baggy clothes.",
    "pear": "A-line dresses and skirts, as well as top-heavy outfits (like puff sleeves), balance your proportions. Avoid wide-leg pants.",
    "apple": "Empire waistlines and flowy dresses will add shape without clinging to your midsection. Go for V-necklines to elongate your torso.",
    "rectangle": "Define your waist with belted dresses or tops, and create curves with peplum designs. Layering works great for you."
}

OCCASION_DRESS_ADVICE = {
    "casual": [
        "For a casual day out, go for comfortable yet stylish options like a loose tee, denim jeans, and sneakers.",
        "A pair of leggings, oversized sweater, and ankle boots make a perfect casual outfit.",
        "Casual dresses with floral prints, paired with flat sandals, work great for warm weather."
    ],
    "formal": [
        "For formal events, opt for tailored suits, dresses with clean lines, or a fitted blazer.",
        "A sleek, monochrome dress with minimal accessories is perfect for a formal dinner.",
        "A high-waisted pencil skirt and a fitted blouse paired with heels is ideal for a business formal look."
    ],
    "party": [
        "A party look should include bold pieces like a bodycon dress or sequined top paired with heels.",
        "For a fun night out, a mini skirt with a cropped top and stilettos makes a trendy party outfit.",
        "Rock a metallic dress with statement earrings and a clutch bag for a chic party look."
    ],
    "date": [
        "For a romantic date, opt for a flowy midi dress paired with soft curls and a pair of ballet flats.",
        "A cute off-shoulder blouse with skinny jeans and a pair of wedges is perfect for a casual date.",
        "A fitted dress with a cinched waist and heels works wonders for a dinner date."
    ],
    "wedding": [
        "For a wedding guest, a floral wrap dress or an elegant cocktail dress paired with nude heels works well.",
        "Opt for a long, flowing gown with a subtle shimmer for a sophisticated wedding look.",
        "A pastel-colored dress with minimal jewelry and a chic clutch is a safe bet for a wedding event."
    ],
    "work": [
        "A button-down shirt tucked into a high-waisted skirt or tailored trousers gives a professional yet stylish vibe.",
        "A shift dress with a blazer is always a go-to work outfit.",
        "Opt for a structured blazer over a blouse and straight-leg trousers for a power look at work."
    ],
    "vacation": [
        "For a beach vacation, go for a flowy sundress, sandals, and a wide-brimmed hat.",
        "A comfy pair of shorts, a tank top, and slip-on shoes are perfect for exploring a new city on vacation.",
        "When traveling to cooler destinations, opt for a cozy sweater, jeans, and a stylish jacket."
    ],
    "brunch": [
        "For brunch, go for a cute wrap dress or a skirt with a tucked-in blouse, paired with comfortable flats.",
        "A pair of high-waisted trousers with a tucked-in button-up shirt makes a fashionable and effortless brunch look.",
        "A casual yet chic romper with espadrilles works great for a daytime brunch."
    ]
}

class SlayBot:
    def __init__(self):
        pass

    def extract_color(self, prompt):
        blob = TextBlob(prompt)
        for word in blob.words:
            word_lower = word.lower()
            if word_lower in COLOR_COMBINATIONS:
                return word_lower
        return None

    def extract_undertone(self, prompt):
        prompt = prompt.lower()
        if "cool" in prompt:
            return "cool"
        elif "warm" in prompt:
            return "warm"
        elif "neutral" in prompt:
            return "neutral"
        return None

    def extract_body_type(self, prompt):
        prompt = prompt.lower()
        for body_type in ["hourglass", "pear", "apple", "rectangle"]:
            if body_type in prompt:
                return body_type
        return None

    def extract_occasion(self, prompt):
        prompt = prompt.lower()
        if "casual" in prompt:
            return "casual"
        elif "formal" in prompt:
            return "formal"
        elif "party" in prompt:
            return "party"
        elif "date" in prompt:
            return "date"
        elif "wedding" in prompt:
            return "wedding"
        elif "work" in prompt:
            return "work"
        elif "vacation" in prompt:
            return "vacation"
        elif "brunch" in prompt:
            return "brunch"
        return None

    def respond(self, prompt):
        prompt = prompt.lower()

        if "color" in prompt or "goes with" in prompt or "match with" in prompt or "color combo" in prompt:
            color = self.extract_color(prompt)
            if color:
                options = COLOR_COMBINATIONS[color]
                return f"{color.title()} pairs well with {', '.join([c.title() for c in options])}. Try mixing and matching!"
            else:
                return "I couldn't detect the base color. Try rephrasing your question."

        elif "trend" in prompt or "trending" in prompt or "what's in" in prompt:
            return f"Hot trend alert! {random.choice(FASHION_TRENDS)} is super in right now."

        elif "ootd" in prompt or "outfit" in prompt or "wear" in prompt or "today" in prompt:
            occasion = self.extract_occasion(prompt)
            if occasion:
                return random.choice(OCCASION_DRESS_ADVICE[occasion])
            return f"Here's an outfit idea for you: {random.choice(OOTD_SUGGESTIONS)}"
     
        elif "tip" in prompt or "advice" in prompt or "style me" in prompt:
            return f"Style tip: {random.choice(STYLE_TIPS)}"

        elif "help" in prompt or "what can you do" in prompt:
            return ("SlayBot can help you with:\n"
                    "- Color combinations (e.g., 'What goes with red?')\n"
                    "- Latest fashion trends (e.g., 'What's trending?')\n"
                    "- Outfit of the day ideas (e.g., 'Give me an OOTD')\n"
                    "- Styling tips (e.g., 'Give me a fashion tip')\n"
                    "- Undertone advice (e.g., 'What colors suit my cool undertone?')\n"
                    "- Body type recommendations (e.g., 'What should I wear for an hourglass figure?')\n"
                    "- Occasion-based dress advice (e.g., 'What should I wear to a party?')")

        elif "undertone" in prompt:
            undertone = self.extract_undertone(prompt)
            if undertone:
                return UNDERTONE_RECOMMENDATIONS[undertone]
            return "Please mention whether your undertone is cool, warm, or neutral."

        elif any(bt in prompt for bt in ["hourglass", "pear", "apple", "rectangle", "body type"]):
            body_type = self.extract_body_type(prompt)
            if body_type:
                return BODY_TYPE_RECOMMENDATIONS[body_type]
            return "Please mention your body type (hourglass, pear, apple, rectangle)."

        elif "occasion" in prompt:
            occasion = self.extract_occasion(prompt)
            if occasion:
                return OCCASION_DRESS_ADVICE[occasion]
            return "Please mention the occasion (casual, formal, party)."

        else:
            return "Hmm... I'm not sure I understood that. Try asking about colors, trends, outfits, or styling tips."

# Streamlit UI
bot = SlayBot()
st.set_page_config(page_title="SlayBot - AI Fashion Assistant", page_icon="💅")
st.title("💅SlayBot - Your AI Fashion Assistant")
st.markdown("_Talk to your AI stylist! Ask about colors, trends, outfits or tips._")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Ask me something fashionable...")

if user_input:
    response = bot.respond(user_input)
    st.session_state.history.append((user_input, response))

for q, a in st.session_state.history:
    with st.chat_message("user"):
        st.markdown(f"🗣️ {q}")
    with st.chat_message("assistant"):
        st.markdown(f"👗 {a}")