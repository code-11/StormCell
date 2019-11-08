const mainReducer = (state={}, action) => {
	switch(action.type){
		case "GET_TIME":
			return { ...state, time: action.time};
	}
}

export default mainReducer