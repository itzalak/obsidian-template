# Obsidian zettlekasten notes

## Table of contents

* [Introduction](#introduction)
* [Features](#features)
* [Structure](#structure)
* [Notes](#notes)
* [Community Plugins](#community-plugins)
* [Technologies](#technologies)

## Introduction

Obsidian is a flexible note taking app that allows me to use my current zettlekasten template and markdown type file to
save notes.

The goal is to use flexibly obsidian and zettlekasten to save notes and using a generic markdown file based on a defined
template and save it using a git repository.

Obsidian saves notes in
a [flavour of Markdown](https://help.obsidian.md/Editing+and+formatting/Obsidian+Flavored+Markdown) format in a vault -
a directory - where it also stores all the configuration and plugins.

## Features

* Create zettlekasten style scratch notes based on [scratch](/templates/scratch-template.md) template, when note is
  definitive it becomes a zettlekasten, and it is moved to `notes/zettlekasten`
* Write down and maintain a list project ideas, tasks, meeting notes, diagrams, etc, via templates. Details in the [[backlog/README|backlog readme]] - example notes exist under backlog directories for saving project views configuration.
* Curate important snippets like commands cheatsheets and cookbook actions under `notes` directory
* Configuration and template should be usable as markdown files outside of obsidian (TODO)

### Obsidian exclusive

* Book notes and management using book search plugin and dataview for presentation (not possible to maintain outside
  obsidian)

## Structure

```
├── backlog
│   ├── README.md
│   ├── archive
│   ├── stack
│   └── tasks
├── bin
├── books
│   ├── The Clean Coder - Robert C Martin.md
│   ├── The Pragmatic Programmer - David Thomas Andrew Hunt.md
│   └── bookshelf.md
├── notes
│     ├── cheatsheet
│     ├── cookbook
│     ├── scratch
│     └── zettlekasten
└── templates
      ├── book-template.md
      ├── cheatsheet-template.md
      ├── epic-template.md
      ├── meeting-template.md
      ├── scratch-template.md
      └── task-template.md
```

## Notes

1. [Obsidian Markdown Flavour](https://help.obsidian.md/Editing+and+formatting/Obsidian+Flavored+Markdown) is different
   from other common flavours and does not support full scope of features, some conflicts will occur when using
   automation and when using other editors to change text
2. Obsidian allows dictionaries through community plugins, but they are limited by comparison to Grammarly or even
   Jetbrains tools
3. Using git to sync the vault requires the use of `.gitkeep` files otherwise the directory structure will not be synced
4. The existent [pre-commit](/.pre-commit-config.yaml) requires the exclusion of the `.obsidian` directory to avoid
   constant conflicts
5. Workspace configuration is excluded from git sync through `.gitignore` to prevent conflict

## Community Plugins

* [Templater](https://github.com/SilentVoid13/Templater)
* [Dataview](https://github.com/blacksmithgu/obsidian-dataview)
* [Commander](https://github.com/phibr0/obsidian-commander)
* [Quick Add](https://github.com/chhoumann/quickadd)
* [Projects](https://github.com/marcusolsson/obsidian-projects)
* [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin)
* [Book Search](https://github.com/anpigon/obsidian-book-search-plugin)
* [Execute Code](https://github.com/twibiral/obsidian-execute-code)
* [Minimal Theme Settings](https://github.com/kepano/obsidian-minimal-settings)

### Others

Multiple other plugins not included that can be useful or interesting to include in obsidian workflow.

* [Calibre](https://github.com/caronchen/obsidian-calibre-plugin) - read and take notes using calibre server
* [Advanced slides](https://github.com/MSzturc/obsidian-advanced-slides) - markdown slides
* [Advanced tables](https://github.com/tgrosinger/advanced-tables-obsidian) - handle markdown tables
* [Kanban](https://github.com/mgmeyers/obsidian-kanban)
* [Annotator](https://github.com/elias-sundqvist/obsidian-annotator) - open and annotate pdf and epub files

## Technologies

* [Obsidian](https://obsidian.md/)
* [Zettlekasten](https://zenkit.com/en/blog/a-beginners-guide-to-the-zettelkasten-method/)
