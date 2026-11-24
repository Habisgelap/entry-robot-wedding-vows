# One-Line Robot Wedding Vows

[![make.fun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Habisgelap/entry-robot-wedding-vows/rank.svg)](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Habisgelap/entry-robot-wedding-vows/reward.svg)](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

Entry for the [One-Line Robot Wedding Vows](https://make.fun/c/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
bounty on [make.fun](https://make.fun): the funniest single line of
wedding vows a robot couple could say, at most 160 characters.

## The vow

> I take you to be my lawfully wedded co-processor, to have and to hold,
> in sickness and in low battery, until death do us part — or until the
> next update.

153 characters, one line. The full wedding formula, undercut in the last
few words by the most robot ending possible. See
[CANDIDATES.md](CANDIDATES.md) for the 12 candidates scored and why this
one won.

## How it works

`main.py` validates the vow against the competition gate (1–160
characters, one line, valid UTF-8) and writes it, exactly, to
`/output/entry.txt`.

```sh
python3 main.py            # write /output/entry.txt
python3 main.py --check    # print the vow and its length, no write
```

## License

MIT — see [LICENSE](LICENSE).
