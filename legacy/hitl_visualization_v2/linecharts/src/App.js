import React, { Component } from 'react';
import {LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend} from 'recharts';
import './App.css';
import logo from './logo.svg';
import model_output2 from './data/model_output2.json';

var masterJSON = model_output2;


//var masterJSON = model_output2;


const dataFrame=[];
for (var key in masterJSON){
  dataFrame.push(masterJSON[key]);
};

class App extends Component {
  render () {
    return (
      <div className="App">
        <header className="App-header">

          <h4 className="App-title">Below is a series of charts that represent the output over time of an
          Agent-Based Model Simulation of a Human-In-The-Loop Solution</h4>
        </header>

      <LineChart width={1400} height={400} data={dataFrame}
            margin={{top: 5, right: 30, left: 20, bottom: 5}}>
       <XAxis dataKey="name"/>
       <YAxis/>
       <CartesianGrid strokeDasharray="3 3"/>
       <Tooltip/>
       <Legend />
       <Line type="monotone" dataKey="Adopter" stroke="#8884d8" activeDot={{r: 8}}/>
       <Line type="monotone" dataKey="Trialer" stroke="#82ca9d" />
       <Line type="monotone" dataKey="Potential Trialer" stroke="#000000" />
      </LineChart>

      <LineChart width={1400} height={200} data={dataFrame}
            margin={{top: 5, right: 30, left: 20, bottom: 5}}>
       <XAxis dataKey="name"/>
       <YAxis/>
       <CartesianGrid strokeDasharray="3 3"/>
       <Tooltip/>
       <Legend />
       <Line type="monotone" dataKey="Defector" stroke="#4286f4" />
       <Line type="monotone" dataKey="Evangelist" stroke="#e5d600" />
      </LineChart>
      <LineChart width={1400} height={200} data={dataFrame}
            margin={{top: 5, right: 30, left: 20, bottom: 5}}>
       <XAxis dataKey="name"/>
       <YAxis/>
       <CartesianGrid strokeDasharray="3 3"/>
       <Tooltip/>
       <Legend />
       <Line type="monotone" dataKey="Algo Accuracy" stroke="#4286f4" />
      </LineChart>
      <LineChart width={1400} height={200} data={dataFrame}
            margin={{top: 5, right: 30, left: 20, bottom: 5}}>
       <XAxis dataKey="name"/>
       <YAxis/>
       <CartesianGrid strokeDasharray="3 3"/>
       <Tooltip/>
       <Legend />
       <Line type="monotone" dataKey="Algo Accuracy Increase" stroke="#4286f4" />
      </LineChart>
      <LineChart width={1400} height={200} data={dataFrame}
            margin={{top: 5, right: 30, left: 20, bottom: 5}}>
       <XAxis dataKey="name"/>
       <YAxis/>
       <CartesianGrid strokeDasharray="3 3"/>
       <Tooltip/>
       <Legend />
       <Line type="monotone" dataKey="Total Dataset Size" stroke="#4286f4" />
      </LineChart>

      </div>

    );
  }
}

export default App;
