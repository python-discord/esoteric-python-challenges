#! python3
"""
    test.py: Run test cases for a particular challenge
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
import json

try:
    with open("testcases.json") as tc:
        test_cases = json.load(tc)
except json.decoder.JSONDecodeError as e:
    print("Malformed test case file. Please inform a maintainer.", e)


def test(entry_point: "function") -> None:
    """Run all test cases against the specific function."""

    fails = []
    print("Running all test cases..\n")
    for i, t in enumerate(test_cases):
        output = entry_point(t['input'])
        if output == t['expected_output']:
            print(f"✓ Test case #{i}")
        else:
            print(f"✗ Test case #{i}")
            fails.append({"number": i, "input": t['input'],
                          "expected_output": t['expected_output'],
                          "actual": output})
    print("\nDone..\n")
    if fails:
        for f in fails:
            print(f"\nTest Case {f['number']} failed:")
            print(f"\nInput:\n{f['input']}\n")
            print(f"\nExpected Output:\n{f['expected_output']}")
            print(f"\nActual Output:\n{f['actual']}\n")
    else:
        print("All test cases passed!")


def case(case_number: int, entry_point: "function") -> bool:
    """Run a specific test case."""

    case = test_cases[case_number]
    print("Running test case", case_number, "..")
    output = entry_point(case['input'])
    if output == case['expected_output']:
        print(f"✓ Test case #{case_number} passed!")
        return True
    else:
        print(f"\nTest Case #{case_number} failed:")
        print(f"\nInput:\n{case['input']}\n")
        print(f"\nExpected Output:\n{case['expected_output']}")
        print(f"\nActual Output:\nf{output}")
    return False


if __name__ == "__main__":
    print("To use, import this module in your solution project/file.")
    sys.exit(0)
