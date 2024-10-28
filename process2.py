from naive_bayes import naive_bayes
infile = open("spam.csv", encoding = "ISO-8859-1")
idx = 0
train_labels = []
train_data = []
test_labels = []
test_data = []
test_split_idx = 4000

def process_line(line):
    words = line.lower().split()
    punct = ".!@#$%^&*()\"\';:,?/"
    for i in range(len(words)):
        for p in punct:
            words[i] = words[i].replace(p, "")
    return words

for line in infile:
    idx+=1
    if(idx==1):
        continue
    entries = line.split(",")
    if(idx<test_split_idx):
        train_labels.append(entries[0]=="spam")
        train_data.append(process_line(entries[1]))
    else:
        test_labels.append(entries[0]=="spam")
        test_data.append(process_line(entries[1]))

outputs = naive_bayes(train_data, train_labels, test_data)
total = 0
accur = 0
for i in range(len(outputs)):
    if(outputs[i]==test_labels[i]):
        accur +=1
    total +=1
print(accur/total)