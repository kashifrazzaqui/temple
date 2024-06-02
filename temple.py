#!/usr/bin/env python3

import os
import sys
import argparse
import json
import subprocess

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def create_project_directory(target_path, project_name):
    project_path = os.path.join(target_path, project_name)
    try:
        os.makedirs(project_path)
        print(f"Created project directory: {project_path}")
    except FileExistsError:
        print(f"Directory {project_path} already exists")
    return project_path

def create_boilerplate_files(project_path, project_name, tsconfig_path=None):
    # Create src directory
    src_path = os.path.join(project_path, 'src')
    os.makedirs(src_path, exist_ok=True)

    # Create index.html
    index_html_content = read_file('templates/index.html').replace('{{project_name}}', project_name)
    with open(os.path.join(project_path, 'index.html'), 'w') as f:
        f.write(index_html_content)
    print("Created index.html")

    # Create src/main.ts
    main_ts_content = read_file('templates/main.ts').replace('{{project_name}}', project_name)
    with open(os.path.join(src_path, 'main.ts'), 'w') as f:
        f.write(main_ts_content)
    print("Created src/main.ts")

    # Create style.css
    style_css_content = read_file('templates/style.css')
    with open(os.path.join(project_path, 'style.css'), 'w') as f:
        f.write(style_css_content)
    print("Created style.css")

    # Handle tsconfig.json
    tsconfig_default_content = json.loads(read_file('templates/tsconfig.json'))

    if tsconfig_path:
        tsconfig_path = os.path.abspath(tsconfig_path)
        if os.path.exists(tsconfig_path):
            os.symlink(tsconfig_path, os.path.join(project_path, 'tsconfig.json'))
            print(f"Softlinked tsconfig.json from {tsconfig_path}")
        else:
            print(f"tsconfig.json not found at {tsconfig_path}, creating default tsconfig.json")
            with open(os.path.join(project_path, 'tsconfig.json'), 'w') as f:
                json.dump(tsconfig_default_content, f, indent=4)
    else:
        with open(os.path.join(project_path, 'tsconfig.json'), 'w') as f:
            json.dump(tsconfig_default_content, f, indent=4)
        print("Created default tsconfig.json")

def initialize_npm(project_path):
    try:
        subprocess.run(['npm', 'init', '-y'], cwd=project_path, check=True)
        print("Initialized npm project")
    except subprocess.CalledProcessError as e:
        print(f"Error initializing npm: {e}")
        sys.exit(1)

def install_dependencies(project_path):
    try:
        subprocess.run(['npm', 'install', 'typescript', 'live-server', 'concurrently', '--save-dev'], cwd=project_path, check=True)
        print("Installed npm dependencies")
    except subprocess.CalledProcessError as e:
        print(f"Error installing npm dependencies: {e}")
        sys.exit(1)

def initialize_git(project_path):
    try:
        subprocess.run(['git', 'init'], cwd=project_path, check=True)
        print("Initialized git repository")
        # Create a .gitignore file
        gitignore_content = read_file('templates/.gitignore')
        with open(os.path.join(project_path, '.gitignore'), 'w') as f:
            f.write(gitignore_content)
        print("Created .gitignore")
    except subprocess.CalledProcessError as e:
        print(f"Error initializing git: {e}")
        sys.exit(1)

def update_package_json(project_path):
    package_json_path = os.path.join(project_path, 'package.json')
    with open(package_json_path, 'r') as f:
        package_json = json.load(f)

    package_json['scripts'] = {
        "start": "concurrently \"npm run tsc\" \"npm run serve\"",
        "tsc": "tsc --watch",
        "serve": "live-server --watch=dist,src,index.html,style.css"
    }

    with open(package_json_path, 'w') as f:
        json.dump(package_json, f, indent=2)
    print("Updated package.json with start, tsc, and serve scripts")

def main():
    parser = argparse.ArgumentParser(description="Create a new TypeScript project.")
    parser.add_argument('project_name', type=str, help="The name of the project")
    parser.add_argument('target_path', type=str, help="The target path to create the project under")
    parser.add_argument('--tsconfig', type=str, help="Path to a custom tsconfig.json")

    args = parser.parse_args()

    project_name = args.project_name
    target_path = args.target_path
    tsconfig_path = args.tsconfig

    project_path = create_project_directory(target_path, project_name)
    initialize_npm(project_path)
    install_dependencies(project_path)
    create_boilerplate_files(project_path, project_name, tsconfig_path)
    initialize_git(project_path)
    update_package_json(project_path)

if __name__ == "__main__":
    main()

