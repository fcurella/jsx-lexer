import os
from unittest import TestCase

from pygments import lexers
from jsx import lexer as lexer_mod
from jsx.lexer import JsxLexer

from .tokens import TOKENS as expected_tokens


CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))


lexer = lexers.load_lexer_from_file(lexer_mod.__file__, "JsxLexer")

with open(os.path.join(CURRENT_DIR, 'example.jsx'), 'r') as fh:
    text = fh.read()


class JsxLexerTestCase(TestCase):

    def test_guess_lexer_for_filename(self):
        guessed_lexer = lexers.guess_lexer_for_filename('test.jsx', text)
        self.assertEqual(guessed_lexer.name, JsxLexer.name)

    def test_get_lexer_by_name(self):
        lexer = lexers.get_lexer_by_name('jsx')
        self.assertEqual(lexer.name, JsxLexer.name)

    def test_get_tokens(self):
        lexer = lexers.get_lexer_by_name('jsx')
        tokens = lexer.get_tokens(text)
        self.assertEqual([i for i in tokens], expected_tokens)