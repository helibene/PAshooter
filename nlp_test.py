# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:42:32 2023

@author: Alexandre
"""
from transformers import pipeline
generator = pipeline('text-generation', model = 'gpt2')
generator("Hello, I'm a language model", max_length = 30, num_return_sequences=3)
