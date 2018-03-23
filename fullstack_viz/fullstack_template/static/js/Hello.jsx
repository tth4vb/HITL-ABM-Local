import React from "react";
import { Button, Grid, Row, Col } from "react-bootstrap";
import {LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend} from 'recharts';

var $ = require('jquery');

export default class Hello extends React.Component {
    constructor(props) {
        super(props);
        this.state = {json:[]};

        // This binding is necessary to make `this` work in the callback
        this.getPythonJSON = this.getPythonJSON.bind(this);
    }

    implementJSON(json) {
      console.log(json);
      var dataFrame =[];
      for (var key in json){
        dataFrame.push(json[key]);
      };
      console.log(dataFrame);
      this.setState({json: dataFrame});
    }

    getPythonJSON() {
        $.getJSON(window.location.href + 'hello', (data) => {
            console.log(data);
            this.implementJSON(data);
        });
    }

    render () {
        return (
            <Grid>
                <Row>
                  <Col md={7} mdOffset={5}>
                    <Button bsSize="large" bsStyle="danger" onClick={this.getPythonJSON}>
                    Run Model
                    </Button>
                    </Col>
                </Row>
                <Row>
                <Col md={7} mdOffset={5}>
                  <LineChart width={1400} height={400} data={this.state.json}
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
                    <LineChart width={1400} height={200} data={this.state.json}
                          margin={{top: 5, right: 30, left: 20, bottom: 5}}>
                     <XAxis dataKey="name"/>
                     <YAxis/>
                     <CartesianGrid strokeDasharray="3 3"/>
                     <Tooltip/>
                     <Legend />
                     <Line type="monotone" dataKey="Defector" stroke="#4286f4" />
                     <Line type="monotone" dataKey="Evangelist" stroke="#e5d600" />
                    </LineChart>
                    <LineChart width={1400} height={200} data={this.state.json}
                          margin={{top: 5, right: 30, left: 20, bottom: 5}}>
                     <XAxis dataKey="name"/>
                     <YAxis/>
                     <CartesianGrid strokeDasharray="3 3"/>
                     <Tooltip/>
                     <Legend />
                     <Line type="monotone" dataKey="Algo Accuracy" stroke="#4286f4" />
                    </LineChart>
                    <LineChart width={1400} height={200} data={this.state.json}
                          margin={{top: 5, right: 30, left: 20, bottom: 5}}>
                     <XAxis dataKey="name"/>
                     <YAxis/>
                     <CartesianGrid strokeDasharray="3 3"/>
                     <Tooltip/>
                     <Legend />
                     <Line type="monotone" dataKey="Algo Accuracy Increase" stroke="#4286f4" />
                    </LineChart>
                    <LineChart width={1400} height={200} data={this.state.json}
                          margin={{top: 5, right: 30, left: 20, bottom: 5}}>
                     <XAxis dataKey="name"/>
                     <YAxis/>
                     <CartesianGrid strokeDasharray="3 3"/>
                     <Tooltip/>
                     <Legend />
                     <Line type="monotone" dataKey="Total Dataset Size" stroke="#4286f4" />
                    </LineChart>
                    <hr/>
                </Col>
                </Row>

            </Grid>
        );
    }
}
