print("ERROR REPORTING EXAMPLE:")

def report_error(error_message):
    print(f"Error: {error_message}")

# Example usage
try:
    1 / 0   # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    report_error(str(e))

print("TRY: & EXCEPT BLOCKS ARE USED FOR ERROR HANDLING.")