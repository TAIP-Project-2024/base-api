#######################################################
# 
# SentimentAnalyzer.py
# Python implementation of the Interface SentimentAnalyzer
# Generated by Enterprise Architect
# Created on:      11-Nov-2024 11:16:01 PM
# Original author: stefan
# 
#######################################################


class SentimentAnalyzer:
    def __init__(self):
        self.method = None

    def set_method(self, method):
        self.method = method

    def analyze(self, text):
        if not self.method:
            raise ValueError("No analysis method set.")
        return self.method.analyze(text)
