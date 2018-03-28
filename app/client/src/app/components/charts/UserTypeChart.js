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
                    <Line type="monotone" dataKey="Adopter" stroke="#8884d8" dot={false} />
                    <Line type="monotone" dataKey="Trialer" stroke="#82ca9d" dot={false} />
                    <Line type="monotone" dataKey="Potential Trialer" stroke="#000000" dot={false}  />
                    <Line type="monotone" dataKey="Defector" stroke="#4286f4" dot={false} />
                    <Line type="monotone" dataKey="Evangelist" stroke="#e5d600" dot={false} />
                    <XAxis dataKey='iteration' type='number' />
                    <YAxis />
                    <Tooltip/>
                    <Legend />
                </LineChart>
            </ResponsiveContainer>
        )
    }
}