import { connect } from 'react-redux';
import React, { Component } from "react";
import {pauseTime, startTime, getCountryShapes} from '../actions/index';
import playImg from '../../data/play.png';
import pauseImg from '../../data/pause.png';

class TimeContols extends Component {
	constructor(props) {
    	super(props);
			this.state={
				displayPlay:true,
			}
    }

		onClickHandler(){
			const displayPlayNew=!this.state.displayPlay;
			this.setState({displayPlay:displayPlayNew});
			if(displayPlayNew){
					this.props.dispatch(pauseTime());
			}else{
					this.props.dispatch(startTime());
			}
		}

    render(){
    	return <div>
					<img src={this.state.displayPlay ? playImg : pauseImg} style={{width:"20px",height:"20px"}} onClick={()=>this.onClickHandler()}/>
				</div>
    }
}
export default connect()(TimeContols);
