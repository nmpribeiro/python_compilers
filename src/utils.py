from src.lexer.JsxLexer import JsxLexer


def repl():
    i = 0
    while True:
        try:
            data: str = input(f"[{i}]: ")
            for tok in JsxLexer().get_tokens(data):
                # if tok.name == EOF:
                #     break
                print(tok)
        except EOFError:           # handling ctrl + D
            print()
        except KeyboardInterrupt:  # handling ctrl + C
            print("bye")
            break
        finally:
            i += 1

    # data: str = input(f"[{i}]: ")


def read_file(file_name: str) -> None:
    with open(file_name) as f:
        data = f.read()
        for tok in JsxLexer().get_tokens(data):
            # if tok.name == EOF:
            #     break
            print(tok)

# def compiler():
#     print(file)
#     lexer = JsxLexer()
#     with open(file) as f:
#         src = f.read()
#         tokens = lexer.get_tokens(src)
#         # for ttype, value in tokens:
#         #     print(ttype, value)
#         for token in tokens:
#             print(token)
