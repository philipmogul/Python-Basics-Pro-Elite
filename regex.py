def main():
    print("REGULAR EXPRESSIONS IN PYTHON")
    import re
    pattern = r'\bfoo\b'
    test_string = "foo bar foobar foo"
    matches = re.findall(pattern, test_string)
    print(f"Pattern: {pattern}")
    print(f"Matches: {matches}")

    # using re.search to find first occurrence
    first_match = re.search(pattern, test_string)
    if first_match:
        print(f"First match found at index: {first_match.start()} to {first_match.end()}")

    # using re.sub to replace occurrences
    replaced_string = re.sub(pattern, 'baz', test_string)
    print(f"Replaced string: {replaced_string}")

    # using compiled regex
    compiled_pattern = re.compile(pattern)
    compiled_matches = compiled_pattern.findall(test_string)
    print(f"Compiled pattern matches: {compiled_matches}")

    # using re.match to check if string starts with pattern
    match_at_start = re.match(pattern, test_string)
    if match_at_start:
        print("String starts with the pattern.")
    else:
        print("String does not start with the pattern.")

    pattern_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email_test_string = "Please contact us at support@example.com or admin@test.org"
    email_matches = re.findall(pattern_email, email_test_string)
    print(f"Email pattern: {pattern_email}")
    print(f"Email matches: {email_matches}")


    pattern_digits = r'\d+'
    digits_test_string = "There are 2 apples and 10 bananas."
    digits_matches = re.findall(pattern_digits, digits_test_string)
    print(f"Digits pattern: {pattern_digits}")
    print(f"Digits matches: {digits_matches}")


    pattern_ignore_case = r'hello'
    ignore_case_test_string = "Hello world! hello everyone!"
    ignore_case_matches = re.findall(pattern_ignore_case, ignore_case_test_string, re.IGNORECASE)
    print(f"Ignore case pattern: {pattern_ignore_case}")
    print(f"Ignore case matches: {ignore_case_matches}")


if __name__ == "__main__":main()