import csv
import requests
from bs4 import BeautifulSoup

def save_webpage_text(url, filename):
  """Fetches webpage text, extracts main content, and saves it to a text file.
  Args:
      url (str): The URL of the webpage to scrape.
      filename (str): The desired filename for the text file.
  """
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  title = soup.find("h1").text.strip()  # Assuming title is within `<h1>` tag
  main_text = ""
  # Find the main content area (replace with website-specific logic)
  content_div = soup.find("div", class_="td-post-content tagdiv-type")  # Modify class name based on website
  if content_div:
      paragraphs = content_div.find_all(['p','h1','ul','ol'])
      for paragraph in paragraphs:
          main_text += paragraph.get_text(strip=True)  # Add double newlines for separation
  # Handle potential errors (e.g., missing content div, network issues)
  if not main_text:
      print(f"Warning: Could not extract main text from {url}.")
  with open(filename, "w", encoding="utf-8") as f:
      f.write("Title: {}".format(title))
      f.write(main_text)
  print(f"Webpage text saved to: {filename}")

if __name__ == "__main__":
  url = input("Enter Url: ")
  filename = input("Enter Filename: ")  # Customize filename as needed
  save_webpage_text(url, filename)

import nltk
nltk.download('punkt')
from nltk import word_tokenize, sent_tokenize
with open(filename, "r", encoding="utf-8") as f:
    text = f.read()
text

sentences = sent_tokenize(text)
sentences

words = word_tokenize(text)
words

nltk.download('stopwords')
from nltk.corpus import stopwords
def remove_stopwords(text_list, stopword_files):
  """
  Removes stopwords from a list of texts using multiple custom stopword files.
  Args:
      text_list: A list of strings containing the text data.
      stopword_files: A list of filenames containing stopwords, one per file.
  Returns:
      A list of strings with stopwords removed.
  """
  # Combine stopwords from all files into a single set
  all_stopwords = set(stopwords.words('english'))
  for filename in stopword_files:
    with open(filename, 'r') as f:
      all_stopwords.update(word.strip() for word in f)

  # Remove stopwords from each text in the list
  cleaned_texts = []
  for text in text_list:
    words = [word for word in text.split() if word not in all_stopwords]
    cleaned_texts.append(' '.join(words))

  return cleaned_texts

# Example usage
text_list = words
stopword_files = ["StopWords/StopWords_Auditor.txt", "StopWords/StopWords_Currencies.txt","StopWords/StopWords_DatesandNumbers.txt","StopWords/StopWords_Generic.txt","StopWords/StopWords_GenericLong.txt","StopWords/StopWords_Geographic.txt","StopWords/StopWords_Names.txt"]

cleaned_texts = remove_stopwords(text_list, stopword_files)

print(cleaned_texts)

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
stemmed_tokens = []
for word in cleaned_texts:
  stemmed = ps.stem(word)
  stemmed_tokens.append(stemmed)
stemmed_tokens

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = []
for word in cleaned_texts:
  lemmatized = lemmatizer.lemmatize(word)
  lemmatized_tokens.append(lemmatized)
lemmatized_tokens

import nltk
from nltk.corpus import stopwords
from collections import defaultdict

def load_lexicon(filenames):
  """
  Loads positive or negative words from multiple files.
  Args:
      filenames: A list of filenames containing words, one per line.
  Returns:
      A set of words from the files.
  """
  words = set()
  for filename in filenames:
    with open(filename, 'r', encoding='utf-8') as f:
      words.update([line.strip() for line in f])
  return words

def load_stopwords(filenames):
  """
  Loads stopwords from multiple files.
  Args:
      filenames: A list of filenames containing stopwords, one per line.
  Returns:
      A set of stopwords from the files.
  """
  stopwords_set = set()
  for filename in filenames:
    with open(filename, 'r', encoding='utf-8') as f:
      stopwords_set.update([line.strip() for line in f])
  return stopwords_set

def create_sentiment_lexicon(positive_filenames, negative_filenames, stopword_filenames):
  """
  Creates a dictionary of positive and negative words from files, excluding stopwords.
  Args:
      positive_filenames: A list of filenames containing positive words.
      negative_filenames: A list of filenames containing negative words.
      stopword_filenames: A list of filenames containing stopwords.
  Returns:
      A dictionary with keys 'positive' and 'negative', each containing sets of words.
  """
  # Download NLTK stopwords (optional)
  nltk.download('stopwords', quiet=True)

  # Load stopwords
  stopwords = load_stopwords(stopword_filenames)

  # Load positive and negative words
  positive_words = load_lexicon(positive_filenames) - stopwords
  negative_words = load_lexicon(negative_filenames) - stopwords

  # Create sentiment lexicon dictionary
  sentiment_lexicon = {
      'positive': positive_words,
      'negative': negative_words,
  }
  return sentiment_lexicon

def calculate_sentiment(text, sentiment_lexicon):
  """
  Calculates sentiment scores for a text using a sentiment lexicon.
  Args:
      text: The text to analyze.
      sentiment_lexicon: A dictionary with 'positive' and 'negative' word sets.
  Returns:
      A dictionary with keys 'positive_score', 'negative_score', and 'polarity_score'.
  """

  # Initialize sentiment scores
  positive_score = 0
  negative_score = 0

  # Count positive and negative words
  for token in lemmatized_tokens:
    if token in sentiment_lexicon['positive']:
      positive_score += 1
    elif token in sentiment_lexicon['negative']:
      negative_score += 1

  # Calculate polarity score with smoothing factor
  if positive_score == 0 and negative_score == 0:
    polarity_score = 0.0
  else:
    polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)
  subjectivity_score = (positive_score + negative_score) / (len(lemmatized_tokens) + 0.000001)
  # Return sentiment scores
  return {
      'positive_score': positive_score,
      'negative_score': negative_score,
      'polarity_score': polarity_score,
      'subjectivity': subjectivity_score,
  }

# Define folder paths and filenames (same as previous code)
positive_filenames = ["MasterDictionary/positive-words.txt"]
negative_filenames = ["MasterDictionary/negative-words.txt"]
stopword_filenames = ["StopWords/StopWords_Auditor.txt", "StopWords/StopWords_Currencies.txt","StopWords/StopWords_DatesandNumbers.txt","StopWords/StopWords_Generic.txt","StopWords/StopWords_GenericLong.txt","StopWords/StopWords_Geographic.txt","StopWords/StopWords_Names.txt"]

# Create sentiment lexicon
sentiment_lexicon = create_sentiment_lexicon(positive_filenames, negative_filenames, stopword_filenames)

# Calculate sentiment scores
sentiment_scores = calculate_sentiment(lemmatized_tokens, sentiment_lexicon)

# Print sentiment scores
# print("Positive score:", sentiment_scores['positive_score'])
# print("Negative score:", sentiment_scores['negative_score'])
# print("Polarity score:", sentiment_scores['polarity_score'])
# print("Subjective score:", sentiment_scores['subjectivity'])

import nltk
from nltk.corpus import words as nltk_words

def readability_analysis(text_list, output_file="output.csv"):
  """
  This function analyzes readability of a list of sentences.
  Args:
      text_list: A list of strings, where each string is a sentence.
      output_file (optional): Path to the output CSV file (default: None)
  Returns:
      A dictionary containing readability scores.
  """
  # Download NLTK resources if not already downloaded
  nltk.download('punkt', quiet=True)
  nltk.download('words', quiet=True)

  # Define a function to check if a word is complex (more than two syllables)
  def is_complex_word(word):
    word = word.lower()
    if word in nltk_words.words():  # Check if word is in english dictionary
      return len(set(w for w in word if w.lower() in 'aeiou')) > 2  # Count vowels
    else:
      return False  # Unknown words are considered complex

  # Initialize variables
  total_words = 0
  complex_words = 0

  # Calculate total words and complex words
  for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    total_words += len(words)
    complex_words += sum(is_complex_word(word) for word in words)

  # Calculate readability scores
  if total_words == 0:
    return {"message": "No text provided"}  # Handle empty input

  avg_sentence_length = total_words / len(sentences)
  percent_complex_words = complex_words / total_words * 100
  fog_index = 0.4 * (avg_sentence_length + percent_complex_words)
  avg_words_per_sentence = total_words / len(sentences)
  complex_word_count = sum(is_complex_word(word) for sentence in sentences for word in nltk.word_tokenize(sentence))
  syllable_count_per_words = 0
  word_count = 0
  personal_pronouns = ["I", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them"]
  personal_pronoun_count = sum(word in personal_pronouns for sentence in sentences for word in nltk.word_tokenize(sentence))
  avg_word_length = sum(len(word) for sentence in sentences for word in nltk.word_tokenize(sentence)) / total_words

  word_count += len(cleaned_texts)
  for word in words:
    if word.endswith('es') or word.endswith('ed'):
      syllable_count_per_words += 1
    else:
      syllable_count_per_words += len(set(w for w in word if w.lower() in 'aeiouy'))
  syllable_count = syllable_count_per_words


  # Return results
  results = {
      "URL":filename,
      "URL_ID":url,
      "Positive Score": sentiment_scores['positive_score'],
      "Negative Score": sentiment_scores['negative_score'],
      "Polarity Score": sentiment_scores['polarity_score'],
      "Subjectivity Score": sentiment_scores['subjectivity'],
      "Average Sentence Length": avg_sentence_length,
      "Percentage of Complex Words": percent_complex_words,
      "Fog Index": fog_index,
      "Average Words per Sentence": avg_words_per_sentence,
      "Complex Word Count": complex_word_count,
      "Word Count": word_count,
      "Syllable Count": syllable_count,
      "Personal Pronouns": personal_pronoun_count,
      "Average Word Length": avg_word_length
  }

  # Print results (optional)
  if not output_file:
      print("Average Sentence Length: ", avg_sentence_length)
      print("Percentage of Complex Words: ", percent_complex_words)
      print("Fog Index: ", fog_index)
      print("Average Number of Words per Sentence: ",avg_words_per_sentence)
      print("Complex Word Count: ",complex_word_count)
      print("Word Count: ",word_count)
      print("Syllable Count: ",syllable_count)
      print("Personal Pronouns",personal_pronoun_count)
      print("Average Word Length",avg_word_length)

  # Save results to CSV (if output_file provided)
  if output_file:
      with open(output_file, 'a+', newline='') as csvfile:
          writer = csv.DictWriter(csvfile, fieldnames=results.keys())
          # Skip header row if file already exists
          writer.writerow(results)
  else:
      # Write header row for new file
      with open(output_file, 'w', newline='') as csvfile:
          writer = csv.DictWriter(csvfile, fieldnames=results.keys())
          writer.writeheader(results.keys())
          writer.writerow(results)

  return results

# Example usage
text_list = text
output_file = "output.csv"
readability_scores = readability_analysis(text_list)
print("Output saved to ",output_file)
