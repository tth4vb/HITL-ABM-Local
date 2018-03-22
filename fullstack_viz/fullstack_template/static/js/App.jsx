import React from "react";
import Hello from "./Hello";
import { PageHeader } from "react-bootstrap";

var $ = require('jquery');


export default class App extends React.Component {
    constructor(props) {
        super(props);
    }
    addHeaderImg() {
        let headerBg = new Image();
        headerBg.src = HeaderBackgroundImage;
    }

    render () {
        return (
            <PageHeader>
                <div className='header-contents'>
                {this.addHeaderImg()}
                <Hello name='Rimini' />
                </div>
            </PageHeader>
        );
    }
}
