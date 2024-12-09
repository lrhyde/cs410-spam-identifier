import gensim
import gensim.downloader

def word2vec(train_set, train_labels, dataset):
    model = gensim.models.Word2Vec(dataset + train_set, min_count=1, vector_size=500, window=5)
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

    yhats = []
    for q in dataset:
        relevantWords = []
        for word in q:
            relevantWords+=[j[0] for j in model.wv.most_similar(word, topn=20)]
            # print(word, relevantWords)
        pos_count = sum([words[w][0] for w in relevantWords if w in words])
        neg_count = sum([words[w][1] for w in relevantWords if w in words])
        if(pos_count>neg_count):
            yhats.append(1)
        else:
            yhats.append(0)
    return yhats