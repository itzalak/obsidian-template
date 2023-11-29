# Scripts

This script depends upon:

- Python being installed
- $HOME being defined
- Correct path to bin folder under obsidian folder
- Correct shell path

**WARNS:**

- This is a WIP, it has tight coupling to existent backlog structure
- To run these scripts execute code requires configuration of the path to shell, current config is meant for linux and it is not compatible for macOS

## Check python

```run-shell
python3 --version
```

## Check home

```run-shell
echo $HOME
```

## Check shell

```run-shell
which zsh
```

## Update metadata

Update metadata for files with status done.

```run-shell
python $HOME/workspace/projects/sheepskin/bin/ob_archive_metadata.py
```

## Move to archive

Move files with metadata status archived to archive folder

```run-shell
python $HOME/workspace/projects/sheepskin/bin/ob_archive_move_files.py
```
