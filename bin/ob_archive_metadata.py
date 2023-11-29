#!/usr/bin/env python3

"""
Updates obsidian backlog notes metadata/frontmatter for archival
"""
import os
import re

from datetime import date

HOME = os.path.realpath(os.path.expandvars('$HOME'))
BACKLOG = f'{HOME}/workspace/projects/sheepskin/backlog'

# seach patterns
DONE = r'^\s*(---\nstatus: done.*?---)'
ARCHIVED = r'^\s*(---\nstatus: archived.*?---)'

# assert backlog directories exist
assert os.path.isdir(BACKLOG)


def validate_file_status(filename: str):
    """
    Returns true when file contains a metadata with status 'done'
    """
    metadata_complete = re.compile(DONE, flags=re.DOTALL)
    with open(filename, 'r') as data:
        metadata = metadata_complete.search(data.read())
        if metadata:
            print('INFO: Original metadata >>>> ')
            print(metadata.group())
            return True


def get_files(source_directory: str, exclusions: list) -> list:
    """
    Returns the absolute path to all markdown files in given directory,
    excluding
    - files from directories in the exclusion list
    - README files
    - files with metadata status different from 'done'
    """
    backlog_files = []
    for root, directories, files in os.walk(source_directory):
        directories[:] = [d for d in directories if d not in exclusions]
        for file in files:
            # Exclude all non markdown files and README
            if file.endswith(('.md', '.markdown')) and not (file.endswith('README.md')):
                filename = f'{root}/{file}'
                # Exclude all files with metadata status different from 'done'
                if validate_file_status(filename):
                    backlog_files.append(filename)
    return backlog_files


def update_metadata(files: list):
    """
    Updates status, archival date and priority
    """
    for filename in files:
        with open(filename, 'r') as file:
            lines = file.read()
            lines = lines.replace('status: done\n', 'status: archived\n', 1)
            lines = lines.replace(
                'archival date:\n', f'archival date: {date.today()}\n', 1
            )
            lines = re.sub(r'priority: \d\n', 'priority: 0\n', lines, 1)
            with open(filename, 'w') as data:
                data.write(lines)
                metadata_complete = re.compile(ARCHIVED, flags=re.DOTALL)
                print('INFO: New metadata >>>> ')
                print(metadata_complete.search(lines).group())
                print('INFO: Updated file >>>> ')
                print(f'{filename}')


files_to_archive = get_files(BACKLOG, [])
if not files_to_archive:
    print('INFO: No file was found with metadata in status done')
    print('WARN: No file was updated')
update_metadata(files_to_archive)
