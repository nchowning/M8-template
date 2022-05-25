#!/usr/bin/env python3

#
# TABLES
#
# All of the reserved tables

tables = {
    # 80-8F: MAJOR CHORDS
    0x80: [  # Root note
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x04, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x07, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "HOP", 0x00, "---", 0x00, "---", 0x00],
    ],
    0x81: [  # Root note + 4
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x03, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x08, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "HOP", 0x00, "---", 0x00, "---", 0x00],
    ],
    0x82: [  # Root note + 7
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x05, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x09, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "HOP", 0x00, "---", 0x00, "---", 0x00],
    ],

    # 90-9F: MINOR CHORDS
    0x90: [  # Root note
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x03, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x07, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "HOP", 0x00, "---", 0x00, "---", 0x00],
    ],
    0x91: [  # Root note + 3
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x04, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x09, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "HOP", 0x00, "---", 0x00, "---", 0x00],
    ],
    0x92: [  # Root note + 7
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x05, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x08, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "HOP", 0x00, "---", 0x00, "---", 0x00],
    ],

    "empty": [  # Template of an empty table
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
        [0x00, "--", "---", 0x00, "---", 0x00, "---", 0x00],
    ]
}

if __name__ == "__main__":
    print("WARNING: 'template.py' is not meant to be run interactively.",
          "This file contains the template data in python objects - edit it and run 'display.py'")