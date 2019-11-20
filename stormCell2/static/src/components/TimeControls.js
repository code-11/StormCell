import { connect } from 'react-redux';
import React, { Component } from "react";
import {pauseTime, startTime, getCountryShapes} from '../actions/index';

class TimeContols extends Component {
	constructor(props) {
    	super(props);
    }

    render(){
    	return <div>
					<button type="button" onClick={()=>this.props.dispatch(pauseTime())}> Pause </button>
					<button type="button" onClick={()=>this.props.dispatch(startTime())}> Play </button>
					<button type="button" onClick={()=>this.props.dispatch(getCountryShapes())}> Get Country Shapes </button>
				</div>
    }
}
export default connect()(TimeContols);