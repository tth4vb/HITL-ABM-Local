import { GET_DATA } from '../actions/types'

export default function(state = [], action) {
  switch (action.type) {
    case GET_DATA:
      return action.payload || false
    default:
      return state
  }
}
