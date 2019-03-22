import React, { Component } from 'react';
import styled from 'styled-components';
import { TableCell, TableRow } from '@material-ui/core';

export default class CuratedReviewRow extends Component {
  render() {
    const { review } = this.props;
    return (
      <TableRow>
        <TableCell><OneLine>{review.name}</OneLine></TableCell>
        <TableCell>{review.quote}</TableCell>
      </TableRow>
    );
  }
}

const OneLine = styled.div`
  text-overflow: ellipsis;
  white-space: nowrap;
`;
