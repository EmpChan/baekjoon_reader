# Baekjoon Problem Document Generator

## Description

This program reads a list of problem numbers from Baekjoon Online Judge, fetches the problem details, and generates a formatted `.docx` file.

## Usage

1.  **Install Dependencies:**
    Install the required Python libraries using pip.
    ```bash
    pip install -r requirements.txt
    ```
2. **Print a Problem Summary**

   Provide a problem number to `main.py` to print the title, description, input/output specifications, and all sample cases in the terminal.
   ```bash
   python src/main.py 1000
   ```

3.  **Generate the Document (Optional):**
    Create a file named `prob_list.txt` in the root directory of the project. Add the problem numbers you want to include in the document, with each number on a new line.

    **Example `prob_list.txt`:**
    ```
    1000
    1001
    2798
    ```
    Run the program without arguments (or override the defaults with `--doc-list`, `--doc-output`, `--tag`) to generate `output/problems.docx`.
    ```bash
    python src/main.py
    ```

    The CLI options:
    ```bash
    python src/main.py --doc-list prob_list.txt --doc-output output/problems.docx --tag imple
    ```

4.  **Check Output:**
    The generated document will be saved as `output/problems.docx`.
