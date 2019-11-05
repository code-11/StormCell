const mainReducer = (state={}, action) => {
	switch(action.type){
		case "TIME":
			return { ...state, time: action.time};
	}
}

export default mainReducer