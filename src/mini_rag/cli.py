from mini_rag.rag import build_rag


def main() -> None:
    rag = build_rag()

    while True:
        try:
            question = input("Ask: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if question.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not question:
            continue

        print(f"\n{rag.ask(question)}\n")


if __name__ == "__main__":
    main()
