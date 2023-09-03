# Backlog

## Concept

This is a *WIP* organization system inspired by [P.A.R.A.](https://fortelabs.com/blog/para/) and the agile scrum system.

Goals:
* Plan and record ideas for future projects
* Create task for working in ideas and short term achievable projects
* Store and record all results and artifacts achieved

## File structure

```sh
projects
├── archive
├── stack
└── tasks
```

### Tasks

* Short term goals
* Work in progress

### Stack

Filenames for raw ideas are prefixed with epic for symmetry with JIRA to denote they are an "holder" notes and work will be performed in tasks.

* ~~Ideas~~ Epic for projects that require further analysis
* Deprioritized projects and tasks
* Long term goals

### Archive

Filenames for meetings are prefixed with meeting for easy understanding and can be created as a task in case some preparation notes are required.

* Finished projects
* Finalized analysis
* Past meetings
* Resources
* Diagrams
* Pictures
* PDFs

## Status

Headers used to filter through kanban board, table or dataview

### Idea

* Raw topic
* Requires analysis
* Topic or task with stoped progress
* Deprioritized tasks

### Todo

* To work in the immediate future
* Short term task to start
* Task reprioritized but still relevant

### In progress

* On going tasks

### Done

* Finished tasks
* Task waiting for result review

### Archive
* Finished tasks
* Finished projects
* Assets to store
* Past meetings
* Diagrams
* Notes and todo lists from finished goals

## Tags

Tags used to specify note type

- `#task` are small notes that will be used to perform atomic actions of related topics
- `#epic` is an all encompassing note that in general should have multiple independent tasks or to hold ideas that are not started yet. Filename is also prefixed with epic to better reflect that intent.
- `#meetingnotes` are notes from meetings or meeting preparation. Filename should be prefixed with `meeting` for easy finding.
- `#archive` represents notes that are done and for which no more additions are expected

## Priority

0 - archived
1 - idea, no priority
2 - incomplete, requires some more work before moving to a different state
3 - important
4 - urgent
5 - urgent and important
