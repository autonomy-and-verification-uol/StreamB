# Stream Processing RV

Small Python implementation to create runtime monitors to achieve Stream Processing of MTL properties.

How to use:

```bash
$ python3
$ import stream
$ stream.parse('<your_property>')
$ stream.parseFile('<path_to_your_file>')
```

To create Parser:

```bash
$ antlr4 -Dlanguage=Python3 -visitor -no-listener Stream.g4
```

# Credits

To https://github.com/doganulus/python-monitors for the MTL Parser.
