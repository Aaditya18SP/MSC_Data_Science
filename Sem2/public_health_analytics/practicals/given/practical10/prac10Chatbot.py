#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import ollama
import codecs


# In[ ]:


dataset = []

with codecs.open(
    "alzheimers-facts.txt", "r", encoding="utf-8", errors="ignore"
) as fdata:

    dataset = fdata.readlines()
    print(f"Loaded {len(dataset)} entries")
    # Implement the retrieval system

   


# In[ ]:


# Each element in the VECTOR_DB will be a tuple (chunk,embedding)
# The embedding is a list of floats, for example: [0.1, 0.04, -0.34,0.21, ...]
VECTOR_DB = []


# In[ ]:


def add_chunk_to_database(chunk):
    embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk)["embeddings"][0]
    VECTOR_DB.append((chunk, embedding))


print("Learning...")
for i, chunk in enumerate(dataset):
    add_chunk_to_database(chunk)
    # print(f'Added chunk {i+1}/{len(dataset)} to the database')
print("Learning done.")


# In[ ]:


def cosine_similarity(a, b):
    dot_product = sum([x * y for x, y in zip(a, b)])
    norm_a = sum([x**2 for x in a]) ** 0.5
    norm_b = sum([x**2 for x in b]) ** 0.5
    return dot_product / (norm_a * norm_b)


# In[ ]:


def retrieve(query, top_n=3):
    query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)["embeddings"][0]
    # temporary list to store (chunk, similarity) pairs
    similarities = []
    for chunk, embedding in VECTOR_DB:
        similarity = cosine_similarity(query_embedding, embedding)

        similarities.append((chunk, similarity))
        # sort by similarity in descending order, because higher similarity means more relevant chunks
        similarities.sort(key=lambda x: x[1], reverse=True)
        # finally, return the top N most relevant chunks
    return similarities[:top_n]


# # Chatbot

# In[ ]:


while True:
    input_query = input("\n\n ❓Ask me a question (Press `q` to exit): ")
    if input_query.lower() == "q":
        break
    retrieved_knowledge = retrieve(input_query)

    # print("Retrieved knowledge:")
    # for chunk, similarity in retrieved_knowledge:
    # print(f" - (similarity: {similarity:.2f}) {chunk}")

    instruction_prompt = f"""You are a helpful chatbot. Use only the following pieces of context to answer the question.Don't make up any new information:{' '.join([f' - {chunk}' for chunk, similarity in retrieved_knowledge])}"""
    # print(instruction_prompt)

    # In[ ]:

    stream = ollama.chat(
        model=LANGUAGE_MODEL,
        messages=[
            {"role": "system", "content": instruction_prompt},
            {"role": "user", "content": input_query},
        ],
        stream=True,
    )

    # In[ ]:

    # print the response from the chatbot in real-time
    print("👉Chatbot response:")
    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)

    print()
    print(
        "================================================================================="
    )
    print()
