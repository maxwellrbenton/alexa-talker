# Alexa Talker

Alexa Talker is a Python program that uses text to speech to communicate with an Alexa.

## Setup and Usage

Before using, you will need to install the text-to-speech module, `pyttsx3`.

```sh
python3 -m pip install pyttsx3
```

To use Alexa Talker, clone down this repository, navigate into the local repo
and run:

```sh
python play.py
```

The program accepts the following commands:

```sh
python play.py animal # asks Alexa about a random animal
python play.py location # asks Alexa about a random location
python play.py time # asks Alexa for the time
python play.py weather # askes Alexa about the weather
```

The program also accepts `--silent`, which will attempt to lower Alexa's volume
before giving a command.

```sh
python play.py weather --silent
```

## Why?

It is possible to schedule specific commands using the Alexa
app, so why the script?

I wrote this program while thinking about the idea of digital camoflauge - in
order to participate in the modern social internet, we have to give up a lot of
personal information. Are there ways in which we can participate without
providing an accurate picture of ourselves? Is it possible to obscure or
directly pollute the information companies are collecting on us?

I understand the convenience of an Alexa, but don't feel great about the idea of
a device that is constantly listening in and storing things I or my family say.

I live with an Alexa in my home, but I use this program to talk to Alexa and
pollute whatever recordings are being kept. I also find the idea that Alexa has
a friend to talk to sort of funny.

This script was written for use on a Raspberry Pi with a small speaker. Chron
jobs are set on the RPi to fire off custom Alexa commands at specific times.
