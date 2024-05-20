def count_lines_sentences_and_words(paragraph):
    # Counting lines
    lines = paragraph.split('\n')
    num_lines = len(lines)

    # Counting sentences
    sentences = paragraph.split('.')
    num_sentences = len(sentences)

    # Counting words
    words = paragraph.split()
    num_words = len(words)

    return num_lines, num_sentences, num_words

example_paragraph = """
Python is a powerful programming language. It is widely used for web development, data science, and artificial intelligence.

Python has a clear and readable syntax, making it easy for beginners to learn.

There are many resources available for learning Python, including online tutorials, books, and coding exercises.
"""

lines, sentences, words = count_lines_sentences_and_words(example_paragraph)

print(f"Number of lines: {lines}")
print(f"Number of sentences: {sentences}")
print(f"Number of words: {words}")
