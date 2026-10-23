from __future__ import annotations

import argparse
from pathlib import Path

from event_engine import EventEngine, SPECIAL_LABELS


BASE_DIR = Path(__file__).resolve().parent
RAW_FILE = BASE_DIR / "raw.txt"
RESOLVED_FILE = BASE_DIR / "resolved.txt"


def save(engine: EventEngine) -> None:
    """Olay günlüğünü ve çözümlenmiş metni UTF-8 olarak kaydet."""
    RAW_FILE.write_text(engine.raw_text, encoding="utf-8")
    RESOLVED_FILE.write_text(engine.text, encoding="utf-8")


def show(engine: EventEngine) -> None:
    print(f"Ham:         {engine.raw_text!r}")
    print(f"Çözümlenmiş: {engine.text!r}")


def apply_event(engine: EventEngine, event: str) -> None:
    """Komut satırından gelen tek bir metin veya özel tuş olayını uygula."""
    key_name = event.upper()
    if key_name in SPECIAL_LABELS:
        engine.key(key_name)
    else:
        engine.insert(event)


def interactive(engine: EventEngine) -> None:
    print("Yerel Klavye Olay Laboratuvarı (GUI yok)")
    print("Metin girin; özel tuşlar için :BACKSPACE, :LEFT gibi bir komut kullanın.")
    print(":paste METİN, :clear, :show ve :quit komutları da kullanılabilir.")

    while True:
        try:
            value = input("> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break

        command, separator, argument = value.partition(" ")
        lowered = command.lower()
        if lowered in {":quit", ":q"}:
            break
        if lowered == ":clear":
            engine.clear()
        elif lowered == ":show":
            show(engine)
            continue
        elif lowered == ":paste":
            engine.paste(argument if separator else "")
        elif value.startswith(":"):
            key_name = value[1:].upper()
            if key_name not in SPECIAL_LABELS:
                print(f"Bilinmeyen komut: {value}")
                continue
            engine.key(key_name)
        else:
            engine.insert(value)

        save(engine)
        show(engine)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Metin ve klavye olaylarını raw.txt ile resolved.txt dosyalarına yaz."
    )
    parser.add_argument(
        "events",
        nargs="*",
        metavar="OLAY",
        help="Metin veya BACKSPACE, DELETE, ENTER, TAB, LEFT, RIGHT, HOME, END",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    engine = EventEngine()
    if not args.events:
        interactive(engine)
        save(engine)
        return

    for event in args.events:
        apply_event(engine, event)
    save(engine)
    show(engine)


if __name__ == "__main__":
    main()
