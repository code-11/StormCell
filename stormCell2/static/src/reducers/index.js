const mainReducer = (state={}, action) => {
	switch(action.type){
		case "GET_TIME":
			return { ...state, time: action.time};
		case "PAUSED_TIME":
			return { ...state, timeRate: "PAUSED"};
	}
}

export default mainReducer