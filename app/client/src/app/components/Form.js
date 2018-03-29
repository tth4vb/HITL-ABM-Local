import React, { Component } from 'react'
import { connect } from 'react-redux'
import * as actions from '../actions'

class Form extends Component {

    handleRefreshModelData() {
        // call action creator to refresh model data and update redux store values
        return this.props.getData()
    }

    render () {
        return (
            <div className='form'>
                <button
                    onClick={(e) => this.handleRefreshModelData(e)}
                    className='button-primary'
                >
                    Refresh Model
                </button>
            </div>
        )
    }
}

export default connect(null, actions)(Form)
