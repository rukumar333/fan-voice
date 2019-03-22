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
      <TableRow selected={review.is_curated}>
        <TableCell><OneLine>{review.name}</OneLine></TableCell>
        <TableCell>{review.quote}</TableCell>
        <TableCell>
          <div style={{color: review.polarity === 'positive' ? 'green' : 'red'}}>{review.polarity}</div>
        </TableCell>
        <TableCell>
          <OneLine>
            {review.is_curated ? 'Added!' :
              <Button color="primary" onClick={this.handleSelectClick} variant="contained">
                Add to curated
              </Button>
            }
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
