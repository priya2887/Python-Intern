def clean_names(raw_names: list[str | None]) -> list[str]:
    cleaned: list[str] = []
    seen: set[str] = set()
    for item in raw_names:
        if item is None:
            continue
        name = item.strip()
        if not name:
            continue
        if name not in seen:
            seen.add(name)
            cleaned.append(name)
    return cleaned


def main() -> None:
    raw = [" Ava ", "Liam", "", None, "Noah", "Ava", "Mia ", "  ", "Noah"]
    cleaned = clean_names(raw)
    print("Cleaned names:", cleaned)


if __name__ == "__main__":
    main()
