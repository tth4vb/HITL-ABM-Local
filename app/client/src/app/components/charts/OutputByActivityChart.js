import React, { Component } from 'react'
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip, Legend } from 'recharts'

export default class UserTypeChart extends Component {
    render() {
        const { modelData } = this.props
        return (
            <ResponsiveContainer width='100%' height={400}>
                <LineChart
                    data={modelData}
                >
                    <Line type="monotone" dataKey="Avg Data Collection Output" stroke="#8884d8" dot={false} />
                    <Line type="monotone" dataKey="Avg Data Interpretation/Analysis Output" stroke="#82ca9d" dot={false} />
                    <Line type="monotone" dataKey="Avg Interpreting Actions Output" stroke="#000000" dot={false}  />
                    <Line type="monotone" dataKey="Avg Coaching Output" stroke="#4286f4" dot={false} />
                    <Line type="monotone" dataKey="Avg Review Output" stroke="#e5d600" dot={false} />
                    <XAxis dataKey='iteration' type='number' />
                    <YAxis/>
                    <Tooltip/>
                    <Legend />
                </LineChart>
            </ResponsiveContainer>
        )
    }
}