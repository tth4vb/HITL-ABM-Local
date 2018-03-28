import React from "react";
import Hello from "./Hello";
import TestForm from "./TestForm";
import { PageHeader } from "react-bootstrap";

require('../css/fullstack.css');
var $ = require('jquery');

const pStyle = {
  fontSize: '16px',
  float: 'none',
  margin: '0 auto',
};

export default class App extends React.Component {
    constructor(props) {
        super(props);
    }


    render () {
        return (
            <PageHeader>
                <div className='header-contents'>
                  <p style={pStyle}> Once the model runs, the empty charts below will depict the model output over time for key KPIs</p>
                  <TestForm style={pStyle} />
                  <Hello name='Hello' />
                </div>
            </PageHeader>
        );
    }
}
