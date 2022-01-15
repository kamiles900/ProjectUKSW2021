import re
import string
import matplotlib.pyplot as plt
from data import deleted_words

# Group 1 : Paweł Jasiński, Mateusz Fila, Kamil Kokoszkiewicz, Piotr Guz, Sebastian Kowalski.

#------Text analyzer------

#load up txt file with book and change test.txt for the book file name
file_a = open('test.txt','r')
file_a = file_a.read().lower()

#cleaning text from special characters
clean_text_raw = re.sub('\W+',' ', file_a).split()

# words frequency and counting
clean_text = list(clean_text_raw)
print('Total words: '+ str(len(clean_text)))


#counting all words
dict = []
for i in clean_text:
    words_freq = clean_text.count(i)
    freq_dic = (i,words_freq)

    #deleting same words
    if freq_dic in dict:
        dict.remove(freq_dic)
    else:
        dict.append(freq_dic)


#making file with numbers of occurences
occurences = open('occurences.txt', 'w')
for i in dict:
    occurences.write(str(i)+ '\n')
occurences.close()



#Unique words
def unique_words(text):
    words = text.replace(',', '').replace("'", '').replace('(','').replace(')','').replace('-',' ').replace('?','').replace('!','').replace(':', '').replace(' - ','').replace('- ','').replace('.','').split()
    unique = list(set(words))
    print('Number of unique words: '+ str(len(unique))+'\n')

unique_words(file_a)

#making a list with all words
def clean_text_file(text_file):
    clean = text_file.replace(',', '').replace("'", '').replace('(', '').replace(')', '').replace('-',' ').replace(';', '').replace(':', '').replace('—','').split()
    file = open('words.txt', 'w')
    for i in clean:
        file.write(i + '\n')
    file.close()
clean_text_file(file_a)

#making a list with all words without conjunctions and pronouns
def clean_text_file_delete_words(text_file):
    clean2 = text_file.replace("'", '').replace('(', '').replace(')', '').replace('-',' ').replace(' - ', '').replace(':', '').replace(';', '').replace(',','').replace('—','').split()
    file = open('words2.txt', 'w')
    #deleting conjunctions and pronouns
    l3 = [x for x in clean2 if x not in deleted_words]
    for i in l3:
        file.write(i + '\n')
    file.close()

    # unique words after cleaning
    unique2 = list(set(l3))

    print('...cleaning... \n')
    print('Total words : '+ str(len(l3)))
    print('Number of unique words: ' + str(len(unique2)))


clean_text_file_delete_words(file_a)




#making a list of points with sorted number of occurencies / 20 points for chart
text = clean_text_raw
d = {}
for line in text:
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))
    words = line.split(" ")
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

#list of the points for chart
sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
list_of_points =[]
for i in sort_orders[0:20]:
	list_of_points.append((i[0],i[1]))
print(list_of_points)


#second list of point with words after cleaning
text2 = clean_text_raw
c = {}
for line in text:
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))
    words = line.split(" ")
    words = [x for x in words if x not in deleted_words]
    for word in words:
        if word in c:
            c[word] = c[word] + 1
        else:
            c[word] = 1

#list of the points for chart
sort_orders2 = sorted(c.items(), key=lambda x: x[1], reverse=True)
list_of_points2 =[]
for i in sort_orders2[0:20]:
	list_of_points2.append((i[0],i[1]))
print(list_of_points2)










#---- Charting part ------#

#chart for words before cleaning
def chart1():
    li = list_of_points
    x, y = zip(*li)
    plt.title('Graph of the number of word repetitions')
    plt.xlabel('words')
    plt.ylabel('repetitions')
    plt.scatter(x, y)
    figure = plt.gcf()
    figure.set_size_inches(10, 8)
    plt.xticks(rotation=60)
    plt.savefig('chart_no_clean.png')
    #plt.show()

#chart for words after cleaning
def chart2():
    li2 = list_of_points2
    x, y = zip(*li2)
    plt.title('Graph of the number of word repetitions after cleaning')
    plt.xlabel('words ')
    plt.ylabel('repetitions ')
    plt.scatter(x, y)
    figure = plt.gcf()
    figure.set_size_inches(10, 8)
    plt.xticks(rotation=60)
    plt.savefig('chart_clean.png')
    #plt.show()

#Create the charts by calling one of the funcyions at the same time
#chart1()
#chart2()


# After run, program produces 3 txt files 
# occurences.txt - number of occurences of  each word
# words.txt, words2.txt - list of words from the bood and second list after deleting some words.
# 2 charts in png file represents words and occurences 




















