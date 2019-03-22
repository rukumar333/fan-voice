import axios from 'axios';
import CurateDialog from './CurateDialog';
import IncomingReviewRow from './IncomingReviewRow';
import React, { Component } from 'react';
import { Table, TableBody, TableCell, TableHead, TableRow } from '@material-ui/core';

export default class IncomingReviews extends Component {
  state = {
    loading: false,
    reviews: [],
    selectedReview: null,
    total: 0
  };

  componentDidMount() {
    this.loadReviews();
  }

  async loadReviews() {
    this.setState({ loading: true });
    const { data } = await axios.get('/api/external-reviews');
    this.setState({
      loading: false,
      reviews: data.reviews,
      selectedReview: null,
      total: data.total
    });
  }

  handleDialogClose = () => {
    this.setState({
      selectedReview: null
    });
  };

  handleDialogSubmit = (review) => {
    this.handleDialogClose();
    this.props.onAddCuratedReview(review);
  };

  handleSelectReview = (review) => {
    this.setState({ selectedReview: review });
  };

  render() {
    const { selectedReview } = this.state;
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
              review => <IncomingReviewRow onSelect={this.handleSelectReview} review={review} />
            )}
          </TableBody>
        </Table>
      { selectedReview && <CurateDialog onClose={this.handleDialogClose} onSubmit={this.handleDialogSubmit} isOpen={!!selectedReview} review={selectedReview} />}
      </div>
    );
  }
}
