# This uses a pseudo code from http://www.aclweb.org/anthology/E06-1042#page=3
# I am using jupyter notebook to test my code, then copy it here
# Parts of the program is only pseudo code. I just wanted to save it here
import helper_functions

# Create variables
WSM = {} # Word Similarity Matrix. 
SSM = {} # Sentence Similarity Matrix. 
SSM_L = {} # SSM for literal context
SSM_N = {} # SSM for nonliteral context

# these 4 sets should not be empty
# S: the set of sentences containing the target word
# target word (temporarily): "nice"
# I manually got rid of punctuation since I haven't developed anything to take care of that
S = ["we had a nice time", "he is a really nice guy", "They are always nice to stranger", "Nice people wouldn not do such things", "It is nice and warm in here", "that is nice of you to say"]
# L: the set of literal seed sentences
L = ["it is about time for us to leave", "that guy over there was very mean"]
# N: the set of nonliteral seed sentences
N = ["time is money", "it makes my heart feel warm"]
# W: the set of words/features, w ∈ s means w is in sentence s, s 3 w means s contains w
# getting all the (unique) words from S, L, and N
W = []
for sentence in S+L+N:
    for word in sentence.split():
        W.append(word)
W = list(set(W)) # set() gets rid of duplicates
# e: threshold that determines the stopping condition

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
