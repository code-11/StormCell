import { connect } from 'react-redux';
import React, { Component } from "react";
import {pauseTime, startTime} from '../actions/index';

class TimeContols extends Component {
	constructor(props) {
    	super(props);
    }

    render(){
    	return <div>
					<button type="button" onClick={()=>this.props.dispatch(pauseTime())}> Pause </button>
					<button type="button" onClick={()=>this.props.dispatch(startTime())}> Play </button>
				</div>
    }
}
export default connect()(TimeContols);