#split the text into words and check each word if it is equal to the word reversed 


import wordninja
text='afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood'

list_of_words = wordninja.split(text)
print(list_of_words)
palindromes = []


for word in list_of_words:
    reverse_word = word[::-1]
    if word == reverse_word:
        palindromes.append(word)

print("The list of palindromes is : {} ".format(palindromes))
