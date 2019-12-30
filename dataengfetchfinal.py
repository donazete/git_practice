#Do you count punctuation or only words? Counting words and punctuation but eliminating whitespaces
#Which words should matter in the similarity comparison? All words
#Do you care about the ordering of words? On a sentence by sentence comparison, ordering does not matter 
#What metric do you use to assign a numerical value to the similarity? By percentage scaled back to 1
#What type of data structures should be used?  (Hint: Dictionaries and lists are particularly helpful data structures that can be leveraged to calculate the similarity of two pieces of text.)
# I'll be implementing both lists and dictionaries
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def sentenceCompare():  #texta, textb
    response = {}
    texta = request.form['texta'] #request.get_data()
    textb = request.form['textb']
    #print(data)
    #texts_list.append(data)

    lista = texta.split('.')
    listb = textb.split('.')
    sentcounta = len(lista)
    sentcountb = len(listb)
    wordcounta = len(texta.split())
    #wordcountb = len(textb.split())
    abbrev_synon = {"clip" : "cut out",
                    "cost" : "total cost",
                    "you'll" : "you will",
                    "don't" : "do not",
                    "we'll" : "we will",
                    "products" : "items",
                    "love" : "buy",
                    "participating" : "eligible",
                    "barcodes" : "UPCs"} # create a dictionary of abbreviations. key would be words in list a and values from list b
    simcount = 0
    i = 0

    while i < sentcounta:
        if i >= sentcountb:
            break
        else:
            if lista[i] == listb[i]: #if sentences match, no need to compare words individually
                simcount += len(lista[i].split())
            else: #if they don't loop through individual words on list x, compare with dictionaries to get abbreviations and synonyms, then compare outcome with the word in the same index on list y
                word_listx = lista[i].split()
                word_countx = len(word_listx)
                j = 0

                while j < word_countx:
                    if word_listx[j] in listb[i]:
                        simcount += 1
                    elif word_listx[j] in abbrev_synon.keys():
                        simcount += 1
                    j += 1
        i += 1
    txt = {"Word count for first text" : wordcounta, "Similar words count" : simcount, "Similarity ratio" : simcount/wordcounta}
    response['Result'] = txt
    return response

if __name__ == '__main__':
 app.run()

a = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
b = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."
c = "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."

#x = sentenceCompare(a,b)
#print(x)
#y = sentenceCompare(a,c)
#print(y)
#z = sentenceCompare(b,c)
#print(z)