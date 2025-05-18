# RepoStats - Repository Statistics Analyzer

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful command-line tool for analyzing code statistics across repositories. RepoStats provides detailed insights into your codebase, including file counts, code lines, comments, and more.

## Features

- 📊 Detailed code statistics for multiple programming languages
- 📊 Code to comment ratio analysis
- 📊 Support for 15+ programming languages
- 📊 JSON and text output formats
- 🚀 Fast directory traversal
- 🛡️ Robust error handling
- 📚 Type-safe implementation

## Supported Languages

- Python (.py)
- JavaScript (.js)
- TypeScript (.ts)
- Java (.java)
- C++ (.cpp)
- C (.c)
- Go (.go)
- Rust (.rs)
- Ruby (.rb)
- PHP (.php)
- HTML (.html)
- CSS (.css)
- YAML (.yml, .yaml)
- JSON (.json)
- XML (.xml)

## Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/repostats.git
```

Or install directly:
```bash
pip install git+https://github.com/yourusername/repostats.git
```

## Usage

Basic usage:
```bash
python repostats.py /path/to/repository
```

With JSON output:
```bash
python repostats.py /path/to/repository --format json
```

## Example Output

```text
Code Statistics Report
==================================================

Language: Python (.py)
Files: 45
Code Lines: 1234
Comment Lines: 345
Total Lines: 1789
Code to Comment Ratio: 3.58
--------------------------------------------------

Language: JavaScript (.js)
Files: 23
Code Lines: 890
Comment Lines: 123
Total Lines: 1054
Code to Comment Ratio: 7.24
--------------------------------------------------

Summary
==================================================
Total Files: 68
Total Code Lines: 2124
Total Comment Lines: 468
Total Lines: 2843
Overall Code to Comment Ratio: 4.54
```

## Output Format

The tool provides two output formats:

1. **Text Format** (default):
   - Human-readable report
   - Detailed statistics per language
   - Summary statistics
   - Code to comment ratios

2. **JSON Format**:
   ```json
   {
     ".py": {
       "files": 45,
       "lines": 1234,
       "comments": 345,
       "total_lines": 1789,
       "language": "Python"
     },
     "summary": {
       "total_files": 68,
       "total_code_lines": 2124,
       "total_comment_lines": 468,
       "total_lines": 2843
     }
   }
   ```

## Development

The code follows Python best practices:
- Type hints for better IDE support
- Proper error handling
- Clean code structure
- Well-documented functions
- Modular design

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- Thanks to all contributors
- Special thanks to the Python community
- Inspired by various code analysis tools
