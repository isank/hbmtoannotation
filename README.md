# hbmtoannotation

A Python based utility to convert your hbm (hibernate mapping xml) files to annotated Java entities.

## Usage

```python
python main.py
```

This will generate a Java file in the same path as your hbm file

## Limitations

The utility does not convert bidirectional mappings (eg. one to many) and result set mappings as of now.
