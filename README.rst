jsx-lexer
=========

A JSX lexer for Pygments

Installation
------------
.. code-block:: sh

    $ pip install jsx-lexer

Usage
-----

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
