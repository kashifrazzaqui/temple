
# TypeScript Project Setup Script
This script helps you to quickly set up a new TypeScript project with the necessary boilerplate files, directory structure, and npm dependencies. It also initializes a git repository and creates a `.gitignore` file with relevant entries.

## Prerequisites

- Python 3.x
- Node.js and npm

## Usage

1. **Clone or Download the Repository**

    First, clone or download this repository to your local machine.

2. **Make the Script Executable**

    If not already executable, make the script executable by running:

    ```sh
    chmod +x temple.py
    ```

3. **Update the Templates Directory**

    Update the following files to suit your taste, if required.

    - `index.html`
    - `index.ts`
    - `tsconfig.json`
    - `style.css`
    - `.gitignore`

4. **Run the Script**

    To create a new TypeScript project, run the script with the desired project name and target path:

    ```sh
    ./temple.py <project_name> <target_path>
    ```

    To specify a custom `tsconfig.json`, use the `--tsconfig` option:
    This tsconfig will be soft-linked and not copied.

    ```sh
    ./temple.py <project_name> <target_path> --tsconfig /path/to/custom/tsconfig.json
    ```

    To run the server with auto reloading

    ```sh
    npx live-server --watch=src --watch=index.html --watch=style.css
    ```
