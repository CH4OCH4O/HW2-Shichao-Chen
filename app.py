import os
from google import genai


PROMPT = """
You are a helpful customer support assistant for an e-commerce company.

Write a professional email reply to the customer.

Requirements:
- Be polite and professional
- Acknowledge the customer's issue
- Keep the response clear and concise
"""

def main():
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set.")

    
    client = genai.Client(api_key=api_key)

    
    customer_message = input("Enter customer message:\n> ").strip()

    if not customer_message:
        print("No input provided.")
        return

    
    full_prompt = f"{PROMPT}\n\nCustomer message:\n{customer_message}"

    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt
    )

    result = response.text

    
    print("\n=== GENERATED RESPONSE ===\n")
    print(result)

    
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("=== CUSTOMER MESSAGE ===\n")
        f.write(customer_message + "\n\n")
        f.write("=== GENERATED RESPONSE ===\n")
        f.write(result)

    print("\nSaved to output.txt")

if __name__ == "__main__":
    main()
