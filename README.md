# LangChain Structured Output

This repository contains simple examples of **structured output in LangChain** using **Pydantic** and **TypedDict**.

The examples show how an LLM can return information in a fixed and structured format instead of returning only plain text.

## Files

```text
Langchain_structured_output_4/
│
├── env.txt
├── pydantic_demo.py
├── typeddict_demo.py
└── with_structured_output_typeddict.py
```

### `pydantic_demo.py`

Example of using **Pydantic** with LangChain to define the expected structure of the LLM output.

Pydantic is useful when you want the output to follow a specific schema with defined fields and data types.

### `typeddict_demo.py`

Basic example of using Python's **TypedDict** to define the expected structure of the response.

### `with_structured_output_typeddict.py`

Example of using LangChain's `with_structured_output()` with a `TypedDict` schema.

This makes it easier to get the model response in the required structure.

### `env.txt`

Contains environment/configuration information required for running the examples.

**Do not upload API keys or other private credentials to GitHub.**

---

## What is Structured Output?

Normally, an LLM can return something like:

```text
Name: Laxman
Age: 23
Role: Data Scientist
```

With structured output, we can define the format we want:

```text
{
    "name": "Laxman",
    "age": 23,
    "role": "Data Scientist"
}
```

This is useful when the output needs to be used by another part of an application.

---

## Pydantic vs TypedDict

| Pydantic | TypedDict |
|---|---|
| Provides data validation | Mainly defines the expected structure |
| Uses Python types | Uses Python type hints |
| Useful when validation is important | Simple and lightweight |
| Can be used to create structured models | Useful for defining dictionary-like output |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/laxmankhedkar/Langchain_structured_output_4.git
```

Move into the project:

```bash
cd Langchain_structured_output_4
```

Install the required packages:

```bash
pip install langchain langchain-openai pydantic python-dotenv
```

---

## API Key

If the examples use an OpenAI model, add your API key through an environment variable.

For example:

```text
OPENAI_API_KEY=your_api_key_here
```

Keep your API key private and do not commit it to GitHub.

---

## Run the Examples

Run the Pydantic example:

```bash
python pydantic_demo.py
```

Run the TypedDict example:

```bash
python typeddict_demo.py
```

Run the structured output example:

```bash
python with_structured_output_typeddict.py
```

---

## Main Concepts

The repository covers:

- LangChain structured output
- Pydantic
- TypedDict
- `with_structured_output()`
- LLM response schemas
- Type hints
- Structured data from LLMs

---

## Why Structured Output?

Structured output is useful when building applications where the LLM response needs to be processed by code.

For example:

```text
User Input
    ↓
LLM
    ↓
Structured Output
    ↓
Python Application
    ↓
Database / API / RAG / UI
```

It is commonly useful for:

- Information extraction
- Data processing
- API responses
- RAG applications
- AI agents
- Classification
- Form/document processing

---

## Author

**Laxman Khedkar**

GitHub: [laxmankhedkar](https://github.com/laxmankhedkar)
