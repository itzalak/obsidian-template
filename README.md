# Obsidian zettlekasten notes

## Table of contents

* [Introduction](#introduction)
* [Features](#features)
* [Structure](#structure)
* [Community Plugins](#community-plugins)
* [Technologies](#technologies)

## Introduction

Obsidian is a flexible note taking app that allows me to use my current zettlekasten template and markdown type file to save notes.

The goal is to use flexibly obsidian and zettlekasten to save notes and using a generic markdown file based on a defined template and save it using a git repository.

An added benefit would be to be able to easily sync with smartphone - without cost.

Obsidian saves notes in markdown format in a vault - or folder - where it also stores all the configuration and plugins.
## Features

* Create zettlekasten style notes based on [scratch](/templates/scratch-template.md) template, unfinished notes go under `notes/scratch` directory, definitive notes under `notes/zettlekasten`
* Write down and maintain a list project ideas via [idea](/templates/idea-template.md) template under `project` directory
* Maintain a journal under `journal/sprint` directory and connected with tasks under `journal/tasks` directory using [sprint](/templates/sprint-template.md) and [task](/templates/task-template.md) templates
* Curate important snippets like commands and dictionary under `notes` directory
* Configuration and template should be usable as markdown files outside of obsidian (this might conflict with templater scripts!)
## Structure

```
├── journal
│   ├── sprint
│   └── tasks
├── notes
│   ├── cheatsheet
│   ├── dictionary
│   ├── scratch
│   └── zettlekasten
├── projects
└── templates
    ├── cheatsheet-template.md
    ├── idea-template.md
    ├── scratch-template.md
    ├── sprint-template.md
    └── task-template.md
```


## Community Plugins

* [Dictionary](https://github.com/phibr0/obsidian-dictionary)
* [Templater](https://github.com/SilentVoid13/Templater)

## Technologies

* [Obsidian](https://obsidian.md/)
* [Zettlekasten](https://zenkit.com/en/blog/a-beginners-guide-to-the-zettelkasten-method/)
* [Templater Documentation](https://silentvoid13.github.io/Templater/)
