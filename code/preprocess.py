import re

def preprocess(in_sentence, language):
    """
    This function preprocesses the input text according to language-specific rules.
    Specifically, we separate contractions according to the source language, convert
    all tokens to lower-case, and separate end-of-sentence punctuation

	INPUTS:
	in_sentence : (string) the original sentence to be processed
	language	: (string) either 'e' (English) or 'f' (French)
				   Language of in_sentence

	OUTPUT:
	out_sentence: (string) the modified sentence
    """
    if language == 'e':
        # remove end of line, strip space and lower case
        proc = in_sentence.split("\n")[0].strip().lower()
        proc = list(proc)
        out_sentence = 'SENTSTART '
        # for each character do punctuation processing
        for idx in range(len(proc)):
            if proc[idx] == '(' or proc[idx] == '<':
                out_sentence += proc[idx] + ' '
            elif proc[idx] == '"':
                if proc[idx-1] == ' ':
                    out_sentence += proc[idx] + ' '
                else:
                    out_sentence += ' ' + proc[idx]
            elif proc[idx] == '-':
                out_sentence += ' ' + proc[idx] + ' '
            elif proc[idx] in [',', '?', '!', ':', ';', ')', '+', '>', '=']:
                out_sentence += ' ' + proc[idx]
            elif proc[idx] == '.':
                if idx == len(proc)-1:
                    out_sentence += ' ' + proc[idx]
            else:
                out_sentence += proc[idx]

        out_sentence += ' SENTEND'
        return out_sentence

    elif language == 'f':
        # remove end of line, strip space and lower case
        proc = in_sentence.split("\n")[0].strip().lower()
        words = proc.split()
        # for each word, if required, separate the following the following contractions
        for ifx in range(len(words)):
            if words[ifx] not in ['d\'abord', 'd\'accord', 'd\'ailleurs', 'd\'habitude']:
                if '\'' in words[ifx]:
                    if 'l\'' in words[ifx] or 'qu\'' in words[ifx] \
                    or '\'on' in words[ifx] or '\'il' in words[ifx] \
                    or 't\'' in words[ifx] or 'j\'' in words[ifx]:
                        parts = words[ifx].split('\'')
                        words[ifx] = parts[0] + '\''
                        words.insert(ifx + 1, parts[1])

        proc = ' '.join(words)

        proc = list(proc)
        out_sentence = 'SENTSTART '
        # for each character do punctuation processing
        for idx in range(len(proc)):
            if proc[idx] == '(' or proc[idx] == '<':
                out_sentence += proc[idx] + ' '
            elif proc[idx] == '"':
                if proc[idx-1] == ' ':
                    out_sentence += proc[idx] + ' '
                else:
                    out_sentence += ' ' + proc[idx]
            elif proc[idx] == '-':
                out_sentence += ' ' + proc[idx] + ' '
            elif proc[idx] in [',', '?', '!', ':', ';', ')', '+', '>', '=']:
                out_sentence += ' ' + proc[idx]
            elif proc[idx] == '.':
                if idx == len(proc)-1:
                    out_sentence += ' ' + proc[idx]
            else:
                out_sentence += proc[idx]

        out_sentence += ' SENTEND'
        return out_sentence
