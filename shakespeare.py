import string


# Filler words we do not want to count
filler_words = [
    "the", "and", "or", "of", "to", "in", "a", "is", "it",
    "that", "this", "with", "for", "as", "be", "by", "are",
    "was", "were", "but", "not", "on", "at", "from",
    "have", "has", "had", "he", "she", "they", "them",
    "his", "her", "their", "you", "your", "i", "me",
    "my", "we", "our", "us"
]


def process_play(input_file, output_file):

     # Open and read file
    inFile = open(input_file, "r", encoding="utf-8")
    text = inFile.read()
    inFile.close()

    #  Make all text lowercase
    text = text.lower()

    # Remove all punctuation
    # This removes: . , ! ? ' " : ; - etc.
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split into individual words
    words = text.split()

      # Create dictionary
    word_dictionary = {}

    #  Count word frequencies
    for word in words:

        # Ignore filler words and very short words
        if word not in filler_words and len(word) > 2:

            if word in word_dictionary:
                word_dictionary[word] = word_dictionary[word] + 1
            else:
                word_dictionary[word] = 1

    # Find top 15 words manually
    top15 = []

    for i in range(15):

        highest_word = ""
        highest_count = 0

        for word in word_dictionary:

            if word_dictionary[word] > highest_count:
                highest_count = word_dictionary[word]
                highest_word = word

        top15.append((highest_word, highest_count))

        # Remove it so it is not counted again
        del word_dictionary[highest_word]

    # Write results to output file
    outFile = open(output_file, "w", encoding="utf-8")

    outFile.write("Word\tFrequency\n")

    for pair in top15:
        word = pair[0]
        count = pair[1]
        outFile.write(word + "\t" + str(count) + "\n")

    outFile.close()


# Run for both plays
process_play("Macbeth.txt", "macbeth_top15.txt")
process_play("titus_andronicus.txt", "titus_andronicus_top15.txt")
