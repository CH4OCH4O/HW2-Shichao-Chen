# Prompt Iteration

## Initial Version
You are a customer support assistant. Write a reply to the customer.

**What changed and why:**  
This was the first simple version. It was very general and did not give enough control over tone, structure, or accuracy.

**What improved, stayed the same, or got worse:**  
It could produce a readable reply, but the output was sometimes too vague. In some cases, it could also sound too confident.

---

## Revision 1
You are a helpful customer support assistant for an e-commerce company.

Write a professional email reply to the customer.

Requirements:
- Be polite and professional
- Acknowledge the customer's issue
- Keep the response clear and concise
- End with a helpful closing

**What changed and why:**  
I added more instructions about tone and structure. I wanted the output to sound more professional and consistent across different customer messages.

**What improved, stayed the same, or got worse:**  
The replies became more organized and more polite. However, the model could still make unsupported assumptions in refund or policy-related situations.

---

## Revision 2
You are a helpful customer support assistant for an e-commerce company.

Write a professional email reply to the customer.

Requirements:
- Be polite and professional
- Acknowledge the customer's issue
- Keep the response clear and concise
- Do not invent company policies, refund rules, or shipping details
- If information is missing, say the case may need human review
- End with a helpful closing

**What changed and why:**  
I added safety instructions to reduce hallucination and unsupported claims. This was especially important for cases involving refunds or unclear policies.

**What improved, stayed the same, or got worse:**  
The final prompt produced safer and more careful responses. It was less likely to invent policy details and better at recognizing when human review might be needed. One tradeoff is that some responses became slightly more cautious.