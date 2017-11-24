# Game of life [![CircleCI][circlesvg]][circleurl]
## Getting started
This game was created in 45mins as part of one
of the sessions of the GCR to learn Python.

The goal was try to achieve [Game of life][wikipedia] 
### Prerequisites
You'll need docker or python2.7 if you are using different version you might find issues

## Running the tests
You need to run this to install the tests frameworks:
```bash
pip install -r requirements.txt
```
For execute the unit test:
```bash
python -m pytest --cov=life
```
For execute the behaviour test:
```bash
behave
```

## Status
Abandoned

[circlesvg]: https://circleci.com/gh/Saphyel/life/tree/master.svg?style=svg
[circleurl]: https://circleci.com/gh/Saphyel/life/tree/master
[wikipedia]: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
