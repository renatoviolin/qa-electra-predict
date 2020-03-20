import pprint
from qa_predict import predict, init_model

model = init_model()

context = "Google was founded in 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its share and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a privately held company on September 4, 1998. An initial public offering (IPO) took place on August 19, 2004, and Google moved to its headquarters in Mountain View, California, nicknamed the Googleplex. In August 2015, Google announced plans to reorganize its various interests as a conglomerate called Alphabet Inc. Google is Alphabet leading subsidiary and will continue to be the umbrella company for Alphabets Internet interests. Sundar Pichai was appointed CEO of Google, replacing Larry Page who became the CEO of Alphabet."
questions = ['who founded google', 'where is the headquarter of google', 'when google was founded?', 'who replaced larry page']
response = predict(questions, context, model)


print('\n====== CONTEXT =====')
print(context)
print()

print('====== QUESTIONS =====')
for i, q in enumerate(questions):
    print(f'q_{i}: {q}')
print()

print('====== RESPONSE ====')
for i, res in enumerate(response.items()):
    print(f'r_{i}: {res[1][0]["text"]}')

print('\n====== ALL RESPONSES DICT====')
pprint.pprint(response)
