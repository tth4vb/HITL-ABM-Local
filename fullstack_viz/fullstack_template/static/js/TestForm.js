import React from "react";

const formStyle = {
  fontSize: '16px',
  textAlign: 'center',
};

export default class TestForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {ae: undefined, trainingDataInput: undefined, ve: undefined};


    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ae: event.target.ae});
    this.setState({trainingDataInput: event.target.trainingDataInput});
    this.setState({ve: event.target.ve});

  }

  handleSubmit(event) {
    alert('algo starting accuracy submitted: ' + this.state.ae);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label style={formStyle}>
          Starting Algorithm Effectiveness:
          <input type="text" value={this.state.ae} onChange={this.handleChange} />
        </label>
        <br></br>
        <label style={formStyle}>
          Training Data Weekly Input
          <input type="text" value={this.state.trainingDataInput} onChange={this.handleChange} />
        </label>
        <br></br>
        <label style={formStyle}>
          Vizualization Effectiveness
          <input type="text" value={this.state.ve} onChange={this.handleChange} />
        </label>
        <br></br>
        <input style={formStyle} type="submit" value="Submit" />
      </form>
    );
  }
}
