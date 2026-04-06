# Report: Simple GenAI Workflow for Customer Support Response Drafting

## Business Use Case

In this project, I built a simple GenAI workflow for drafting customer support responses in an e-commerce setting. Customer support teams often receive many similar messages every day, such as delivery delays, damaged products, or refund requests. Writing these responses manually can take time and may lead to inconsistency.

The goal of this workflow is to generate a first draft of a response based on the customer’s message. The user is a customer support employee. The input is a customer message, and the output is a professional email reply. This task is suitable for partial automation because many responses follow similar patterns, but still require human judgment in some situations.

## Model Choice

I chose to use Gemini through Google AI Studio because it is easy to access and provides a simple API for building a prototype. It was convenient to integrate into a Python script, and the model was able to generate clear and readable responses for business communication tasks.

I did not test many other models in this project, but Gemini was sufficient for this assignment since the goal was to build a small and reproducible workflow rather than a production system.

## Baseline vs Final Design

The baseline version of the system used a very simple prompt that only asked the model to write a reply to the customer. While this version could generate understandable responses, it often lacked structure and sometimes sounded too general.

In the second version, I added more specific instructions about tone and structure. I required the model to be polite, professional, and clear. This improved the consistency of the output and made the responses more suitable for a business context.

In the final version, I added constraints to reduce hallucination. For example, the model was instructed not to invent company policies or refund rules. It was also told to indicate when human review might be needed. This made the responses safer, especially in cases involving refunds or unclear situations.

Overall, prompt iteration improved both the quality and reliability of the generated responses.

## Remaining Limitations

The prototype still has several limitations. It does not have access to real order data, shipping systems, or company policies. Because of this, it cannot verify facts or provide accurate case-specific answers.

In some situations, the model may still produce responses that sound confident but are not fully correct. It also cannot properly handle complex or sensitive cases, such as legal issues, repeated complaints, or high-risk refund requests.

Another limitation is that the system only works as a text-based prototype and does not include integration with real business systems.

## Recommendation

I would recommend using this workflow as a draft-generation tool rather than a fully automated system. It can help customer support staff save time by generating a first draft quickly, but the final response should always be reviewed by a human.

Human review is especially important for cases involving refunds, policy interpretation, or customer escalation. With proper human oversight, this workflow can improve efficiency and consistency. However, it should not be deployed as a fully autonomous system without additional safeguards.