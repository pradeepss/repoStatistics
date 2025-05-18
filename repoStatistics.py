import os
import re
import argparse
import json
from typing import Dict


def get_file_extensions() -> Dict[str, str]:
    """Get supported file extensions and their language names"""
    return {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.java': 'Java',
        '.cpp': 'C++',
        '.c': 'C',
        '.go': 'Go',
        '.rs': 'Rust',
        '.rb': 'Ruby',
        '.php': 'PHP',
        '.html': 'HTML',
        '.css': 'CSS',
        '.yml': 'YAML',
        '.yaml': 'YAML',
        '.json': 'JSON',
        '.xml': 'XML'
    }


def is_code_line(line: str) -> bool:
    """Check if a line is a code line (non-empty and not a comment)"""
    line = line.strip()
    if not line:
        return False

    # Check for common comment patterns
    if line.startswith(('#', '//', '/*', '*/', '--')):
        return False

    # Check for YAML frontmatter
    if line.startswith('---'):
        return False

    return True


def is_comment_line(line: str) -> bool:
    """Check if a line is a comment line"""
    line = line.strip()
    if not line:
        return False

    # Check for common comment patterns
    if line.startswith(('#', '//', '/*', '*/', '--')):
        return True

    # Check for YAML frontmatter
    if line.startswith('---'):
        return True

    return False


def count_code_statistics(directory: str, output_format: str = 'text') -> Dict[str, Dict[str, int]]:
    """
    Count code statistics for files in a directory.

    Args:
        directory: Path to analyze
        output_format: Format for output ('text' or 'json')

    Returns:
        Dictionary containing file statistics
    """
    stats = {}
    extensions = get_file_extensions()

    try:
        for root, _, files in os.walk(directory):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in extensions:
                    path = os.path.join(root, file)
                    try:
                        with open(path, "r", encoding="utf-8", errors="ignore") as f:
                            lines = f.readlines()
                    except Exception as e:
                        print(f"Warning: Could not read {path}: {str(e)}")
                        continue

                    code_lines = sum(1 for line in lines if is_code_line(line))
                    comment_lines = sum(1 for line in lines if is_comment_line(line))
                    total_lines = len(lines)

                    if ext not in stats:
                        stats[ext] = {
                            "files": 0,
                            "lines": 0,
                            "comments": 0,
                            "total_lines": 0,
                            "language": extensions[ext]
                        }

                    stats[ext]["files"] += 1
                    stats[ext]["lines"] += code_lines
                    stats[ext]["comments"] += comment_lines
                    stats[ext]["total_lines"] += total_lines

        return stats

    except Exception as e:
        print(f"Error processing directory: {str(e)}")
        return {}


def format_output(stats: Dict[str, Dict[str, int]], format_type: str = 'text') -> str:
    """
    Format statistics output in specified format.

    Args:
        stats: Dictionary containing file statistics
        format_type: Output format ('text' or 'json')

    Returns:
        Formatted output string
    """
    if format_type == 'json':
        return json.dumps(stats, indent=2)

    output = "\nCode Statistics Report\n" + "=" * 50 + "\n\n"

    total_files = 0
    total_code_lines = 0
    total_comment_lines = 0
    total_total_lines = 0

    for ext, data in stats.items():
        total_files += data["files"]
        total_code_lines += data["lines"]
        total_comment_lines += data["comments"]
        total_total_lines += data["total_lines"]

        output += f"Language: {data['language']} ({ext})\n"
        output += f"Files: {data['files']}\n"
        output += f"Code Lines: {data['lines']}\n"
        output += f"Comment Lines: {data['comments']}\n"
        output += f"Total Lines: {data['total_lines']}\n"
        if data['comments'] != 0:
            output += f"Code to Comment Ratio: {data['lines'] / data['comments']:.2f}\n"
        else:
            output += f"Code to Comment Ratio: N/A\n"
        output += "-" * 50 + "\n\n"

    output += "Summary\n" + "=" * 50 + "\n"
    output += f"Total Files: {total_files}\n"
    output += f"Total Code Lines: {total_code_lines}\n"
    output += f"Total Comment Lines: {total_comment_lines}\n"
    output += f"Total Lines: {total_total_lines}\n"
    if total_comment_lines != 0:
        output += f"Overall Code to Comment Ratio: {total_code_lines / total_comment_lines:.2f}\n"
    else:
        output += f"Overall Code to Comment Ratio: N/A\n"

    return output


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description='Analyze code statistics in a directory')
    parser.add_argument('directory', help='Directory to analyze')
    parser.add_argument('--format', choices=['text', 'json'], default='text',
                        help='Output format (text or json)')

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory")
        return

    stats = count_code_statistics(args.directory)
    print(format_output(stats, args.format))


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()