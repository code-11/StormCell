import { connect } from 'react-redux';
import React, { Component } from "react";
import {getTime, pauseTime, startTime, getCountryShapes} from '../actions/index';
import playImg from '../../data/play.png';
import pauseImg from '../../data/pause.png';

function mapStateToProps(state) {
  return {}
  // return { time: state.time };
}

class TimeContols extends Component {
	constructor(props) {
    	super(props);
			this.state={
				displayPlay:true,
				time:0,
				timeCaller:null
			}
    }

		requestSetTime(){
			if(this.state!=undefined && !this.state.displayPlay){
				this.props.dispatch(getTime()).then(()=>{
							const newTime=this.props.store.getState().time;
							this.setState({time:newTime});
				});
			}
		}

		startGuiTime(){
			const timeCaller=setInterval(this.requestSetTime.bind(this), 1000);
			this.setState({timeCaller});
		}

		endGuiTime(){
			clearInterval(this.state.timeCaller);
		}

		onClickHandler(){
			const displayPlayNew=!this.state.displayPlay;
			this.setState({displayPlay:displayPlayNew});
			if(displayPlayNew){
					this.props.dispatch(pauseTime());
					this.endGuiTime();
			}else{
					this.props.dispatch(startTime());
					this.startGuiTime();
			}
		}

		month(monthNum){
			const months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
			return months[monthNum-1];
		}

    render(){
			const day=this.state.time ? this.state.time.day : 0;
			const month=this.state.time ? this.month(this.state.time.month) : 0;
			const year=this.state.time ? this.state.time.year : 0;
    	return <div>
					<img src={this.state.displayPlay ? playImg : pauseImg} style={{width:"20px",height:"20px"}} onClick={()=>this.onClickHandler()}/>
					{day} {month}, {year}
				</div>
    }
}
export default connect(mapStateToProps)(TimeContols);
