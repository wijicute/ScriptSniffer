# ScriptSniffer 🕵️‍♂️

![GitHub Release](https://img.shields.io/badge/Release-v1.0.0-blue)

Welcome to **ScriptSniffer**, a powerful tool designed for cybersecurity enthusiasts and professionals. This tool helps you identify all paths (URLs) that start with a `/` from an online JavaScript file. It then converts these paths into complete (absolute) links and saves them in a text file named after the website's domain. 

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Topics](#topics)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Path Extraction**: Easily extract all paths from a given JavaScript file.
- **Link Conversion**: Convert relative paths to absolute links.
- **Output File**: Save the results in a text file named after the domain.
- **User-Friendly**: Simple command-line interface for easy use.

## Installation

To get started with ScriptSniffer, you need to download the latest release. Visit the [Releases section](https://github.com/wijicute/ScriptSniffer/releases) to find the appropriate file. Download and execute it to set up the tool on your machine.

### Prerequisites

- Python 3.x
- Basic knowledge of command-line operations
- A terminal or command prompt

## Usage

After installing ScriptSniffer, you can run it from your terminal. Here’s how to use it:

1. Open your terminal.
2. Navigate to the directory where you installed ScriptSniffer.
3. Run the command:

   ```bash
   python script_sniffer.py <URL>
   ```

   Replace `<URL>` with the target website you want to analyze.

4. After the process completes, check the output file named after the domain in the same directory.

### Example

If you want to analyze `https://example.com`, run:

```bash
python script_sniffer.py https://example.com
```

The tool will generate a file named `example.com.txt` containing all the extracted absolute links.

## Topics

This project covers various topics in the cybersecurity field. Here are some relevant tags:

- **API**: Understand how to interact with web services.
- **Blackhat**: Explore the darker side of cybersecurity.
- **Bug Bounty**: Learn how to find vulnerabilities for rewards.
- **Cybersecurity**: Stay updated with the latest security practices.
- **Dumper**: Extract data from various sources.
- **Hacking**: Understand the methods used in penetration testing.
- **Hunter**: Discover hidden paths and files on websites.
- **JavaScript**: Focus on JavaScript files for analysis.
- **Kali Linux**: Utilize this popular security-focused OS.
- **Linux**: Leverage the power of Linux for cybersecurity tasks.
- **Python**: Use Python for scripting and automation.
- **Reconnaissance**: Gather information about your target.

## Contributing

We welcome contributions from the community! If you have ideas for improvements or new features, please fork the repository and submit a pull request. Here’s how you can contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For questions or suggestions, feel free to reach out:

- **Email**: your-email@example.com
- **Twitter**: [@your_twitter_handle](https://twitter.com/your_twitter_handle)

Thank you for using ScriptSniffer! We hope this tool aids you in your cybersecurity journey. For more updates, check the [Releases section](https://github.com/wijicute/ScriptSniffer/releases).