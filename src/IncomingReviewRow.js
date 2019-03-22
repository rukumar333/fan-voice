import React, { Component } from 'react';
import { Button, TableCell, TableRow } from '@material-ui/core';

export default class IncomingReviewRow extends Component {
  handleSelectClick = () => {
    this.props.onSelect(this.props.review);
  };

  render() {
    const { review } = this.props;

    return (
      <TableRow>
        <TableCell>{review.name}</TableCell>
        <TableCell>{review.text}</TableCell>
        <TableCell>
          <Button color="primary" onClick={this.handleSelectClick} variant="contained">
            Add to curated
          </Button>
        </TableCell>
      </TableRow>
    );
  }
}
