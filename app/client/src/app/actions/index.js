import { GET_DATA } from './types'

export const getData = () => async dispatch => {
    const res = await fetch('/api/model')
    const data = await res.json()

    // convert the object into an array of object values using Object.values which creates and array from the object keys
    const dataArray = Object.values(data).map((datum, index) => {
        return Object.assign({}, datum, {'iteration': index + 1})
    })
    dispatch({ type: GET_DATA, payload: dataArray })
  }
