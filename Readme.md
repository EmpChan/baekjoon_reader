# Baekjoon Problem Document Generator

## Description

This program reads a list of problem numbers from Baekjoon Online Judge, fetches the problem details, and generates a formatted `.docx` file.

## Usage

1.  **Install Dependencies:**
    Install the required Python libraries using pip.
    ```bash
    pip install -r requirements.txt
    ```
2.  **Create Problem List:**
    Create a file named `prob_list.txt` in the root directory of the project. Add the problem numbers you want to include in the document, with each number on a new line.

    **Example `prob_list.txt`:**
    ```
    1000
    1001
    2798
    ```
3.  **Run the Program:**
    Execute the `main.py` script from the `src` directory.
    ```bash
    python src/main.py
    ```
4.  **Check Output:**
    The generated document will be saved as `output/problems.docx`.
