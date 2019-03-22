import IncomingReviews from './IncomingReviews';
import React, { Component } from 'react';

const makeReview = (name, text) => ({ name, text });

const incomingReviews = [
  makeReview('George Daole-Wellman', 'Nailed it!'),
  makeReview('Rushil', 'Slayed!')
];

class App extends Component {
  handleAddCuratedReview = (review) => {

  };

  render() {
    return (
      <div>
        <IncomingReviews
          onAddCuratedReview={this.handleAddCuratedReview}
          reviews={incomingReviews}
        />
      </div>
    );
  }
}

export default App;
