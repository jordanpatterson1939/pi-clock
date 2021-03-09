# pi-clock
Set alarms, create timers or stopwatches right from your terminal.

![Piclock Demo](demo/demo.gif)

## Installation
```bash
pip3 install pi-clock
```

## Usage
**Setting an alarm**
```bash
 piclock -a
```

**Creating a timer**
```bash
piclock -t
```

**Creating a new stopwatch**
```bash
piclock -s
```

**Interactive mode**
```bash
 piclock -i
```

**Command Line Arguments**
```text
usage: piclock [-h] [-i] [-t] [-a] [-s]

optional arguments:
-h, --help          shows this help message and exit
-i, --interactive   Interactive mode
-t, --timer         Set a new timer
-a, --alarm         Set a new alarm
-s. --stopwatch     Start a new stopwatch
```

Todo:
- [ ] Allow alarms to run in the background while in intercative mode.
