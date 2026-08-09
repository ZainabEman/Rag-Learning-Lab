# _templates

Templates used to keep every topic folder identical, so a new topic can be
added at any time without restructuring anything.

- [topic-template/](topic-template/) - the five files every topic folder has.
- [new_topic.py](new_topic.py) - copies the template into a section.

## Usage

```bash
python _templates/new_topic.py 07-advanced-retrieval 13-splade "SPLADE"
```

The script refuses to overwrite an existing folder.
