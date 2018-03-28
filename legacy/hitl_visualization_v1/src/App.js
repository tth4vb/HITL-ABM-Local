import React, { Component } from 'react';
import { XAxis, YAxis, CartesianGrid, Area, LineChart, Line, AreaChart, Tooltip,
  ResponsiveContainer } from 'recharts';
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
          Visualization should appear below
        </p>
        <TestClass/>
        <LineChart width={500} height={300} data={data}>
   <XAxis dataKey="name"/>
   <YAxis/>
   <CartesianGrid stroke="#eee" strokeDasharray="5 5"/>
   <Line type="monotone" dataKey="uv" stroke="#8884d8" />
   <Line type="monotone" dataKey="pv" stroke="#82ca9d" />
 </LineChart>
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
