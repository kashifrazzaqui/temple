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
    chmod +x create_ts_project.py
    ```

3. **Create the Templates Directory**

    Ensure that you have a `templates` directory in the same directory as the script, containing the following files:

    - `index.html`
    - `index.ts`
    - `tsconfig.json`
    - `style.css`
    - `.gitignore`

    You can create these files using the provided content below.

4. **Run the Script**

    To create a new TypeScript project, run the script with the desired project name and target path:

    ```sh
    ./create_ts_project.py <project_name> <target_path>
    ```

    To specify a custom `tsconfig.json`, use the `--tsconfig` option:

    ```sh
    ./create_ts_project.py <project_name> <target_path> --tsconfig /path/to/custom/tsconfig.json
    ```

## File Contents

### `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{project_name}}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Welcome to {{project_name}}</h1>
    <script src="dist/index.js"></script>
</body>
</html>

