var DynamicSearch = React.createClass({

  // sets initial state
  getInitialState: function(){
    return { searchString: '' };
  },

  handleChange: function(event){
    this.setState({searchString: event.target.value,
                   loading: true
                  });
  },

  resetSearch: function() {
    this.setState({searchString: ''});
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
      <div className="grid">
          <form action="#">
            <div className="mdl-textfield mdl-js-textfield mdl-textfield--floating-label">
              <input className="mdl-textfield__input" onBlur={this.resetSearch} type="text" id="sample3" value={this.state.searchString} onChange={this.handleChange}/>
              <label className="mdl-textfield__label" for="sample3">Filter by Route</label>
            </div>
          </form>
        <div className="row">
          <ul className="demo-list-two mdl-list">
                { stops.slice(0,20).map(function(stop){ return <Prediction stop={stop}/> }) }
          </ul>
        </div>
      </div>
    )
  }

});


var Prediction = React.createClass({
  render: function() {
    var stop = this.props.stop;
    predictions = setPredictions(stop.predictions);

    return (
      <li className="mdl-list__item mdl-list__item--three-line">
        <span className="mdl-list__item-primary-content">
        <i className="material-icons md-36 md-light mdl-list__item-avatar">directions_bus</i>
          <span>
            Route: {stop.route} -- {predictions.join(', ')}
          </span>
          <span className="mdl-list__item-text-body">
            {stop.direction} at {stop.title}
          </span>
        </span>
      </li>
    );
  }
});


function setPredictions(prediction_list){
  predictions = []
  for(i = 0; i < prediction_list.length; i++){
    if(prediction_list[i] == 0){
      predictions.push('Arriving')
    }
    else{
      predictions.push(String(prediction_list[i]) + ' min')
    }
  }

  return predictions
}


function filterStops (stops) {
  stops = stops.map(JSON.parse)
  ReactDOM.render(
    <DynamicSearch items={ stops } />,
    document.getElementById('stop_list')
  );
}
