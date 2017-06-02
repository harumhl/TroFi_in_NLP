# This uses a pseudo code from http://www.aclweb.org/anthology/E06-1042#page=3
# I am using jupyter notebook to test my code, then copy it here
# Parts of the program is only pseudo code. I just wanted to save it here

# Create variables
WSM = {} # Word Similarity Matrix. 
SSM = {} # Sentence Similarity Matrix. 
SSM_L = {} # SSM for literal context
SSM_N = {} # SSM for nonliteral context

# these 4 sets should not be empty
S = {} # the set of sentences containing the target word
L = {} # the set of literal seed sentences
N = {} # the set of nonliteral seed sentences
W = {} # the set of words/features, w ∈ s means w is in sentence s, s 3 w means s contains w
# e: threshold that determines the stopping condition

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
    
# Initialize (all words and sentences have similarity of 1 to itself)
# 1: w-sim0(wx, wy) := 1 if wx = wy, 0 otherwise
for word1 in W:
    for word2 in W:
        if word1 == word2:
            WSM[word1, word2] = 1
        else:
            WSM[word1, word2] = 0
    
# 2: s-simI 0(sx, sy) := 1, for all sx, sy ∈ S × S where sx = sy, 0 otherwise
for sentence1 in S:
    for sentence2 in S:
        if sentence1 == sentence2:
            SSM [sentence1, sentence2] = 1
        else:
            SSM [sentence1, sentence2] = 0
            
# 3: i := 0
i = 0

# 4: while (true) do
while True:
    
#5: s-simL i+1(sx, sy) := P wx∈sx p(wx, sx)maxwy∈sy w-simi(wx, wy), for all sx, sy ∈ S × L
for s_x in S:
    for s_y in L:
        
        summed_val = 0
        for w_x in s_x:
            
            # max WSM [w_x, w_y]
            max_of_WSM = 0
            for w_y in s_y:
                if WSM [w_x, w_y] > max_of_WSM:
                    max_of_WSM = WSM [w_x, w_y]
                    
            summed_val += p(w_x, s_x) * max_of_WSM
        SSM_L[s_x, s_y] = summed_val

# 6: s-simN i+1(sx, sy) := P wx∈sx p(wx, sx)maxwy∈sy w-simi(wx, wy), for all sx, sy ∈ S × N
# everything is same as step 5 except that we use N instead of L & SSM_N instead of SSM_L

#7: for wx, wy ∈ W × W do 
for w_x in W:
    for w_y in W:
        
#8: w-simi+1(wx, wy) := (i = 0 P sx3wx p(wx, sx)maxsy3wy s-simI i (sx, sy)
#                        else P sx3wx p(wx, sx)maxsy3wy {s-simL i (sx, sy),s-simN i (sx, sy)}
        for s_x in sentences_containing (w_x, ???):
        
            summed_val = 0
            for s_y in sentences_containing (w_y, ???):
                max_of_SSM = 0
                if i == 0:
                    if SSM [s_x, s_y] > max_of_SSM:
                        max_of_SSM = SSM [s_x, s_y]
                else:
                    if SSM_L [s_x, s_y] > max_of_SSM:
                        max_of_SSM = SSM_L [s_x, s_y]
                    if SSM_N [s_x, s_y] > max_of_SSM:
                        max_of_SSM = SSM_N [s_x, s_y]
            summed_val += p(w_x, s_x) * max_of_SSM
        WSM [w_x, w_y] = summed_val
        
#9: end for
#10: if ∀wx, maxwy {w-simi+1(wx, wy) − w-simi(wx, wy)} ≤  then
# when to end. I'll just set it based on i value

#11: break # algorithm converges in 1steps.
        break

#12: end if
#13: i := i + 1
    i += 1
#14: end while

# so far above was KE-train
# below is KE-test
#1: For any sentence sx ∈ S
for s_x in S:
    
#2: if max sy s-simL(sx, sy) > max sy s-simN (sx, sy) then
    max_SSM_N = 0
    max_SSM_L = 0
    for s_y in ???:
        if SSM [s_x, s_y] > max_SSM_L:
            max_SSM_L = SSM [s_x, s_y]
    for s_y in ???:
        if SSM [s_x, s_y] > max_SSM_N:
            max_SSM_N = SSM [s_x, s_y]
            
    if max_SSM_L > max_SSM_N:
#3: tag sx as literal
        print s_x, "literal"
#4: else
    else:
#5: tag sx as nonliteral
        print s_x, "nonliteral"
#6: end if
