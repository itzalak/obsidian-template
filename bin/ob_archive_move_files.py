#!/usr/bin/env python3

"""
Move archived obsidian backlog notes to archive folder
"""
import os
import re
import shutil

HOME = os.path.realpath(os.path.expandvars('$HOME'))
BACKLOG = f'{HOME}/workspace/projects/sheepskin/backlog'
ARCHIVE = f'{BACKLOG}/archive'

# search patterns
ARCHIVED = r'^\s*(---\nstatus: archived.*?---)'

# assert backlog directories exist
assert os.path.isdir(BACKLOG)
assert os.path.isdir(ARCHIVE)


def validate_file_status(filename: str):
    """
    Returns true when file contains a metadata with status 'archived'
    """
    metadata_complete = re.compile(ARCHIVED, flags=re.DOTALL)
    with open(filename, 'r') as data:
        metadata = metadata_complete.search(data.read())
        if metadata:
            return True


def get_files(source_directory: str, exclusions: list) -> list:
    """
    Returns the absolute path to all markdown files in given directory,
    excluding
    - files from directories in the exclusion list
    - README files
    - files with metadata status different from 'archived'
    """
    backlog_files = []
    for root, directories, files in os.walk(source_directory):
        directories[:] = [d for d in directories if d not in exclusions]
        for file in files:
            # Exclude all non markdown files and README
            if file.endswith(('.md', '.markdown')) and not (file.endswith('README.md')):
                filename = f'{root}/{file}'
                # Exclude all files with metadata status different from 'archived'
                if validate_file_status(filename):
                    backlog_files.append(filename)
    return backlog_files


def move_files(files: list):
    for file_path in files:
        if ARCHIVE not in file_path:
            new_path = f'{ARCHIVE}/{os.path.basename(file_path)}'
            print(f'Archived file {new_path}')
            shutil.move(file_path, new_path)


files_to_archive = get_files(BACKLOG, ['archive'])
if not files_to_archive:
    print('INFO: No file was found with metadata in status archived')
    print('WARN: No file was moved')
move_files(files_to_archive)
