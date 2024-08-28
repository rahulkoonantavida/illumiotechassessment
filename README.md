# illumio technical assessment

## Assumptions :
- logs.txt contains version 2 default logs ONLY
- the size of logs.txt DOES NOT exceed 10MB
- the number of mappings in lookup.txt DOES NOT exceed 10000
- formatting of logs.txt and lookup.txt is predictable (see sample files in `data` folder)
- remaining assumptions are made clear with comments in `main.py`

## Compilation :
This program strictly uses Python and its available built-in functions. In order to run the program:
1. Clone the [repository](https://github.com/rahulkoonantavida/illumiotechassessment.git).
2. Replace content of `logs.txt` and `lookup.txt` with desired data (formatting and filenames must remain consistent).
3. Run `python3 main.py` (other versions of Python may work, but have not been tested).
4. See the generated `output.txt` file for program output.

## Testing, Analysis, Other :
Due to the predictable format of data being parsed, testing was straightforward. `logs.txt` was populated with various numbers of rows, with various port and protocol numbers, and upon running `main.py`, the generated `output.txt` file was inspected for any discrepancies with respect to `lookup.txt`. By leveraging the data in `iana.txt`, the program can effectively distinguish different protocols and return the correct match counts for tags and (port, protocol) combinations in `output.txt`.

## Resources :
- Referenced the [IANA](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) website for information regarding assigned internet protocol numbers and used provided files to populate `iana.txt`.
