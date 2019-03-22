import React, { Component } from 'react';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle, Divider, FormControl, NativeSelect, TextField, Typography } from '@material-ui/core';

export default class CurateModal extends Component {
  constructor(props) {
    super(props);

    const { review } = this.props;
    const [firstName, lastName] = review.name.split(' ');
    const lastInitial = lastName ? lastName[0] + '.' : '';
    this.state = {
      gender: '',
      name: lastInitial ? firstName + ' ' + lastInitial : firstName,
      quote: review.quote
    };
  }

  handleSubmit = () => {
    this.props.onSubmit({
      id: this.props.review.id,
      gender: this.state.gender,
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
        <DialogTitle>Add Curated Reviews</DialogTitle>
        <Divider classes={{root: "divider"}} />
        <DialogContent>
          <Typography variant="h6">Name</Typography>
          <Typography variant="body2" color="textSecondary">Original: {review.name}</Typography>
          <TextField fullWidth label="Redacted" name="name" onChange={this.handleTextFieldChange} value={this.state.name} />
          <FormControl>
            <NativeSelect
              classes={{root: 'select'}}
              name="gender"
              onChange={this.handleTextFieldChange}
              value={this.state.gender}
            >
              <option disabled value="">Gender (sorry)</option>
              <option value="man">Male</option>
              <option value="female">Female</option>
            </NativeSelect>
          </FormControl>
        </DialogContent>
        <Divider classes={{root: "divider"}} />
        <DialogContent>
          <Typography variant="h6">Review Content</Typography>
          <Typography variant="body2" color="textSecondary">Original: {review.quote}</Typography>
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
