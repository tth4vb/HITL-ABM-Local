import { combineReducers } from 'redux'
import modelReducer from './modelReducer'

const rootReducer = combineReducers({
  modelData: modelReducer
})

export default rootReducer
