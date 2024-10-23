#!/usr/bin/env python3
""" Create a readme using Gemini ai """

from google import generativeai as genai
import os
import sys


genai.configure(api_key=os.getenv('GEMINI_API_KEY'))


model = genai.GenerativeModel("gemini-1.5-flash")

try:
    project_name = sys.argv[1]
except KeyError:
    print('Please pass the project name as an argument')
    sys.exit(1)

prompt = f"""
Design a detailed README for a project named "{project_name}".
Include the following sections:
Explain "{project_name}" in a few sentences.
1. Project Description
2. Installation Instructions
3. Usage Instructions
4. Contributing Guidelines
5. License Information
"""

response = model.generate_content(prompt)
print(response.text)
print(response.json)
