class MetadataService:

    def __init__(self):
        pass

    @staticmethod
    def generate_metadata_for_post(author, post, reactions):
        """
        maybe generate some json storing sentiment analysis results.
        """
        metadata = {"author": author, "post": post, "reactions": reactions}
        return metadata