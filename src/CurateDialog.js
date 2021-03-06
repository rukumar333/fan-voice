import React, { Component } from 'react';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle, TextField, Typography } from '@material-ui/core';

export default class CurateModal extends Component {
  constructor(props) {
    super(props);

    const { review } = this.props;
    const [firstName, lastName] = review.name.split(' ');
    const lastInitial = lastName ? lastName[0] + '.' : '';
    this.state = {
      name: lastInitial ? firstName + ' ' + lastInitial : firstName,
      quote: review.quote
    };
  }

  handleSubmit = () => {
    this.props.onSubmit({
      id: this.props.review.id,
      name: this.state.name,
      quote: this.state.quote
    });
  }

  handleTextFieldChange = (event) => {
    this.setState({
      [event.target.name]: event.target.value
    });
  };

  render() {
    const { isOpen, onClose, review } = this.props;

    return (
      <Dialog open={isOpen}>
        <DialogTitle>Add this review to curated reviews</DialogTitle>
        <DialogContent>
          <Typography variant="h6">Name</Typography>
          <Typography variant="body2">Original: {review.name}</Typography>
          <TextField fullWidth label="Redacted Name" name="name" onChange={this.handleTextFieldChange} value={this.state.name} />
          <Typography variant="h6">Review Content</Typography>
          <Typography variant="body2">Original: {review.quote}</Typography>
          <TextField fullWidth label="Selected text" margin="normal" multiline name="quote" onChange={this.handleTextFieldChange} value={this.state.quote} variant="outlined" />
        </DialogContent>
        <DialogActions>
          <Button onClick={onClose}>
            Cancel
          </Button>
          <Button onClick={this.handleSubmit} color="primary">
            Add to Curated
          </Button>
        </DialogActions>
      </Dialog>
    );
  }
}
