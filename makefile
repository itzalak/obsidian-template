# Makefile

pre-commit: setup-pre-commit update-pre-commit

setup-pre-commit:
	pre-commit install

update-pre-commit:
	pre-commit autoupdate

archive-metadata:
	python3 $(HOME)/workspace/projects/sheepskin/bin/ob_archive_metadata.py

archive-files:
	python3 $(HOME)/workspace/projects/sheepskin/bin/ob_archive_move_files.py
