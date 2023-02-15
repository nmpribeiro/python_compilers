# Cross platform Python UI

## Install

SDL:

```bash
conda create --name pythonUI python=3.10
conda activate pythonUI

pip install castella[sdl]
```

Check [castella getting started](https://i2y.github.io/castella/getting-started/) to see how to install for GLFW.

## How to

### Web

 `python -m http.server 3000`

Browse to [localhost:3000/counter.html](http://localhost:3000/counter.html) (you can check file counter.html)

### Native

 `python main.py`

## Resources

* [Let's build a Compiler, by Jack Crenshaw](https://compilers.iecc.com/crenshaw/)
* [Let's build an interpreter in python from scratch](https://python.plainenglish.io/lets-build-an-interpreter-in-python-from-scratch-833e9929bbb8)
