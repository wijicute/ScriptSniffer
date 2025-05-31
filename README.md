# Scriptsniffer

**Scriptsniffer** is a Python tool designed to extract all relative URLs (paths starting with `/`) from an online JavaScript file, convert them into absolute URLs, and save them into a text file named after the website's domain.

## 🚀 Features

- **Extract Relative URLs**: Identifies all paths starting with `/` within a JavaScript file.
- **Convert to Absolute URLs**: Transforms relative paths into complete URLs using the base domain.
- **Automatic File Naming**: Saves the extracted URLs into a `.txt` file named after the website's domain (e.g., `example.com.txt`).
- **Simple Command-Line Interface**: User-friendly interface requiring only the JavaScript file URL as input.

## 📦 Requirements

- Python 3.6 or higher
- `requests` library

## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YourUsername/scriptsniffer.git
   cd scriptsniffer

## ▶️ Usage

Run the script and provide the URL of the JavaScript file when prompted:

   ```bash
   python3 scriptsniffer.py
   ```
Example:
Enter the JavaScript file URL: https://example.com/script.js





