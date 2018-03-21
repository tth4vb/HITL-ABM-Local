import React, { Component } from 'react';
import {LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend} from 'recharts';
import './App.css';
import model_output2 from './data/model_output2.json';
import axios from 'axios';

var masterJSON = model_output2;


//var masterJSON = model_output2;


const dataFrame=[];
for (var key in masterJSON){
  dataFrame.push(masterJSON[key]);
};

class App extends Component {
  constructor() {
          super();
          this.state = {
            density: '',
            wms: '',
            wts: '',
            wus: '',
            trainingDataWeeklyInput: '',
            ve: '',
            ae: '',
          };
        }

        onChange = (e) => {
                // Because we named the inputs to match their corresponding values in state, it's
                // super easy to update the state
                const state = this.state
                state[e.target.name] = e.target.value;
                this.setState(state);
              }

              onSubmit = (e) => {
                e.preventDefault();
                // get our form data out of state
                const { density, wms, wts, wus, trainingDataWeeklyInput, ve, ae } = this.state;

                axios.post('http://127.0.0.1:5000/', { density, wms, wts, wus, trainingDataWeeklyInput, ve, ae })
                  .then(function (response) {
                        console.log(response);
                      })
                      .catch(function (error) {
                  console.log(error);
                  });
                }
  render () {
    const { density, wms, wts, wus, trainingDataWeeklyInput, ve, ae } = this.state;
    return (
      <div className="App">
        <header className="App-header">

          <h4 className="App-title">Below is a series of charts that represent the output over time of an
          Agent-Based Model Simulation of a Human-In-The-Loop Solution</h4>
        </header>

        <form onSubmit={this.onSubmit}>
            <label>Density</label><br></br>
            <input type="number" name="density" value={density} onChange={this.onChange} /><br></br><br></br>
<label>Weekly Marketing Spend</label><br></br>
            <input type="number" name="wms" value={wms} onChange={this.onChange} /><br></br><br></br>
<label>Weekly Training Spend</label><br></br>
            <input type="number" name="wts" value={wts} onChange={this.onChange} /><br></br><br></br>
<label>Weekly Usability Spend</label><br></br>
            <input type="number" name="wus" value={wus} onChange={this.onChange} /><br></br><br></br>
<label>Training Data Weekly Input</label><br></br>
            <input type="number" name="trainingDataWeeklyInput" value={trainingDataWeeklyInput} onChange={this.onChange} /><br></br><br></br>
<label>Visualization Effect</label><br></br>
            <input type="number" name="ve" value={ve} onChange={this.onChange} /><br></br><br></br>
<label>Algorithm Starting Accuracy</label><br></br>
            <input type="number" name="ae" value={ae} onChange={this.onChange} /><br></br><br></br>

            <button type="submit">Run</button>
          </form>
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
