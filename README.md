# StreamB

Python implementation of StreamB using python ROS library.

Further reading:

Angelo Ferrando, Fabio Papacchini:
StreamB: A Declarative Language for Automatically Processing Data Streams in Abstract Environments for Agent Platforms. EMAS@AAMAS 2021: 114-136


What to install:
- ROS http://wiki.ros.org/it/ROS/Installation (with python)

How to use:

```bash
$ python3 stream.py <specification_file>
```
Where <specification_file> is the path to the specification file where the beliefs are defined using StreamB syntax.

The execution will generate a folder containing all ROS-node transducers. Among these nodes, a launch file will be created for a simplified use.

To create Parser:

```bash
$ antlr4 -Dlanguage=Python3 -visitor -no-listener Stream.g4
```

# Credits

To https://github.com/doganulus/python-monitors for the MTL Parser.
