import ollama
import codecs

with codecs.open(
    "../given/practical10/alzheimers-facts.txt",
    "rb",
    encoding="utf-8",
    errors="gignore",
) as fdata:
    dataset = fdata.readlines()

    embedModel = "hf.co/CompendiumLabs/bge-base-en-v1.5-gguf"
    langModel = "hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF"


vecDb = []


def add_chunk_to_database(chunk):
    embedding = ollama.embed(embedModel, input=chunk)["embeddings"][0]
    vecDb.append((chunk, embedding))


print("learning")
for i, data in enumerate(dataset):
    add_chunk_to_database(data)

print("finished")


def cosine_similarity(a, b):
    dot_product = sum([x * y for x, y in zip(a, b)])
    norm_a = (sum([x**2 for x in a])) ** 0.5
    norm_b = (sum([x**2 for x in b])) ** 0.5
    return dot_product / (norm_a * norm_b)


def retrieve(query, top_n=3):
    qEmbed = ollama.embed(embedModel, input=query)["embeddings"][0]
    similarities = []
    for chunk, embedding in vecDb:
        similarity = cosine_similarity(embedding, qEmbed)
        similarities.append((chunk, similarity))
        similarities.sort(key=lambda x: x[1], reverse=False)
    return similarities[:top_n]


while True:
    query = input("Enter question:(press q to exit):")
    if query.lower().strip() == "q":
        break

    similarities = retrieve(query)
    prompt = (
        "You are clever chatbot that knows about alzheimers and only answer as the text provided to you. Context is:"
        + ",".join([chunk for chunk, similarity in similarities])
    )

    stream = ollama.chat(
        model=langModel,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": query},
        ],
        stream=True,
    )

    print("Response:")
    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)

    print()
    print("=======")
    print()
