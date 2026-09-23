"""
semantic_routing_guardrails.py
==============================

Semantic routing + guardrails demo using **LangChain** and **Gemini 3.8 Flash**.

Components
----------
1. ``classifier_chain``  – outputs ONLY one of: TOXIC | CODE_REQUEST | GENERAL
2. ``toxic_chain``       – RunnableLambda, hard-coded rejection
3. ``code_chain``        – LLMChain, answers programming questions
4. ``general_chain``     – LLMChain, politely refuses non-programming questions
5. ``RunnableBranch``    – routes input based on classifier output

Run
---
    pip install langchain langchain-google-genai google-genai
    export GOOGLE_API_KEY=...
    python semantic_routing_guardrails.py
"""

import os
import re
from typing import Any

# --------------------------------------------------------------------------- #
#  LangChain imports
# --------------------------------------------------------------------------- #
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI

# --------------------------------------------------------------------------- #
#  1. classifier_chain  – outputs ONLY one of: TOXIC / CODE_REQUEST / GENERAL
# --------------------------------------------------------------------------- #
classifier_llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.0,
    api_key=os.getenv("GOOGLE_API_KEY"),
)

# Force single-word output with a strict system prompt.
classifier_chain = (
    RunnablePassthrough()  # passes the raw user input through unchanged
    | RunnableLambda(
        lambda text: classifier_llm.invoke(
            [
                SystemMessage(
                    "You are a strict classifier. Reply with EXACTLY ONE "
                    "WORD from this set: TOXIC, CODE_REQUEST, GENERAL. "
                    "Nothing else."
                ),
                HumanMessage(text),
            ]
        )
    )
    | RunnableLambda(
        lambda response: re.sub(r"[^A-Za-z_]", "", response.content).upper().strip()
    )
)

# --------------------------------------------------------------------------- #
#  2. toxic_chain  – hard-coded guardrail rejection
# --------------------------------------------------------------------------- #
toxic_chain = RunnableLambda(
    lambda _: "Security Violation: Prompt rejected."
)

# --------------------------------------------------------------------------- #
#  3. code_chain  – real LLM answers programming questions
# --------------------------------------------------------------------------- #
code_llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.2,
    api_key=os.getenv("GOOGLE_API_KEY"),
)

# --------------------------------------------------------------------------- #
#  4. general_chain  – politely refuses non-programming questions
# --------------------------------------------------------------------------- #
general_llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.2,
    api_key=os.getenv("GOOGLE_API_KEY"),
)

general_chain = RunnableLambda(
    lambda text: (
        "I'm designed to help with programming and technical questions only. "
        "I can't assist with that, but I'd be happy to help with a coding topic!"
    )
)

# --------------------------------------------------------------------------- #
#  5. RunnableBranch  – route based on classifier output
# --------------------------------------------------------------------------- #
def _is_toxic(label: str) -> bool:
    return label == "TOXIC"


def _is_code(label: str) -> bool:
    return label == "CODE_REQUEST"


routing_chain = RunnableBranch(
    (
        _is_toxic,
        toxic_chain,
    ),
    (
        _is_code,
        RunnablePassthrough(),  # passes original text into code_chain below
    ),
)

# Full pipeline: input -> classifier -> branch -> destination
full_chain = (
    RunnablePassthrough()
    | RunnableLambda(
        lambda text: (
            text,
            classifier_chain.invoke(text),
        )
    )
    | RunnableLambda(
        lambda pair: (
            pair[0],
            pair[1],
            routing_chain.invoke(pair[1]),
        )
    )
)

# --------------------------------------------------------------------------- #
#  Tests
# --------------------------------------------------------------------------- #
SAMPLES = [
    ("You're a complete idiot and you should just shut up!", "TOXIC"),
    ("How do I reverse a list in Python?", "CODE_REQUEST"),
    ("How do I bake a chocolate cake?", "GENERAL"),
]


def main():
    print("=" * 64)
    print("Semantic Routing + Guardrails  (LangChain + Gemini 3.8 Flash)")
    print("=" * 64)

    for text, expected_label in SAMPLES:
        # Step 1: classify
        label = classifier_chain.invoke(text)

        # Step 2: route and get response
        if _is_toxic(label):
            response = toxic_chain.invoke(text)
        elif _is_code(label):
            # Use the real code_chain LLM for code questions
            response = code_llm.invoke(
                [
                    SystemMessage(
                        "You are a helpful programming assistant. "
                        "Answer the coding question clearly with examples."
                    ),
                    HumanMessage(text),
                ]
            ).content
        else:
            response = general_chain.invoke(text)

        status = "OK" if label == expected_label else "MISMATCH"
        print(f"\n[INPUT]     {text}")
        print(f"[CLASSIFY]  -> {label}  (expected {expected_label})  [{status}]")
        print(f"[RESPONSE]  {response}")

    print("\n" + "=" * 64)
    print("All samples processed.")
    print("=" * 64)


if __name__ == "__main__":
    main()
