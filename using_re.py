import json
import re

def prepare_qa_pairs(json_data):
    qa_pairs = []
    for item in json_data['data']:
        title = item['title']
        context = item['context']

        sentences = re.split(r'(?<=[.!?])\s+', context)
        for sentence in sentences:
            sentence = re.sub(r'[^\w\s]', '', sentence).strip()

            if sentence:
                question = f"What is {sentence}?"
                answer = sentence
                qa_pairs.append({"question": question, "answer": answer, "context": context})

        question = f"What can you tell me about {title}?"
        answer = title
        qa_pairs.append({"question": question, "answer": answer, "context": context})

    return qa_pairs

with open('output_context.json', 'r') as file:
    json_data = json.load(file)

qa_pairs = prepare_qa_pairs(json_data)

output_data = {'data': []}
for item in json_data['data']:
    title = item['title']
    context = item['context']
    entry = {'title': title, 'context': context, 'qa_pairs': []}

    for pair in qa_pairs:
        if pair['context'] == context:
            entry['qa_pairs'].append({"question": pair['question'], "answer": pair['answer']})

    output_data['data'].append(entry)

with open('output_qa.json', 'w') as file:
    json.dump(output_data, file, indent=2)
