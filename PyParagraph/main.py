#Need to create python script to automate the analysis of passages
import re
#need to import a text file with a paragraph of your choosing. 
file = 'raw_data/paragraph_1.txt'
file2 = 'raw_data/paragraph_2.txt'
file_output = 'paragraph_analysis.txt'

#open file in read('r') mode, store the contents in a variable called text
with open(file,'r') as text:
    # print(text)

    # Store the contents as a string (with no new lines)
    passage_text = text.read().replace("\n", " ")
    # print(passage_text)

    #we are cleaning text and lower casing all words
    # for char in '-,()':
    #     passage_text = passage_text.replace(char,' ')
    # passage_text = passage_text.lower()

    # print(passage_text)
    # Split the paragraph based on spaces to calculate word count
    word_list = passage_text.split(" ")
    word_count = len(word_list)

    # calculate the avg. length of word
    total_letters = []

    # for loop to sum up the total letters
    for word in word_list:
        #append letter counts to our total_letters list
        total_letters.append(len(word))
    # print(total_letters)

    #calculate average length
    avg_word = sum(total_letters) / (word_count)
    # print(avg_word)

    # Re-split the original paragraph based on punctuation (. ? !)
    sentence_split = re.split("(?<=[.!?]) +", passage_text)
    # print(sentence_split)
    num_sentences = len(sentence_split)

    words_sentences = []

    for sentence in sentence_split:
        words_sentences.append(len(sentence.split(" ")))
        # print(sentence.split(" "))


    # print(words_sentences)
    avg_word_sentence = sum(words_sentences)/num_sentences

    # print(word_count)

    output = (
        f'Paragraph Analysis\n'
        f'-------------------\n'
        f'Approximate Total Words: {word_count}\n'
        f'Approximate Sentence Count: {num_sentences}\n'
        f'Average Letter Count: {avg_word}\n'
        f'Average Words Per Sentence: {avg_word_sentence}'
    )

with open(file_output, "a") as txt_file:
    txt_file.write(output)

