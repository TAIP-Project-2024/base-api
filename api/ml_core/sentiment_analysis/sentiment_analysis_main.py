from api.ml_core.models.model_factory import ModelFactory

import nltk

if __name__ == '__main__':
    # Ensure VADER lexicon data is downloaded
    nltk.download('vader_lexicon')

    # Example usage
    texts = ["He went to the park and had a great time!",
             "She failed her exam and felt miserable.",
             "I am going outside."]

    # Lexicon-based analysis
    print("Lexicon-based analysis:")
    lexicon_model = ModelFactory.create_model('sentiment', 'lexicon')
    for text in texts:
        # compound provides an overall sentiment score from -1 (most negative) to +1 (most positive).
        print(f"Text: {text}")
        print(f"Prediction: {lexicon_model.analyze(text)}")

    # BERT analysis
    print("\nBERT analysis:")
    bert_model = ModelFactory.create_model('sentiment', 'bert')
    for text in texts:
        print(f"Text: {text}")
        prediction = bert_model.analyze(text)
        print(f"Prediction: {prediction}")

    # LSTM analysis
    print("\nLSTM analysis:")
    lstm_model = ModelFactory.create_model('sentiment', 'lstm')
    predictions = lstm_model.analyze(texts)
    for i, text in enumerate(texts):
        print(f"Text: {text}")
        print(f"Prediction: {predictions[i]}")
        print()
