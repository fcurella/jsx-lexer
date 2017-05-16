import re

from pygments.lexer import bygroups, include
from pygments.lexers.javascript import JavascriptLexer
from pygments.token import Name, Operator, Punctuation, String, Text


# Use same tokens as `JavascriptLexer`, but with tags and attributes support
TOKENS = JavascriptLexer.tokens
TOKENS.update({
    'jsx': [
        (r'(<)(\s*)([\w]+)',
         bygroups(Punctuation, Text, Name.Tag), 'tag'),
        (r'(<)(\s*)(/)(\s*)([\w]+)(\s*)(>)',
         bygroups(Punctuation, Text, Punctuation, Text, Name.Tag, Text,
                  Punctuation)),
    ],
    'tag': [
        (r'\s+', Text),
        (r'([\w]+\s*)(=)(\s*)', bygroups(Name.Attribute, Operator, Text),
         'attr'),
        (r'[{}]+', Punctuation),
        (r'[\w\.]+', Name.Attribute),
        (r'(/?)(\s*)(>)', bygroups(Punctuation, Text, Punctuation), '#pop'),
    ],
    'attr': [
        ('\s+', Text),
        ('".*?"', String, '#pop'),
        ("'.*?'", String, '#pop'),
        (r'[^\s>]+', String, '#pop'),
    ],
})
TOKENS['root'].insert(0, include('jsx'))


class JsxLexer(JavascriptLexer):
    name = 'react'
    aliases = ['jsx', 'react']
    filenames = ['*.jsx', '*.react']
    mimetypes = ['text/jsx', 'text/typescript-jsx']

    flags = re.MULTILINE | re.DOTALL | re.UNICODE

    tokens = TOKENS
