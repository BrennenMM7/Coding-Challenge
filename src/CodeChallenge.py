import argparse
import re
from collections import Counter
import sys


def format_data_files(document_path):
    with open(document_path, 'r', encoding="utf8") as txtFile:
        Formatted_Words = (txtFile.read()).lower()
        Removed_LineBreaks = Formatted_Words.replace('\n', ' ')
        NonWord_Chars_Removed = re.sub(
            r"[^a-zA-Z0-9' ]+", repl='', string=Removed_LineBreaks)
        parsed_Word_List = re.findall(
            r"(?:^|(?<=\s))[A-Za-z0-9_'\-]+(?=\s|$|\b)", NonWord_Chars_Removed)
        return parsed_Word_List


def format_data_stdin():
    Formatted_Words = sys.stdin.read().lower()
    Removed_LineBreaks = Formatted_Words.replace('\n', ' ')
    NonWord_Chars_Removed = re.sub(
        r"[^a-zA-Z0-9' ]+", repl='', string=Removed_LineBreaks)
    parsed_Word_List = re.findall(
        r"(?:^|(?<=\s))[A-Za-z0-9_'\-]+(?=\s|$|\b)", NonWord_Chars_Removed)
    return parsed_Word_List


def analyze_word_list(WordList):
    Counted_Phrases = Counter(
        tuple(WordList[i:i+3]) for i in range(len(WordList)-3))
    return Counted_Phrases.most_common(100)


def output_information(Results, filename):
    print('----------------Results for "{}"-------------------'.format(filename))
    for each in Results:
        print(each[0][0], each[0][1], each[0][2], ' - ', each[1])
    print('-------------------------------------')


def Main():
    if not sys.stdin.isatty():
        WordList = format_data_stdin()
        Results = analyze_word_list(WordList)
        output_information(Results, "Terminal Input")
    else:
        parser = argparse.ArgumentParser(
            description='List of TXT Files to Scan')
        parser.add_argument('-f', '--files', nargs='+',
                            help='Please provide a single or series of .txt file paths')
        args = parser.parse_args()
        for document_path in args.files:
            WordList = format_data_files(document_path)
            Results = analyze_word_list(WordList)
            output_information(Results, document_path)


if __name__ == '__main__':
    Main()
