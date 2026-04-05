# Evaluation Set

This evaluation set is designed for a GenAI workflow that drafts customer support responses for an e-commerce business. The goal is to test whether the model can produce clear, polite, and useful first-draft replies across common and risky customer situations.

## Case 1 - Normal case
**Input:**  
Hi, my order was supposed to arrive three days ago, but I still have not received it. Can you check the status?

**What a good output should do:**  
A good response should apologize politely, acknowledge the late delivery, and say that the issue will be checked. It should sound professional and helpful.

---

## Case 2 - Normal case
**Input:**  
I received my package today, but the product inside was damaged. The screen is cracked. What can I do?

**What a good output should do:**  
A good response should show empathy, acknowledge the damaged item, and explain the next step clearly. It should not blame the customer.

---

## Case 3 - Edge case
**Input:**  
I ordered two items, but only one arrived. The tracking page says delivered. Please help.

**What a good output should do:**  
A good response should recognize that this may be a partial shipment or delivery issue. It should avoid making unsupported assumptions and may ask for more order details if needed.

---

## Case 4 - Likely failure / needs human review
**Input:**  
This is the second time this happened. Your company is clearly scamming people. If I do not get my money back today, I will report this everywhere.

**What a good output should do:**  
A good response should stay calm, respectful, and professional. It should de-escalate the situation, avoid defensive language, and suggest escalation or human review if needed.

---

## Case 5 - Hallucination risk
**Input:**  
I want a full refund for my custom-made product. Your website says all items can be refunded within 30 days, so process it now.

**What a good output should do:**  
A good response should avoid inventing refund policy details. It should not claim policy terms unless confirmed. It should respond carefully and note that this case may require policy review or human review.