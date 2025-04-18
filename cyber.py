import nltk
from better_profanity import profanity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import requests
import webbrowser

# Download required resources from NLTK
nltk.download('stopwords')
nltk.download('punkt')

# Initialize better_profanity
profanity.load_censor_words()


# Function to fetch website content
def get_website_content(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch website content. Status code: {response.status_code}")
        return None

def detect_cyberthreat(text):
    # Tokenize the text and remove punctuation
    words = word_tokenize(text)
    words = [word for word in words if word.isalpha()]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Check for profanity and cyberthreat terms
    for word in words:
        if profanity.contains_profanity(word):
            return True  # Detected profanity

    return False  # No cyberthreat detected
        

# URL of the website to scan
website_url = "https://gu.icloudems.com/corecampus/student/student_index.php"

# Fetch website content
content = get_website_content(website_url)

# Check for cyberthreat in the website content
if content:
    if detect_cyberthreat(content):
        print("Cyberthreat detected on the website:", website_url)
        # Redirect the user to cybercrime.gov.in
        webbrowser.open("https://cybercrime.gov.in/Webform/Crime_AuthoLogin.aspx")
    else:
        print("No cyberthreat detected on the website:", website_url)
else:
    print("Failed to fetch website content.")

# Test the function with a sample text
#text = "all the best"
#if detect_cyberbullying(text):
 #   print("Cyberbullying detected.")
    # Redirect the user to cybercrime.gov.in
  #  webbrowser.open("https://cybercrime.gov.in")
#else:
   # print("No cyberbullying detected.")
