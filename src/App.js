import IncomingReviews from './IncomingReviews';
import React, { Component } from 'react';

const makeReview = (name, text) => ({ name, text });

const incomingReviews = [
  makeReview('George Daole-Wellman', 'Nailed it!'),
  makeReview('Rushil', 'Slayed!')
];

class App extends Component {
  render() {
    return (
      <div>
        <IncomingReviews reviews={incomingReviews} />
      </div>
    );
  }
}

export default App;
