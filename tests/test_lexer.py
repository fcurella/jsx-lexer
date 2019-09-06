import os
import re
from unittest import TestCase

from pygments import lexers
from pygments.token import Token
from jsx import lexer as lexer_mod
from jsx.lexer import JsxLexer

from .tokens import TOKENS as expected_tokens


CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))


lexer = lexers.load_lexer_from_file(lexer_mod.__file__, "JsxLexer")

with open(os.path.join(CURRENT_DIR, "example.jsx"), "r") as fh:
    text = fh.read()


class JsxLexerTestCase(TestCase):
    def __filter_tokens(self, tokens):
        space = re.compile("[ \n]+")
        return [i for i in tokens if not space.match(i[1]) and not i[1] == ""]

    def test_guess_lexer_for_filename(self):
        guessed_lexer = lexers.guess_lexer_for_filename("test.jsx", text)
        self.assertEqual(guessed_lexer.name, JsxLexer.name)

    def test_get_lexer_by_name(self):
        lexer = lexers.get_lexer_by_name("jsx")
        self.assertEqual(lexer.name, JsxLexer.name)

    def test_get_tokens(self):
        lexer = lexers.get_lexer_by_name("jsx")
        tokens = lexer.get_tokens(text)
        self.assertEqual([i for i in tokens], expected_tokens)

    def test_lexing_object_attribute(self):
        lexer = lexers.get_lexer_by_name("jsx")
        tokens = lexer.get_tokens(
            """
            <div style={{ color: 'red' }} />
        """
        )

        self.assertEqual(
            self.__filter_tokens(tokens),
            [
                (Token.Punctuation, "<"),
                (Token.Name.Tag, "div"),
                (Token.Name.Attribute, "style"),
                (Token.Operator, "="),
                (Token.Punctuation, "{"),
                (Token.Punctuation, "{"),
                (Token.Name.Other, "color"),
                (Token.Operator, ":"),
                (Token.Literal.String.Single, "'red'"),
                (Token.Punctuation, "}"),
                (Token.Punctuation, "}"),
                (Token.Punctuation, "/"),
                (Token.Punctuation, ">"),
            ],
        )

    def test_lexing_multiple_attributes(self):
        lexer = lexers.get_lexer_by_name("jsx")
        tokens = lexer.get_tokens(
            """
            <User name={'jhon'} last={'doe'} />
        """
        )

        self.assertEqual(
            self.__filter_tokens(tokens),
            [
                (Token.Punctuation, "<"),
                (Token.Name.Tag, "User"),
                (Token.Name.Attribute, "name"),
                (Token.Operator, "="),
                (Token.Punctuation, "{"),
                (Token.Literal.String.Single, "'jhon'"),
                (Token.Punctuation, "}"),
                (Token.Name.Attribute, "last"),
                (Token.Operator, "="),
                (Token.Punctuation, "{"),
                (Token.Literal.String.Single, "'doe'"),
                (Token.Punctuation, "}"),
                (Token.Punctuation, "/"),
                (Token.Punctuation, ">"),
            ],
        )

    def test_lexing_arrow_function_attribute(self):
        lexer = lexers.get_lexer_by_name("jsx")
        tokens = lexer.get_tokens(
            """
            <button onClick={e => e.preventDefault ()} />
        """
        )

        self.assertEqual(
            self.__filter_tokens(tokens),
            [
                (Token.Punctuation, "<"),
                (Token.Name.Tag, "button"),
                (Token.Name.Attribute, "onClick"),
                (Token.Operator, "="),
                (Token.Punctuation, "{"),
                (Token.Name.Other, "e"),
                (Token.Punctuation, "=>"),
                (Token.Name.Other, "e"),
                (Token.Punctuation, "."),
                (Token.Name.Other, "preventDefault"),
                (Token.Punctuation, "("),
                (Token.Punctuation, ")"),
                (Token.Punctuation, "}"),
                (Token.Punctuation, "/"),
                (Token.Punctuation, ">"),
            ],
        )

    def test_lexing_function_returing_jsx(self):
        lexer = lexers.get_lexer_by_name("jsx")
        tokens = lexer.get_tokens(
            """
            <Component wrapped={data => <User name={data.name} />} />
        """
        )

        self.assertEqual(
            self.__filter_tokens(tokens),
            [
                (Token.Punctuation, "<"),
                (Token.Name.Tag, "Component"),
                (Token.Name.Attribute, "wrapped"),
                (Token.Operator, "="),
                (Token.Punctuation, "{"),
                (Token.Name.Other, "data"),
                (Token.Punctuation, "=>"),
                (Token.Punctuation, "<"),
                (Token.Name.Tag, "User"),
                (Token.Name.Attribute, "name"),
                (Token.Operator, "="),
                (Token.Punctuation, "{"),
                (Token.Name.Other, "data"),
                (Token.Punctuation, "."),
                (Token.Name.Other, "name"),
                (Token.Punctuation, "}"),
                (Token.Punctuation, "/"),
                (Token.Punctuation, ">"),
                (Token.Punctuation, "}"),
                (Token.Punctuation, "/"),
                (Token.Punctuation, ">"),
            ],
        )

    def test_lexing_short_syntax_fragments(self):
        """
        Testing <></> React Short Syntax JSXFragment
        see: `https://facebook.github.io/jsx/`
        JSXFragment :
            <> JSXChildrenopt </>
        """
        lexer = lexers.get_lexer_by_name("jsx")
        tokens = lexer.get_tokens("""<></>""")
        self.assertEqual(
            self.__filter_tokens(tokens),
            [
                (Token.Punctuation, "<"),
                (Token.Punctuation, ">"),
                (Token.Punctuation, "<"),
                (Token.Punctuation, "/"),
                (Token.Punctuation, ">"),
            ],
        )

    def test_lexing_full_fragments(self):
        """
        Testing <React.Fragment></React.Fragment>
        """
        lexer = lexers.get_lexer_by_name("jsx")
        tokens = lexer.get_tokens("""<React.Fragment></React.Fragment>""")
        self.assertEqual(
            self.__filter_tokens(tokens),
            [
                (Token.Punctuation, "<"),
                (Token.Name.Tag, "React"),
                (Token.Punctuation, "."),
                (Token.Name.Attribute, "Fragment"),
                (Token.Punctuation, ">"),
                (Token.Punctuation, "<"),
                (Token.Punctuation, "/"),
                (Token.Name.Tag, "React"),
                (Token.Punctuation, "."),
                (Token.Name.Attribute, "Fragment"),
                (Token.Punctuation, ">"),
            ],
        )
