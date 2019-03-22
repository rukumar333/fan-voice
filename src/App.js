import axios from 'axios';
import IncomingReviews from './IncomingReviews';
import React, { Component } from 'react';

class App extends Component {
  handleAddCuratedReview = (review) => {
    axios.post(`/api/curated-reviews/${review.id}`, {
      gender: 'woman',
      name: review.name,
      quote: review.quote
    });
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
