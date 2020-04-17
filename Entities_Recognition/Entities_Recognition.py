# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT EDIT! This is a generated sample ("Request",  "language_entities_text")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-language

# sample-metadata
#   title: Analyzing Entities
#   description: Analyzing Entities in a String
#   usage: python3 samples/v1/language_entities_text.py [--text_content "California is a state."]

# [START language_entities_text]
from google.cloud import language_v1
from google.cloud.language_v1 import enums


def sample_analyze_entities(text_content):
    """
    Analyzing Entities in a String
    Args:
      text_content The text content to analyze
    """
    entities = []
    client = language_v1.LanguageServiceClient()

    # text_content = 'California is a state.'

    # [START language_python_migration_entities_text]
    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_entities(document, encoding_type=encoding_type)
    # Loop through entitites returned from the API
    for entity in response.entities:
        entities.append(entity.name)
    
    return entities

def main():
    text = "Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430)"
    entities = sample_analyze_entities(text)
    print(entities)

if __name__ == "__main__":
    main()