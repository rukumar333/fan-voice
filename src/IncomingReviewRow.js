import React, { Component } from 'react';
import styled from 'styled-components';
import { Button, TableCell, TableRow } from '@material-ui/core';

export default class IncomingReviewRow extends Component {
  handleSelectClick = () => {
    this.props.onSelect(this.props.review);
  };

  render() {
    const { review } = this.props;

    return (
      <TableRow>
        <TableCell><OneLine>{review.name}</OneLine></TableCell>
        <TableCell>{review.text}</TableCell>
        <TableCell>
          <OneLine>
            <Button color="primary" onClick={this.handleSelectClick} variant="contained">
              Add to curated
            </Button>
          </OneLine>
        </TableCell>
      </TableRow>
    );
  }
}

const OneLine = styled.div`
  text-overflow: ellipsis;
  white-space: nowrap;
`;
