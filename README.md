**Project Description — AI-Powered Web Content Summarizer & X (Twitter) Post Generator**

This Python script automates the process of extracting, summarizing, and generating social media posts from any given website URL using OpenAI’s GPT models.

**Overview**
**The script performs a 4-step pipeline:**
**Fetch Website Content**
Downloads the HTML content of a given webpage using the requests library.
Handles errors gracefully in case of invalid or unreachable URLs.

**Extract Core Website Text**
Uses an OpenAI model (gpt-5-nano) to clean and extract the main readable content from the raw HTML.
Removes navigation bars, footers, scripts, and ads — keeping only the central article or post content.

**Summarize Extracted Content**
Summarizes the extracted text into a short, concise overview using GPT.
The summary is formatted in bullet points for readability and focus.

**Generate an X (Twitter) Post**
Reads example post templates from a local JSON file (post-examples.json).
Passes the summary and example posts to GPT, prompting it to create an engaging, platform-ready X post that mirrors your desired tone, length, and structure.

**Key Components**
Function	Purpose
get_website_html(url)	Fetches and returns raw HTML from a provided website URL.
extract_core_website_content(html)	Uses GPT to extract readable text (main content) from the HTML structure.
summarize_content(content)	Summarizes the extracted text into a concise format (bullet points).
generate_x_post(summary)	Generates a short, catchy X (Twitter) post using provided examples as style references.
main()	Coordinates the full process: fetch → extract → summarize → generate.

**Technologies Used**
Python 3
OpenAI GPT-5-nano model (for text extraction, summarization, and post generation)
Requests (for web scraping)
JSON (for reading example posts and storing data)
