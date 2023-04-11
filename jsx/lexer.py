import re

from pygments.lexer import bygroups, default, include
from pygments.lexers.javascript import JavascriptLexer, TypeScriptLexer
from pygments.token import Name, Operator, Punctuation, String, Text

# Add tags and attributes support to existing tokens


def build_react_tokens(tokens):
    tokens.update(
        {
            "jsx": [
                (
                    r"(<)(/?)(>)",
                    bygroups(Punctuation, Punctuation, Punctuation),
                ),  # JSXFragment <>|</>
                (r"(<)([\w]+)(\.?)", bygroups(Punctuation,
                                              Name.Tag, Punctuation), "tag"),
                (
                    r"(<)(/)([\w]+)(>)",
                    bygroups(Punctuation, Punctuation, Name.Tag, Punctuation),
                ),
                (
                    r"(<)(/)([\w]+)",
                    bygroups(Punctuation, Punctuation, Name.Tag),
                    "fragment",
                ),  # Same for React.Context
            ],
            "tag": [
                (r"\s+", Text),
                (r"([\w-]+\s*)(=)(\s*)",
                 bygroups(Name.Attribute, Operator, Text), "attr"),
                (r"[{}]+", Punctuation),
                (r"[\w\.]+", Name.Attribute),
                (r"(/?)(\s*)(>)", bygroups(Punctuation, Text, Punctuation), "#pop"),
            ],
            "fragment": [
                (r"(.)([\w]+)", bygroups(Punctuation, Name.Attribute)),
                (r"(>)", bygroups(Punctuation), "#pop"),
            ],
            "attr": [
                ("{", Punctuation, "expression"),
                ('".*?"', String, "#pop"),
                ("'.*?'", String, "#pop"),
                default("#pop"),
            ],
            "expression": [
                ("{", Punctuation, "#push"),
                ("}", Punctuation, "#pop"),
                include("root"),
            ],
        }
    )
    tokens["root"].insert(0, include("jsx"))
    return tokens


JSX_TOKENS = build_react_tokens(JavascriptLexer.tokens)
TSX_TOKENS = build_react_tokens(TypeScriptLexer.tokens)


class JsxLexer(JavascriptLexer):
    name = "react"
    aliases = ["jsx", "react"]
    filenames = ["*.jsx", "*.react"]
    mimetypes = ["text/jsx"]

    flags = re.MULTILINE | re.DOTALL | re.UNICODE

    tokens = JSX_TOKENS


class TsxLexer(TypeScriptLexer):
    name = "react-typescript"
    aliases = ["tsx", "react-typescript"]
    filenames = ["*.tsx"]
    mimetypes = ["text/tsx", "text/typescript-jsx"]
    mimetypes = ["text/jsx"]

    flags = re.MULTILINE | re.DOTALL | re.UNICODE

    tokens = JSX_TOKENS


class TsxLexer(TypeScriptLexer):
    name = "react-typescript"
    aliases = ["tsx", "react-typescript"]
    filenames = ["*.tsx"]
    mimetypes = ["text/tsx", "text/typescript-jsx"]

    flags = re.MULTILINE | re.DOTALL | re.UNICODE

    tokens = TSX_TOKENS
