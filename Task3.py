
from nltk import word_tokenize, sent_tokenize,PorterStemmer,SnowballStemmer
#stop words
from nltk.corpus import stopwords
stop=stopwords.words('english')

#assignments
text=input("Enter  a text , please:\n")
print(" Enter : \n 1 for word tokenization \n 2 for sentence tokenization \n 3 for  original text\n 4 for stemming \n your choice is :")
choice=int(input())

#stemming function
def stem_func():  
    stemmed_text=[]  
    tokenized_text=word_tokenize(text)
    for word in tokenized_text:
        if word in stop:    
            stemmed_text.append(word)
            continue
        stemmed_text.append(x.stem(word))
    #Displaying stemmed text
    stemmed_sent=" ".join(stemmed_text)
    print('stemmed_text:',stemmed_sent) 

#program body
if choice == 1:
    print(word_tokenize(text))
elif choice==2:
    print(sent_tokenize(text))
elif choice==3:
    print(text)
    
elif choice==4:
    print('Enter:\n 4.1 for Porter stemmer\n 4.2 for Snowball stemmer')
    st_type=float(input("Stemming type is: "))
    if st_type==4.1:
        x=PorterStemmer()
        stem_func()
    elif st_type==4.2:
        x=SnowballStemmer("english")
        stem_func()
    else:
        print("please,choose correct stemming number")              
else:
    print("please , enter a right number")



# I am studying programming

