# qa-electra-predict
Implementing a predict function to use with electra model fine tuned in squad 2.0.

To test yourself you need to adjust the variables at qa_predict.py:
- DATA_MODEL_DIR: folder where all files and tf_records will be created
- INIT_CHECKPOINT: this folder must have the checkpoint and the vocab.txt file from original electra-large.

You don't need to keep the original electra-large files and checkpoints.

If you run the run_predict.py, this will be the expected result:

```
====== CONTEXT =====
Google was founded in 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its share and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a privately held company on September 4, 1998. An initial public offering (IPO) took place on August 19, 2004, and Google moved to its headquarters in Mountain View, California, nicknamed the Googleplex. In August 2015, Google announced plans to reorganize its various interests as a conglomerate called Alphabet Inc. Google is Alphabet leading subsidiary and will continue to be the umbrella company for Alphabets Internet interests. Sundar Pichai was appointed CEO of Google, replacing Larry Page who became the CEO of Alphabet.

====== QUESTIONS =====
q_0: who founded google
q_1: where is the headquarter of google
q_2: when google was founded?
q_3: who replaced larry page

====== RESPONSE ====
r_0: Larry Page and Sergey Brin
r_1: Mountain View, California
r_2: 1998
r_3: Sundar Pichai
```
