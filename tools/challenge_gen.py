#! python3
"""
    challenge_gen.py: Generate directory structure and templates for challenges
    Copyright (C) 2018  Shawn McLaughlin

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import sys
import shutil
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: py challenge_gen.py <challenge number> \"<name>\"")
        sys.exit()

    challenge_number, challenge_name = sys.argv[1:]

    try:
        challenge_num = int(challenge_number)
    except ValueError as e:
        print("Challenge number must be a valid integer")
        sys.exit()

    challenge_number = str(
        challenge_num) if challenge_num > 9 else "0"+str(challenge_num)

    dir_name = f"{challenge_number}-{'-'.join(challenge_name.split())}"
    current_dirname = os.path.dirname(__file__)
    new_dir_path = os.path.join(current_dirname, '..', 'challenges', dir_name)
    solutions_dir = os.path.join(new_dir_path, 'solutions')
    readme_template = os.path.join(current_dirname, 'templates', 'README.md')
    testrunner = os.path.join(current_dirname, 'templates', 'test_runner.py')
    testcases = os.path.join(current_dirname, 'templates', 'testcases.json')

    # Create challenge directory
    os.mkdir(new_dir_path)
    # Create a directory for solutions underneath
    os.mkdir(solutions_dir)
    # Add an __init__.py mostly to force commit of otherwise empty dir
    with open(os.path.join(solutions_dir, '__init__.py'), "w") as _:
        pass
    # Copy the template and test cases into the challenge folder
    shutil.copy(readme_template, new_dir_path)
    shutil.copy(testrunner, new_dir_path)
    shutil.copy(testcases, new_dir_path)

    print(f"Deployed template for {dir_name}")
