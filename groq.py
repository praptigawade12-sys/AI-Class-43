import config
from openai import OpenAI

GROQ_URL = "https://api.groq.com/openai/v1"

MODELS = [

"llama-3-8b-8192",

"llama-3-70b-8192"

]

def generate_response(prompt: str, temperature: float = 0.3, max_tokens: int = 512) -> str:
    key = config.GROQ_API_KEY
    print("GROG",key)
    if not key:
        return "Error: GROQ_API_KEY is missing in groq.py"
    c = OpenAI(api_key=key, base_url=GROQ_URL)

    last_err = None
    for m in MODELS:
        try:
            r = c.chat.completions.create(
                model=m,
                messages=[{"role":"user","content":prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            return r.choices[0].content
        except Exception as e:
            last_err = e

    return(
        "Groq model failed. \n"
        f"Tried models: {MODELS}\n"
        f"Details {type(last_err).__name__}: {last_err}"
    )
