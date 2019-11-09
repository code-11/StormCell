import {pauseTime, startTime} from '../actions/index';

export default class TimeContols extends Component {
	constructor(props) {
    	super(props);
    }

    render(){
    	<div>
    		<button type="button" onClick={()=>this.props.dispatch(pauseTime())}> Pause </button>
        	<button type="button" onClick={()=>this.props.dispatch(startTime())}> Play </button>
        </div>
    }
}