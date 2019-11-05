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

export const getTime = (dispatch) =>{
    dispatch(requestTime);
    return fetch("/time").then((time)=>{
        dispatch(receiveTime(time));
    });
};

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