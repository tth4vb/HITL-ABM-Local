import React, { Component } from 'react'
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts'

export default class DataSetChart extends Component {
    render () {
        const { modelData} = this.props
        return (
            <ResponsiveContainer width='100%' height={400}>
                <LineChart
                    data={modelData}
                    margin={{top: 5, right: 30, left: 20, bottom: 5}}
                >
                    <XAxis dataKey="name"/>
                    <YAxis />
                    <CartesianGrid strokeDasharray="3 3"/>
                    <Tooltip/>
                    <Legend />
                    <Line type="monotone" dataKey="Total Dataset Size" stroke="#4286f4" />
                </LineChart>
            </ResponsiveContainer>
        )
    }
}
