import IncomingReviews from './IncomingReviews';
import React, { Component } from 'react';

class App extends Component {
  handleAddCuratedReview = (review) => {

  };

  render() {
    return (
      <div>
        <IncomingReviews
          onAddCuratedReview={this.handleAddCuratedReview}
        />
      </div>
    );
  }
}

export default App;
