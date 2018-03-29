import React, { Component } from 'react'
import { connect } from 'react-redux'
import * as actions from '../actions'
import UserTypeChart from './charts/UserTypeChart'
import AlgorithmChart from './charts/AlgorithmChart'
import OutputChart from './charts/OutputChart'
import DataSetChart from './charts/DataSetChart'
import OutputByActivityChart from './charts/OutputByActivityChart'

class Model extends Component {

    componentDidMount() {
        // call action creator to refresh model data and update redux store values
        return this.props.getData()
    }

    handleRefreshModelData() {
        // call action creator to refresh model data and update redux store values
        return this.props.getData()
    }

    render () {
        const { modelData } = this.props
        console.log(modelData)
        return (
            <div>
                <div className='row'>
                    <div className='col col-12'>
                        <UserTypeChart 
                            modelData={modelData}
                        />
                    </div>
                </div>
                <div className='row'>
                    <div className='col col-12'>
                        <AlgorithmChart
                            modelData={modelData}
                        />

                    </div>
                </div>
                <div className='row'>
                    <div className='col col-12'>
                        <OutputChart
                            modelData={modelData}
                        />
                    </div>
                </div>
                <div className='row'>
                    <div className='col col-12'>
                        <OutputByActivityChart
                            modelData={modelData}
                        />
                    </div>
                </div>
                <div className='row'>
                    <div className='col col-12'>
                        <DataSetChart
                            modelData={modelData}
                        />
                    </div>
                </div>
            </div>
        )
    }
}

function mapStateToProps({ modelData }) {
    return { modelData }
}

export default connect(mapStateToProps, actions)(Model)
