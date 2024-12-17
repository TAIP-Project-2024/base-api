from api.ml_core.data_preprocess.text_preprocessor import TextPreprocessor


class BertPreprocessor(TextPreprocessor):
    """
    BertPreprocessor prepares text for BERT-based models, handling format conversion for Reddit-style data.
    Extends TextPreprocessor.
    """
    def __init__(self):
        super().__init__()

    @staticmethod
    def preprocess_bert(text):
        """
        Converts Reddit-specific placeholders (e.g., u/username -> @user) for compatibility with BERT.

        :param text: Input string
        :return: Preprocessed string compatible with BERT
        """
        new_text = []
        for t in text.split(" "):
            # placeholders for reddit data (BERT is trained on Twitter data)
            t = '@user' if t.startswith('u/') and len(t) > 1 else t
            t = 'http' if t.startswith('http') else t
            t = 'www' if t.startswith('www') else t
            t = 'subreddit' if t.startswith('r/') and len(t) > 1 else t
            new_text.append(t)
        return " ".join(new_text)

    def preprocess(self, text, **kwargs):
        """
        Executes the preprocessing pipeline for BERT-compatible formatting.

        :param text: Input string
        :return: Preprocessed string
        """
        return self.preprocess_bert(text)
