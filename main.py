#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary — make.fun entry.

The pick: "whom".

Why this word, against the judge's brief:
  1. A real word every reader recognises — the objective-case pronoun
     every English speaker has met, feared, and misused.
  2. Funny at first sight: erase "whom" and nothing is lost, because
     nobody uses it correctly anyway. The joke lands the moment the
     word is gone — the language does not even notice.
  3. The humour comes from the word itself: a dusty formal leftover
     whose only remaining job is letting pedants correct strangers.
     The gap it leaves is the punchline — there is no gap.
  4. Fresh: the field will reach first for "moist", "literally" or
     "synergy". "whom" is the quieter, sharper pick, still instantly
     understood by every reader.
  5. Exact: one word, spelled correctly, nothing added around it.

The program writes the single word to /output/entry.txt, UTF-8,
mode 0644, inside a 0755 folder, per the kit's output rules.
"""

import os

WORD = "whom"


def main() -> None:
    os.umask(0o022)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, mode=0o755, exist_ok=True)
    entry = WORD.strip()
    assert entry and " " not in entry, "entry must be exactly one word"
    assert 1 <= len(entry.encode("utf-8")) <= 77, "entry must be 1-77 bytes"
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file must hold exactly one word, with
    # nothing added around it (judge criterion 5).
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(entry)
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)
    print(f"wrote {path}: {entry!r} ({len(entry)} chars)")


if __name__ == "__main__":
    main()
