import axios from 'axios';
import CuratedReviews from './CuratedReviews';
import IncomingReviews from './IncomingReviews';
import React, { Component } from 'react';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import './App.css';

class App extends Component {
  state = {
    view: 'external'
  };

  handleAddCuratedReview = (review) => {
    axios.post(`/api/curated-reviews/${review.id}`, {
      gender: review.gender,
      name: review.name,
      quote: review.quote
    });
  };

  handleViewChange = (event, view) => {
    this.setState({ view });
  };

  render() {
    return (
      <div>
        <AppBar position="static">
        <Tabs value={this.state.view} onChange={this.handleViewChange}>
          <Tab label="External Reviews" value="external" />
          <Tab label="Curated Reviews" value="curated" />
        </Tabs>
      </AppBar>
        {this.state.view === 'external' ?
        <IncomingReviews
          onAddCuratedReview={this.handleAddCuratedReview}
        /> : <CuratedReviews />
      }
      </div>
    );
  }
}

export default App;
