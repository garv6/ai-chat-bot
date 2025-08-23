import json
import random
import re
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()
stopwords = set(nltk.corpus.stopwords.words('english'))  # Load stopwords

# Load the intents file
file_path = 'education.json'

def load_intents_education(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        intents = json.load(f)
    return intents

# Preprocess the data
def preprocess_data_education(intents):
    questions = []
    tags = []
    for intent in intents['intents']:
        for question in intent['questions']:
            # Clean and tokenize the question
            question = re.sub(r'\W', ' ', question.lower())  # Remove punctuation
            tokens = nltk.word_tokenize(question)  # Tokenize
            tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stopwords]  # Lemmatize and remove stopwords
            questions.append(' '.join(tokens))
            tags.append(intent['tag'])
    return questions, tags

# Train the chatbot using Logistic Regression for classification
def train_chatbot_education(intents):
    questions, tags = preprocess_data_education(intents)
    
    # Convert questions to numerical form using TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(questions)
    
    # Encode the target labels (tags)
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(tags)

    # Train a Logistic Regression model
    model = LogisticRegression()
    model.fit(X, y)

    return vectorizer, label_encoder, model

# Get a response based on user input
def get_response_education(user_input, vectorizer, label_encoder, model, intents):
    # Clean and tokenize user input
    user_input = re.sub(r'\W', ' ', user_input.lower())  # Remove punctuation and convert to lower
    user_tokens = nltk.word_tokenize(user_input)  # Tokenize
    user_tokens = [lemmatizer.lemmatize(token) for token in user_tokens if token not in stopwords]  # Lemmatize and remove stopwords
    user_input_processed = ' '.join(user_tokens)

    # Transform the user input using the trained TF-IDF vectorizer
    user_input_vector = vectorizer.transform([user_input_processed])

    # Predict the tag using the trained Logistic Regression model
    predicted_tag_index = model.predict(user_input_vector)[0]
    predicted_tag = label_encoder.inverse_transform([predicted_tag_index])[0]

    # Return the corresponding response
    for intent in intents['intents']:
        if intent['tag'] == predicted_tag:
            return random.choice(intent['responses'])

    return "I'm sorry, I didn't understand that."

# Main function
def main():
    intents = load_intents_education(file_path)
    vectorizer, label_encoder, model = train_chatbot_education(intents)
    
    print("Chatbot is running! Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        response = get_response_education(user_input, vectorizer, label_encoder, model, intents)
        print("Bot:", response)

if __name__ == "__main__":
    main()
