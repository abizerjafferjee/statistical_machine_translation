# statistical_machine_translation
A word alignment model between English and French using the IBM-1 Model

The corpus used for this project is the Hansard records of the 36th Canadian Parliamnet.
The data is pairs of correponsing english and french sentence lines.

preprocess.py - Processes each sentence for each language. 

lm_train.py - Counts unigrams and bigrams for the language corpus and creates a language model for each language.

log_prob.py - Calculates Maximum Likelihood Estimate or Delta-Smoothed estimate of sentence based on language model.

perplexity.py - Calculates perplexity of test corpus given language model

align_ibm1.py - Using IBM-1 Algoirthm to train an alignment model which holds the probability of an english word aligining to a french word.

evalAlign.py - Evaluates the alignment model by comparing french to english translations from AM with hansard_english translations and google_english translations using BLEU score.

decode.py - To decode french to english

BLEU_score.py - To calculate BLEU_score

Sample training data added. Request the rest.
