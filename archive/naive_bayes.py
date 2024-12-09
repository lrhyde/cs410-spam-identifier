import math

def naive_bayes(train_set, train_labels, dev_set, laplace=0.005, pos_prior=0.8, silently=False):
    # word : [num of pos reviews, num of neg reviews]
    words = dict()
    total_pos_reviews = 0
    total_neg_reviews = 0
    total_pos_words = 0
    total_neg_words = 0

    for i in range(len(train_set)):
        if(train_labels[i]==1):
            total_pos_reviews+=1
            for word in train_set[i]:
                if(word in words.keys()):
                    words[word][0]+=1
                else:
                    words[word] = [1, 0]
                total_pos_words+=1
        else:
            total_neg_reviews+=1
            for word in train_set[i]:
                if(word in words.keys()):
                    words[word][1]+=1
                else:
                    words[word] = [0, 1]
                total_neg_words+=1
    print(total_neg_reviews)
    print(total_pos_reviews)

    # total word types
    v_pos = len([w for w in words.keys() if words[w][0]!=0])
    v_neg = len([w for w in words.keys() if words[w][1]!=0])
    yhats = []
    for doc in dev_set:
        pos_prob = math.log2(pos_prior)
        neg_prob = math.log2(1-pos_prior)
        for word in doc:
            if(word in words.keys()):
                    print(word, words[word])
                    pos_prob+=math.log2((words[word][0] + laplace)/(total_pos_words + laplace*(v_pos+1)))
                    neg_prob+=math.log2((words[word][1] + laplace)/(total_neg_words + laplace*(v_neg+1)))
            else:
                # unk
                pos_prob+=math.log2(laplace/(total_pos_words + laplace*(v_pos+1)))
                neg_prob+=math.log2(laplace/(total_neg_words + laplace*(v_neg+1)))
        if(pos_prob>neg_prob):
            yhats.append(1)
        else:
            yhats.append(0)
    return yhats
