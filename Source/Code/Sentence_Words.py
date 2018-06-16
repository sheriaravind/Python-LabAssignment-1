def Sentence(sentence):
    reverse_Sentence = ''
    longest_word = ''
    length = 0
    split_Sentence = sentence.strip().split()
    if(len(split_Sentence) % 2 == 0):
        print("Middle Word is: ({0},{1})".format(split_Sentence[int(len(split_Sentence)/2 - 1)],
                                                 split_Sentence[int(len(split_Sentence)/2)]))
    elif(len(split_Sentence) % 2 != 0):
        print("Middle Word is: ({0})".format(split_Sentence[int(len(split_Sentence) / 2)]))

    for word in split_Sentence:
        if(len(word) > length):
            length = len(word)
            longest_word = word
        reverse_Sentence += word[::-1] + " "
    print("Sentence with reverse words is: ",reverse_Sentence)
    print("Longest word in the sentence is: ", longest_word)


if __name__ == '__main__':
    sentence = input("Enter a Sentence:")
    Sentence(sentence)
