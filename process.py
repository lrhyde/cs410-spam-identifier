from naive_bayes import naive_bayes
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

infile = open("bot_detection_data.csv")
idx = 0
train_labels = []
train_data = []
test_labels = []
test_data = []
test_split_idx = 35000
stop_words=stopwords.words('english')

def process_line(line):
    words = line.lower().split()
    punct = ".!@#$%^&*()\"\';:,?/"
    for i in range(len(words)):
        for p in punct:
            words[i] = words[i].replace(p, "")

    # print("words: ", words)

    # remove stop words
    clean_words = [word.lower() for word in words if word.lower() not in stop_words]  
    # print("clean_words: ", clean_words)
    return clean_words

for line in infile:
    idx+=1
    if(idx==1):
        continue
    entries = line.split(",")
    print(entries)
    print(entries[7])
    if(idx<test_split_idx):
        train_labels.append(int(entries[7]))
        train_data.append(process_line(entries[2]))
    else:
        test_labels.append(int(entries[7]))
        test_data.append(process_line(entries[2]))

outputs = naive_bayes(train_data, train_labels, test_data)
total = 0
accur = 0
for i in range(len(outputs)):
    if(outputs[i]==test_labels[i]):
        accur +=1
    total +=1
print(accur/total)

print("stop_words: ", stop_words)