# Web Scraping and Text Analysis Toolkit  🚀💻 #
This Python toolkit empowers you to extract textual content from webpages 🕸️ and perform in-depth analysis to gain valuable insights. 📊

# Features #
  - **Robust Web Scraping:** Fetches webpage content using requests  🌎 and parses it with BeautifulSoup. 🥣
    
  - **Customizable Content Extraction:** Locates the main content area based on HTML structure (class names or IDs) using the find_main_content function, adaptable for different websites. 🌐🏠
    
  - **Comprehensive Text Preprocessing:** Reads text data from a file and performs sentence tokenization (nltk.sent_tokenize), word tokenization (nltk.word_tokenize), stopword removal (customizable list of stopwords),      and optional stemming (PorterStemmer) or lemmatization (WordNetLemmatizer) for reducing words to their base form.✂️🔬
    
  - **Accurate Sentiment Analysis:** Leverages a pre-built sentiment lexicon to identify positive and negative words, calculates sentiment scores with smoothing to avoid zero scores, and returns a dictionary containing     polarity (positive minus negative divided by the total), subjectivity, and detailed scores.😄😡📉
    
  - **In-depth Readability Analysis:** Calculates various readability metrics including average sentence length, percentage of complex words (based on syllable count), Fog Index, average words per sentence, complex         word count, word count, syllable count (estimated by vowel count), personal pronoun count, and average word length.👀⚖️📄

  - **Flexible Output:** Provides options to print results to the console for quick analysis and write them to a CSV file (output.csv) using the csv module.🖨️📈

# Installation #
1. Clone the repository
   - `git clone https://github.com/Gwala-1413/web-scraping-text-analysis.git`
2. Install required dependencies:
   - `pip install requests beautifulsoup4 nltk`

# Usage #
1. Navigate to the repository directory in your terminal.💻 :cd:
2. Run the script: ▶️
   - `python Exe.py`
3. When prompted, enter the target URL and the desired filename for saving the extracted text.🔗📝
4. An output.csv file will be generated containing sentiment analysis and readability scores.📈

# Acknowledgements #
- requests - For efficient HTTP requests (https://docs.python-requests.org/en/latest/)🙌
- BeautifulSoup - For parsing HTML content (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)🙌
- nltk - For natural language processing tasks (https://www.nltk.org/)🙌

# Contributing #
We welcome contributions to this project! Feel free to fork the repository and submit pull requests for bug fixes, feature enhancements, or additional functionalities.🙌🔧🌟
