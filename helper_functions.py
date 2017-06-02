# helper function
def p (word, sentence): # unigram probability
    count = 0
    for a_word in sentence:
        if word == a_word:
            count += 1
    return count / num_of_words (sentence)

def sentence_containing (word, sentences): #sentences = S + L + N?
    new_set = {}
    for sentence in sentences:
        if word in sentence:
            new_set.append(sentence)
    return new_set

def print_WSM (WSM, max_words = 9999):
    # usage of matrix: WSM [word1, word2] = number
    # data format: WSM = [((w11, w12), n1), ((w21, w22), n2), ((w31, w32), n3), ...]

    # first value of a tuple = [w11, w21, w31, ...]
    # second value of a tuple = [w12, w22, w32, ...]
    #     changing it to a set gets rid of duplicates
    first_vals = list(set([word_tuple[0] for word_tuple in WSM]))
    second_vals = list(set([word_tuple[1] for word_tuple in WSM]))

    # the length of the longest word in the list
    longest_length = max(len(word) for word in first_vals)

    i = 0
    # display column names
    print ' ' * (longest_length +1), # spaces to display row names + one space
    for second_val in second_vals:
        print second_val,

        # like a tab. spaces to match up with longest word (comma adds an extra)
        print ' ' * (longest_length -len(second_val)),

        i += 1
        if i > max_words:
            break
    print

    # display row names & similarity values
    i = 0
    for first_val in first_vals:
        # display row names + like a tab, spaces to match up with longest word
        print first_val, ' '*(longest_length -len(first_val)),

        j = 0
        for second_val in second_vals:
            # (longest_length-2) decimals (zero & dot take two spaces)
            print ('%.' +str(longest_length-2) +'f') % WSM [first_val, second_val], 
            print '', # just one space (by comma)

            j += 1
            if j > max_words:
                break
        print    
        
        i += 1
        if i > max_words:
            break

def print_SSM ():
    print ""
