import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to Alloy HITL Simulation</h1>
        </header>
        <p className="App-intro">
          Place holder for eventual visualization
        </p>
        <p> new paragraph test</p>
        <TestClass/>
      </div>
    );
  }
}

class TestClass extends Component {
  render() {
    return(
      <div> This is a test </div>
    );
  }
}

export default App;
