import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("AIzaSyDxXLH0Ek5C6qjHYmmL-Fyazz-7iEZX8dI"))

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
  
def run_advisor_agent(stock_info: dict, risk_profile: str):
    prompt = open("prompts/advisor_prompt.txt").read().format(
        name=stock_info["Name"],
        sector=stock_info["Sector"],
        industry=stock_info["Industry"],
        market_cap=stock_info["Market Cap"],
        price=stock_info["Current Price"],
        high=stock_info["52 Week High"],
        low=stock_info["52 Week Low"],
        pe=stock_info["PE Ratio"],
        dividend=stock_info["Dividend Yield"],
        risk_profile=risk_profile
    )

    response = model.generate_content(prompt)
    return response.text
