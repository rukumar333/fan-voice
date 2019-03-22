import axios from 'axios';
import CuratedReviewRow from './CuratedReviewRow';
import React, { Component } from 'react';
import { Table, TableBody, TableCell, TableHead, TableRow } from '@material-ui/core';

export default class CuratedReviews extends Component {
  state = {
    loading: false,
    reviews: [],

    total: 0
  };

  componentDidMount() {
    this.loadReviews();
  }

  async loadReviews() {
    this.setState({ loading: true });
    const { data } = await axios.get('/api/curated-reviews');
    this.setState({
      loading: false,
      reviews: data.reviews,
      total: data.total
    });
  }

  render() {
    return (
      <div>
        <Table>
          <TableHead>
            <TableRow>
            <TableCell>Name</TableCell>
            <TableCell>Review Content</TableCell>
            <TableCell></TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {this.state.reviews.map(
              review => <CuratedReviewRow key={review.id} review={review} />
            )}
          </TableBody>
        </Table>
      </div>
    );
  }
}
