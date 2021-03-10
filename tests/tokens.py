from pygments.token import Token


TOKENS = [
    (Token.Keyword.Declaration, "const"),
    (Token.Text, " "),
    (Token.Name.Other, "isOldEnough"),
    (Token.Text, " "),
    (Token.Operator, "="),
    (Token.Text, " "),
    (Token.Punctuation, "("),
    (Token.Name.Other, "value"),
    (Token.Punctuation, ","),
    (Token.Text, " "),
    (Token.Name.Other, "ownProps"),
    (Token.Punctuation, ")"),
    (Token.Text, " "),
    (Token.Punctuation, "=>"),
    (Token.Text, " "),
    (Token.Punctuation, "{"),
    (Token.Text, "\n    "),
    (Token.Keyword, "if"),
    (Token.Text, " "),
    (Token.Punctuation, "("),
    (Token.Name.Builtin, "parseInt"),
    (Token.Punctuation, "("),
    (Token.Name.Other, "value"),
    (Token.Punctuation, ","),
    (Token.Text, " "),
    (Token.Literal.Number.Float, "10"),
    (Token.Punctuation, ")"),
    (Token.Text, " "),
    (Token.Operator, "<"),
    (Token.Text, " "),
    (Token.Literal.Number.Float, "14"),
    (Token.Punctuation, ")"),
    (Token.Text, " "),
    (Token.Punctuation, "{"),
    (Token.Text, "\n        "),
    (Token.Keyword, "return"),
    (Token.Text, " "),
    (Token.Literal.String.Double, '"Only 14yo and older can register to the site."'),
    (Token.Text, "\n    "),
    (Token.Punctuation, "}"),
    (Token.Text, "\n"),
    (Token.Punctuation, "}"),
    (Token.Punctuation, ";"),
    (Token.Text, "\n\n"),
    (Token.Comment.Single, "// functional component\n"),
    (Token.Keyword.Declaration, "const"),
    (Token.Text, " "),
    (Token.Name.Other, "BlogTitle"),
    (Token.Text, " "),
    (Token.Operator, "="),
    (Token.Text, " "),
    (Token.Punctuation, "("),
    (Token.Punctuation, "{"),
    (Token.Text, " "),
    (Token.Name.Other, "children"),
    (Token.Text, " "),
    (Token.Punctuation, "}"),
    (Token.Punctuation, ")"),
    (Token.Text, " "),
    (Token.Punctuation, "=>"),
    (Token.Text, " "),
    (Token.Punctuation, "("),
    (Token.Text, "\n  "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "h3"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, "{"),
    (Token.Name.Other, "children"),
    (Token.Punctuation, "}"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "h3"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n"),
    (Token.Punctuation, ")"),
    (Token.Punctuation, ";"),
    (Token.Text, "\n\n"),
    (Token.Comment.Single, "// class component\n"),
    (Token.Keyword.Declaration, "class"),
    (Token.Text, " "),
    (Token.Name.Other, "BlogPost"),
    (Token.Text, " "),
    (Token.Keyword, "extends"),
    (Token.Text, " "),
    (Token.Name.Other, "React"),
    (Token.Punctuation, "."),
    (Token.Name.Other, "Component"),
    (Token.Text, " "),
    (Token.Punctuation, "{"),
    (Token.Text, "\n  "),
    (Token.Name.Other, "renderTitle"),
    (Token.Punctuation, "("),
    (Token.Name.Other, "title"),
    (Token.Punctuation, ")"),
    (Token.Text, " "),
    (Token.Punctuation, "{"),
    (Token.Text, "\n    "),
    (Token.Keyword, "return"),
    (Token.Text, " "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "BlogTitle"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, "{"),
    (Token.Name.Other, "title"),
    (Token.Punctuation, "}"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "BlogTitle"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n  "),
    (Token.Punctuation, "}"),
    (Token.Punctuation, ";"),
    (Token.Text, "\n  "),
    (Token.Name.Other, "render"),
    (Token.Punctuation, "("),
    (Token.Punctuation, ")"),
    (Token.Text, " "),
    (Token.Punctuation, "{"),
    (Token.Text, "\n    "),
    (Token.Keyword, "return"),
    (Token.Text, " "),
    (Token.Punctuation, "("),
    (Token.Text, "\n    "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "div"),
    (Token.Text, " "),
    (Token.Name.Attribute, "className"),
    (Token.Operator, "="),
    (Token.Literal.String, '"blog-body"'),
    (Token.Punctuation, ">"),
    (Token.Text, "\n      "),
    (Token.Punctuation, "{"),
    (Token.Keyword, "this"),
    (Token.Punctuation, "."),
    (Token.Name.Other, "renderTitle"),
    (Token.Punctuation, "("),
    (Token.Keyword, "this"),
    (Token.Punctuation, "."),
    (Token.Name.Other, "props"),
    (Token.Punctuation, "."),
    (Token.Name.Other, "title"),
    (Token.Punctuation, ")"),
    (Token.Punctuation, "}"),
    (Token.Text, "\n      "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "p"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, "{"),
    (Token.Keyword, "this"),
    (Token.Punctuation, "."),
    (Token.Name.Other, "props"),
    (Token.Punctuation, "."),
    (Token.Name.Other, "body"),
    (Token.Punctuation, "}"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "p"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n      "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "CustomComponent"),
    (Token.Punctuation, ">"),
    (Token.Name.Other, "text"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "CustomComponent"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n      "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "input"),
    (Token.Text, " "),
    (Token.Name.Attribute, "type"),
    (Token.Operator, "="),
    (Token.Literal.String, '"text"'),
    (Token.Text, " "),
    (Token.Punctuation, "{"),
    (Token.Name.Attribute, "...props.inputProps"),
    (Token.Punctuation, "}"),
    (Token.Text, " "),
    (Token.Punctuation, "/"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n    "),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "div"),
    (Token.Punctuation, ">"),
    (Token.Text, "\n    "),
    (Token.Punctuation, ")"),
    (Token.Punctuation, ";"),
    (Token.Text, "\n  "),
    (Token.Punctuation, "}"),
    (Token.Text, "\n"),
    (Token.Punctuation, "}"),
    (Token.Text, "\n\n"),
    (Token.Keyword.Declaration, "const"),
    (Token.Text, " "),
    (Token.Name.Other, "body"),
    (Token.Text, " "),
    (Token.Operator, "="),
    (Token.Text, " "),
    (Token.Literal.String.Double, '"Hello World!"'),
    (Token.Punctuation, ";"),
    (Token.Text, "\n"),
    (Token.Keyword.Declaration, "const"),
    (Token.Text, " "),
    (Token.Name.Other, "blogNode"),
    (Token.Text, " "),
    (Token.Operator, "="),
    (Token.Text, " "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "BlogPost"),
    (Token.Text, " "),
    (Token.Name.Attribute, "title"),
    (Token.Operator, "="),
    (Token.Literal.String, '"What\'s going on?"'),
    (Token.Text, " "),
    (Token.Name.Attribute, "body"),
    (Token.Operator, "="),
    (Token.Punctuation, "{"),
    (Token.Name.Other, "body"),
    (Token.Punctuation, "}"),
    (Token.Text, " "),
    (Token.Punctuation, "/"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, ";"),
    (Token.Text, "\n"),
    (Token.Comment.Single, "// some comment. Tags shouldn't be lexed in here\n"),
    (Token.Comment.Single, '// <div class="blog-body">\n'),
    (Token.Comment.Single, "// <h3>What's going on?</h3>\n"),
    (Token.Comment.Single, "// <p>Hello World!</p>\n"),
    (Token.Comment.Single, "// </div>\n"),
    (Token.Text, "\n"),
    (
        Token.Comment.Multiline,
        "/*\n  Some comment. Tags shouldn't be lexed in here either\n  <div class=\"blog-body\">\n  <h3>What's going on?</h3>\n  <p>Hello World!</p>\n  </div>\n*/",
    ),
    (Token.Text, "\n\n"),
    (Token.Keyword.Declaration, "const"),
    (Token.Text, " "),
    (Token.Name.Other, "shortSyntaxfragmentEmptyBody"),
    (Token.Text, " "),
    (Token.Operator, "="),
    (Token.Text, " "),
    (Token.Punctuation, "<"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, ";"),
    (Token.Text, "\n\n"),
    (Token.Keyword.Declaration, "const"),
    (Token.Text, " "),
    (Token.Name.Other, "shortSyntaxfragmentFullBody"),
    (Token.Text, " "),
    (Token.Operator, "="),
    (Token.Text, " "),
    (Token.Punctuation, "<"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "div"),
    (Token.Punctuation, "/"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, ";"),
    (Token.Text, "\n\n"),
    (Token.Keyword.Declaration, "const"),
    (Token.Text, " "),
    (Token.Name.Other, "reactDotFragment"),
    (Token.Text, " "),
    (Token.Operator, "="),
    (Token.Text, " "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "React"),
    (Token.Punctuation, "."),
    (Token.Name.Attribute, "Fragment"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "div"),
    (Token.Punctuation, "/"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "React"),
    (Token.Punctuation, "."),
    (Token.Name.Attribute, "Fragment"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, ";"),
    (Token.Text, "\n\n"),
    (Token.Keyword.Declaration, "const"),
    (Token.Text, " "),
    (Token.Name.Other, "reactDotContext"),
    (Token.Text, " "),
    (Token.Operator, "="),
    (Token.Text, " "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "Context"),
    (Token.Punctuation, "."),
    (Token.Name.Attribute, "Provider"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "div"),
    (Token.Punctuation, "/"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "Context"),
    (Token.Punctuation, "."),
    (Token.Name.Attribute, "Provider"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, ";"),
    (Token.Text, "\n\n"),
    (Token.Keyword.Declaration, "const"),
    (Token.Text, " "),
    (Token.Name.Other, "reactDotContextValue"),
    (Token.Text, " "),
    (Token.Operator, "="),
    (Token.Text, " "),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "Context"),
    (Token.Punctuation, "."),
    (Token.Name.Attribute, "Provider"),
    (Token.Text, " "),
    (Token.Name.Attribute, "value"),
    (Token.Operator, "="),
    (Token.Literal.String, '"Hello"'),
    (Token.Punctuation, ">"),
    (Token.Punctuation, "<"),
    (Token.Name.Tag, "div"),
    (Token.Punctuation, "/"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, "<"),
    (Token.Punctuation, "/"),
    (Token.Name.Tag, "Context"),
    (Token.Punctuation, "."),
    (Token.Name.Attribute, "Provider"),
    (Token.Punctuation, ">"),
    (Token.Punctuation, ";"),
    (Token.Text, "\n"),
]
