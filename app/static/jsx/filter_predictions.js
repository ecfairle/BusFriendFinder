var DynamicSearch = React.createClass({

  // sets initial state
  getInitialState: function(){
    return { searchString: '' };
  },

  handleChange: function(event){
    this.setState({searchString:event.target.value});
  },

  render: function() {

    var stops = this.props.items;
    var searchString = this.state.searchString.trim().toLowerCase();

      if(searchString.length > 0){
        stops = stops.filter(function(stop){
          return stop.route.toLowerCase().match( searchString );
        });
      }

    return (
      <div>
        <input type="text" value={this.state.searchString} onChange={this.handleChange} placeholder="filter by route" />
        <ul>
          { stops.slice(0,10).map(function(stop){ return <Prediction stop={stop}/> }) }
        </ul>
      </div>
    )
  }

});

var Prediction = React.createClass({
  render: function() {
    var stop = this.props.stop
    return (
      <div>{stop.route}</div>
    );
  }
});


stops = stops.map(JSON.parse)

ReactDOM.render(
  <DynamicSearch items={ stops } />,
  document.getElementById('stop_list')
);