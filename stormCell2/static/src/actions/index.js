// dispatch(requestPosts(subreddit))

const requestTime = () => {
    return {
        type:"ASK_TIME",
    };
};

const receiveTime = (time) => {
    return {
        type:"GET_TIME",
        time: time
    };
};

export const getTime = () =>{
    return (dispatch) =>{
        dispatch({type:"ASK_TIME"});
        return fetch("/time")
        .then((response)=>response.json())
        .then((time)=>{
            console.log(time);
            dispatch(receiveTime(time));
        });
    };
};

export const pauseTime = () =>{
    return (dispatch) =>{
        dispatch({type:"PAUSING_TIME"});
        return fetch("/pauseTime")
        .then((response)=>response.json())
        .then((success))=>{
            console.log("Stopped server clock");
            dispatch({type:"PAUSED_TIME"});
        }
    }
}

// export const getTime = (dispatch, getState) => {
//     return dispatch(sendGetTime);
// }

// let nextTaskId = 0;

// export const addTask = ({ text, executor }) => {
//     return {
//         type: 'ADD_TASK',
//         id: (nextTaskId++).toString(),
//         text,
//         executor
//     };
// };

// export const removeTask = (id) => {
//     return {
//         type: 'REMOVE_TASK',
//         id
//     };
// };

// export const changeTaskStatus = (id) => {
//     return {
//         type: 'CHANGE_TASK_STATUS',
//         id
//     };
// };