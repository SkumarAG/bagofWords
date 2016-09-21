from collections import OrderedDict,Counter
import re,itertools
def bagofWords(text_data,n=1):
    """ text data should be in array form 
    i.e. in arrya of list
    Ex :
    data = ["John likes to watch movies. Mary likes movies too.","John also likes to watch football games."]
    
    number of ngrams is decided by n
    by defalutl it is 1
    """
    unique_ngram = []
    
    single_list = []# sinlge list of all the Ngram - might have duplicate 
    
    tokenized_data = [re.findall(r'\w+',i) for i in text_data]# for tokenization
    
    
    single_list = list(itertools.chain(*tokenized_data))# all list of token convert in to a single list

    def listToNgram(single_list):
        ngram = []
        # if input is ['John', 'likes', 'to','watch']
        # output is ['John likes','likes to','to watch'] if n = 2
        if n>1:
            a = 1 #helpful when n = 2 as when n = 2 in ngram tokenization, last word be unigram so to avoid iterate only to len-1    
        else:
            a = 0
        for i in range(len(single_list)-a):
            words = single_list[i:i+n]# select words from a lsit according to ngram
            word = " ".join(words) #combine the words in to a single sentence
            ngram.append(word)
        return ngram
        
    ngrams = listToNgram(single_list)# contail all ngram from a input
    print ngrams
    unique_ngram = list(OrderedDict.fromkeys(ngrams))# remove duplicate from ngram
    temp = []
    bow = []
    # convert input text array in to a n gram and then apply bag of word technique
    for i in range(len(tokenized_data)):
        datax = listToNgram(tokenized_data[i])
        word_freq = Counter(datax) # have all the word - how many times it appearin the sentence
        temp = []
        for j in unique_ngram:
            if j in (datax):
                freq = word_freq[j]
                temp.append(freq)
            else:
                temp.append(0)
        bow.append(temp)
    
    return bow
        
if __name__ == "__main__":
     data = ["this is for test","John likes to watch movies. Mary likes movies too.","John also likes to watch football games."]
     print bagofWords(data,2)
