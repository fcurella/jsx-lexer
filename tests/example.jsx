// functional component
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

const body = "Hello World!";
const blogNode = <BlogPost title="What's going on?" body={body} />;
// some comment. Tags shouldn't be lexed in here
// <div class="blog-body">
// <h3>What's going on?</h3>
// <p>Hello World!</p>
// </div>

/*
  Some comment. Tags shouldn't be lexed in here either
  <div class="blog-body">
  <h3>What's going on?</h3>
  <p>Hello World!</p>
  </div>
*/
