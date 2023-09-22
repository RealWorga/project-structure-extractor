#!/usr/bin/env python3

import os

def extract_structure(path, file_handle, prefix='', include_hidden=False, ignore_list=None):
    if not ignore_list:
        ignore_list = []

    absolute_path = os.path.abspath(path)
    if absolute_path in ignore_list:
        return

    if os.path.isdir(path):
        items = sorted([item for item in os.listdir(path)
                        if (include_hidden or not item.startswith('.'))
                        and os.path.join(path, item) not in ignore_list])

        for index, item in enumerate(items):
            is_last = index == len(items) - 1
            item_path = os.path.join(path, item)

            line_prefix = '└── ' if is_last else '├── '

            if os.path.isdir(item_path):
                file_handle.write(f"{prefix}{line_prefix}{item}/\n")
                new_prefix = prefix + ('    ' if is_last else '│   ')
                extract_structure(item_path, file_handle, new_prefix, include_hidden, ignore_list)
            else:
                file_handle.write(f"{prefix}{line_prefix}{item}\n")
    else:
        file_handle.write(f"{prefix}└── {os.path.basename(path)}\n")