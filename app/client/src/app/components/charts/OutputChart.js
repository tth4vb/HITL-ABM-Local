import React, { Component } from 'react'
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip, Legend } from 'recharts'

export default class OutputChart extends Component {
    render () {
        const { modelData} = this.props
        return (
            <ResponsiveContainer width='100%' height={400}>
                <LineChart
                    data={modelData}
                >
                    <XAxis dataKey='iteration' type='number' />
                    <YAxis domain={[2900, 3000]}/>
                    <Tooltip/>
                    <Legend />
                    <Line type="monotone" dataKey="Avg Output Value Per Person" stroke="#4286f4" dot={false} />
                </LineChart>
            </ResponsiveContainer>
        )
    }
}
