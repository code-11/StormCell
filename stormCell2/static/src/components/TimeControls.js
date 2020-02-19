import { connect } from 'react-redux';
import React, { Component } from "react";
import {getTime, pauseTime, startTime, getCountryShapes} from '../actions/index';
import playImg from '../../data/play.png';
import pauseImg from '../../data/pause.png';

const YEAR_IN_SECONDS = 31536000;
const GAME_DURATION = 50;  // years
const FULL_SECOND_DURATION = YEAR_IN_SECONDS * GAME_DURATION;
const TWO_HOURS = 7200;
const MULTIPLIER = FULL_SECOND_DURATION / TWO_HOURS;

const MILLISECONDS=1000;

function mapStateToProps(state) {
  return {}
  // return { time: state.time };
}

function timeDicToDate(timeDic){
  const toReturn = new Date();
  toReturn.setFullYear(timeDic.year, timeDic.month, timeDic.day);
  toReturn.setHours(timeDic.hour);
  return toReturn;
}

class TimeContols extends Component {
	constructor(props) {
    	super(props);
			this.state={
				displayPlay:true,
				serverTimeDic:0,
        frontEndDate:0,
				timeCaller:null
			}
    }

    componentDidMount(){
        this.syncTime();
    }

    syncTime(){
      this.props.dispatch(getTime()).then(()=>{
            const newTime=this.props.store.getState().time;
            this.setState({serverTimeDic:newTime, frontEndDate:timeDicToDate(newTime)});
      });
    }

		// requestSetTime(force){
		// 	if(this.state!=undefined && (!this.state.displayPlay || force)){
    //
		// 	}
		// }

    addOneSecond(){
      const oldDate=this.state.frontEndDate;
      const mult=MULTIPLIER;
      const milli=MILLISECONDS;
      this.setState({frontEndDate:new Date( oldDate.getTime() + .1 * mult * milli )});
    }

		startGuiTime(){
			const timeCaller=setInterval(this.addOneSecond.bind(this), 100);
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
			const day=this.state.frontEndDate ? this.state.frontEndDate.getDate() : 0;
			const month=this.state.frontEndDate ? this.month(this.state.frontEndDate.getMonth()) : 0;
			const year=this.state.frontEndDate ? this.state.frontEndDate.getFullYear() : 0;
    	return <div>
					<img src={this.state.displayPlay ? playImg : pauseImg} style={{width:"20px",height:"20px"}} onClick={()=>this.onClickHandler()}/>
					{day} {month}, {year}
				</div>
    }
}
export default connect(mapStateToProps)(TimeContols);
