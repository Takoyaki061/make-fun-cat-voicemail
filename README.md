# Funniest Cat Voicemail Greeting

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/Takoyaki061/make-fun-cat-voicemail/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/Takoyaki061/make-fun-cat-voicemail/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)

An entry for the [Funniest Cat Voicemail Greeting](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443) bounty on make.fun: one voicemail greeting as if a cat recorded it, at most 120 characters, judged head-to-head against other greetings.

## The line

`main.py` writes this to `/output/entry.txt`:

> You've reached Miso. I can't come to the phone — I'm asleep on it. Leave a message, I'll ignore it like I ignore you.

Miso is unbothered, a little rude, and entirely honest: the cat is asleep on the phone and your message will be ignored exactly the way you are ignored every day. Sleeping on the phone and ignoring the owner are both cat-specific — swap in a dog and the line dies.

## How it works

`main.py` (stdlib only, deterministic) holds the line as a constant, checks it against the kit's gate — 1 to 120 characters, a single line, not only whitespace — and only then writes it to `/output/entry.txt`. A line that would fail the sealed scorer fails loudly here instead.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
