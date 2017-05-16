jsx-lexer
=========

.. image:: https://travis-ci.org/fcurella/jsx-lexer.svg?branch=master
    :target: https://travis-ci.org/fcurella/jsx-lexer

.. image:: https://coveralls.io/repos/github/fcurella/jsx-lexer/badge.svg?branch=master
    :target: https://coveralls.io/github/fcurella/jsx-lexer?branch=master

A JSX lexer for Pygments

Installation
------------
.. code-block:: sh

    $ pip install jsx-lexer

Usage with Sphinx
-----------------

To use within Sphinx, simply specify ``jsx`` for your ``code-block``::

    .. code-block:: jsx

        const BlogTitle = ({ children }) => (
          <h3>{children}</h3>
        );
        // class component
        class BlogPost extends React.Component {
          renderTitle(title) {
            return <BlogTitle>{title}</BlogTitle>
          };
          render() {
            return (
            <div className="blog-body">
              {this.renderTitle(this.props.title)}
              <p>{this.props.body}</p>
            </div>
            );
          }
        }

Usage with mkdocs
-----------------

First, you need to create the ``CSS`` for the highlighting:

.. code-block:: bash

  $ pygmentize -S default -f html -a .codehilite > code/pygments.css

Then, add the following to your ``mkdocs.yml``:

.. code-block:: yaml

  markdown_extensions:
    - codehilite
  extra_css: [pygments.css]

Now, you can use ``jsx`` in your code blocks::

    ```jsx
    const BlogTitle = ({ children }) => (
      <h3>{children}</h3>
    );
    // class component
    class BlogPost extends React.Component {
      renderTitle(title) {
        return <BlogTitle>{title}</BlogTitle>
      };
      render() {
        return (
        <div className="blog-body">
          {this.renderTitle(this.props.title)}
          <p>{this.props.body}</p>
        </div>
        );
      }
    }
    ```
