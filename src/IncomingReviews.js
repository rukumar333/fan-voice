import CurateDialog from './CurateDialog';
import IncomingReviewRow from './IncomingReviewRow';
import React, { Component } from 'react';
import { Table, TableBody, TableCell, TableHead, TableRow } from '@material-ui/core';

export default class IncomingReviews extends Component {
  state = {
    selectedReview: null
  };

  handleDialogClose = () => {
    this.setState({
      selectedReview: null
    });
  };

  handleDialogSubmit = () => {
    this.handleDialogClose();
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
            {this.props.reviews.map(
              review => <IncomingReviewRow onSelect={this.handleSelectReview} review={review} />
            )}
          </TableBody>
        </Table>
      { selectedReview && <CurateDialog onClose={this.handleDialogClose} onSubmit={this.handleDialogSubmit} isOpen={!!selectedReview} review={selectedReview} />}
      </div>
    );
  }
}
