from preprocess import *
import pickle
import os

def lm_train(data_dir, language, fn_LM):
    """
	This function reads data from data_dir, computes unigram and bigram counts,
	and writes the result to fn_LM

	INPUTS:

    data_dir	: (string) The top-level directory continaing the data from which
					to train or decode. e.g., '/u/cs401/A2_SMT/data/Toy/'
	language	: (string) either 'e' (English) or 'f' (French)
	fn_LM		: (string) the location to save the language model once trained

    OUTPUT

	LM			: (dictionary) a specialized language model

	The file fn_LM must contain the data structured called "LM", which is a dictionary
	having two fields: 'uni' and 'bi', each of which holds sub-structures which
	incorporate unigram or bigram counts

	e.g., LM['uni']['word'] = 5 		# The word 'word' appears 5 times
		  LM['bi']['word']['bird'] = 2 	# The bigram 'word bird' appears 2 times.
    """
    files = os.listdir(data_dir)

    unigram = {}
    bigram = {}

    for ffile in files:
        if ffile.split(".")[-1] != language:
            continue

        opened_file = open(data_dir + ffile, "r")
        for line in opened_file:
            processed_line = preprocess(line, language)

            # tokens in line
            tokens = processed_line.split()
            # add tokens from line to unigram
            for token in tokens:
                if token not in unigram:
                    unigram[token] = 1
                else:
                    unigram[token] += 1

                # add token if token not in bigram
                if token not in bigram:
                    bigram[token] = {}

            # add bigram to bigram dict
            for idx in range(len(tokens)):
                if idx < len(tokens)-1:
                    if tokens[idx+1] not in bigram[tokens[idx]]:
                        bigram[tokens[idx]][tokens[idx+1]] = 1
                    else:
                        bigram[tokens[idx]][tokens[idx+1]] += 1

    language_model = {'uni':unigram, 'bi':bigram}

    # Save Model
    with open(fn_LM +'.pickle', 'wb') as handle:
        pickle.dump(language_model, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return language_model


if __name__ == "__main__":

    saved_files = '/test'
    data_dir = '/data/Hansard/Training/'
    LMed = '{}/LM_e'.format(saved_files)
    LMfd = '{}/LM_f'.format(saved_files)
    LMe = lm_train(data_dir, 'e', LMed)
    LMf = lm_train(data_dir, 'f', LMfd)
